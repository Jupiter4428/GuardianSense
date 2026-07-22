# GuardianSense: Secure Skeleton Monitoring 🛡️

**ระบบตรวจจับการล้มด้วย AI สำหรับผู้สูงอายุและผู้ป่วย — Hackathon Proposal**[cite: 1]

GuardianSense คือระบบตรวจจับการล้มที่ออกแบบมาเพื่อความเป็นส่วนตัวสูงสุด (Privacy-First) ประมวลผลบนอุปกรณ์ Edge แบบ Real-time โดยไม่มีการบันทึกภาพจริง (No Video-at-Rest) ข้อมูลที่ส่งออกมีเพียงพิกัดโครงกระดูก (Keypoints) และผลการวิเคราะห์ท่าทาง ทำให้รักษาความเป็นส่วนตัวได้เต็มรูปแบบ พร้อมระบบแจ้งเตือนผ่านช่องทางที่เข้ารหัส[cite: 1, 2]

## 🌟 จุดเด่นของโครงการ (Impact)
* **Privacy-First:** ระบบไม่เคยเก็บหรือส่งภาพจริงออกจากอุปกรณ์ ตลอดกระบวนการทำงาน[cite: 2]
* **Fast Response:** ลดเวลาช่วยเหลือจากชั่วโมงเป็นนาที[cite: 1, 2]
* **High Acceptance:** เพิ่มการยอมรับในการติดตั้งในพื้นที่ส่วนตัว เช่น ห้องนอน ห้องน้ำ[cite: 1, 2]
* **Workload Reduction:** ลดภาระบุคลากรพยาบาลที่มีจำนวนจำกัด ในการดูแลผู้ป่วยที่ช่วยเหลือตัวเองไม่ได้[cite: 2]

## 🏗️ สถาปัตยกรรมระบบ (4 Layers)
ระบบทำงานผ่าน 4 ชั้นหลัก จากเซนเซอร์สู่การแจ้งเตือน:[cite: 1, 2]

1. **Sensing Layer:** กล้อง Skeleton, เรดาร์ mmWave, เซนเซอร์ IMU[cite: 1, 2]
2. **Edge AI Layer:** ประมวลผล Pose Estimation (BlazePose/MobileNet) และ Sensor Fusion เพื่อลด False Alarm[cite: 1, 2]
3. **Secure Transport Layer:** ใช้ Mutual TLS (mTLS), PKI และแนวคิด Zero-Trust ยืนยันตัวตนทุกครั้งที่เชื่อมต่อ[cite: 1, 2]
4. **Application Layer:** Dashboard แสดงสถานะห้องพัก และระบบแจ้งเตือน Mobile Alert ทันที[cite: 1, 2]

## 🚥 ระดับการแจ้งเตือน (Severity Table)
* 🟢 **สีเขียว (เฝ้าระวัง):** ท่าทางปกติ ระบบทำการบันทึกข้อมูลเฉย ๆ[cite: 1, 2]
* 🟡 **สีเหลือง (ล้มแต่ยังขยับได้):** ตรวจพบการล้ม ระบบแจ้งเตือนระดับปานกลาง[cite: 1, 2]
* 🔴 **สีแดง (เข้าข่ายฉุกเฉิน):** ล้มและไม่ขยับ + ค่าสัญญาณชีพ (Vital) ผิดปกติ ระบบแจ้งฉุกเฉินทันที[cite: 1, 2]

## 🔐 Security & Privacy Features
* **No Video-at-Rest:** สกัด Keypoints แล้วทิ้งภาพทันที ไม่มีภาพหลุดออกจากอุปกรณ์[cite: 1, 2]
* **mTLS Authentication:** ยืนยันตัวตนอุปกรณ์และเซิร์ฟเวอร์ทุกครั้งที่เชื่อมต่อ[cite: 2]
* **Role-based Access:** พยาบาลและแพทย์เห็นข้อมูลในระดับสิทธิ์ที่แตกต่างกันบน Dashboard[cite: 1, 2]

## 🚀 Hackathon Timeline (36–48 ชม.)
* **Phase 1:** Setup Sensor[cite: 1, 2]
* **Phase 2:** Pose Estimation + Data Collection[cite: 1, 2]
* **Phase 3:** Model Fusion + Rule-based[cite: 1, 2]
* **Phase 4:** Secure Transport Integration[cite: 1, 2]
* **Phase 5:** Dashboard + Demo[cite: 1, 2]

## 🔮 แผนการในอนาคต (Future Work)
* ขยายผลการติดตั้งทั้งชั้นและอาคาร ในโรงพยาบาลและสถานดูแลผู้สูงอายุ[cite: 1, 2]
* เชื่อมต่อหุ่นยนต์บริการให้เคลื่อนที่ไปยังจุดเกิดเหตุพร้อมชุดปฐมพยาบาล[cite: 1, 2]
