from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI(title="GuardianSense Backend API")

# รูปแบบ Data Payload ที่ Edge AI ส่งมาให้ Backend
class SensorPayload(BaseModel):
    device_id: str
    patient_id: int
    severity: str  # GREEN, YELLOW, RED
    keypoints: Optional[dict] = None
    vital_abnormal: bool = False

def trigger_mobile_alert(patient_id: int, severity: str, room_no: str):
    """
    ฟังก์ชันจำลองการยิง Push Notification หรือ Webhook ไปยังมือถือพยาบาล/แพทย์
    """
    if severity == "RED":
        print(f"[EMERGENCY ALERT] ผู้ป่วย {patient_id} ห้อง {room_no} ล้มและไม่ขยับ + Vital ผิดปกติ! ต้องการความช่วยเหลือด่วน!")
    elif severity == "YELLOW":
        print(f"[WARNING] ผู้ป่วย {patient_id} ห้อง {room_no} ล้มแต่ยังขยับได้ กรุณาตรวจสอบ")

@app.post("/api/v1/events")
async def receive_fall_event(payload: SensorPayload):
    """
    Endpoint รับข้อมูลจาก Edge Device (สมมติว่าเชื่อมต่อผ่าน mTLS แล้ว)
    """
    if payload.severity not in ["GREEN", "YELLOW", "RED"]:
        raise HTTPException(status_code=400, detail="Invalid severity level")

    # TODO: นำข้อมูล Insert ลงฐานข้อมูลตาราง fall_events ตรงนี้
    # db.execute("INSERT INTO fall_events (patient_id, device_id, severity, keypoints_data) VALUES (...)")
    
    # ดึงข้อมูลห้องพัก (สมมติว่า Query มาจาก DB)
    mock_room_no = "309" if payload.severity == "RED" else "204"
    
    # ---------------------------------------------------------
    # Logic ตาม Severity Table ของ GuardianSense
    # ---------------------------------------------------------
    if payload.severity == "GREEN":
        # เขียว: เฝ้าระวังท่าทางปกติ -> บันทึกข้อมูลลง DB อย่างเดียว
        print(f"Log: ท่าทางปกติ (Room {mock_room_no})")
        
    elif payload.severity == "YELLOW":
        # เหลือง: ล้มแต่ยังขยับได้ -> บันทึกและแจ้งเตือนปานกลาง
        trigger_mobile_alert(payload.patient_id, payload.severity, mock_room_no)
        
    elif payload.severity == "RED":
        # แดง: ล้มและไม่ขยับ (+ Vital ผิดปกติ) -> แจ้งฉุกเฉินทันที
        trigger_mobile_alert(payload.patient_id, payload.severity, mock_room_no)

    return {"status": "success", "message": "Event logged securely"}