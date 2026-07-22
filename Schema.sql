-- โครงสร้างฐานข้อมูลสำหรับ GuardianSense

-- ตารางผู้ใช้งาน/เจ้าหน้าที่ (สำหรับ Role-based Access)
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('NURSE', 'DOCTOR', 'ADMIN') NOT NULL
);

-- ตารางข้อมูลผู้ป่วยและห้องพัก
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    room_number VARCHAR(10) NOT NULL
);

-- ตารางบันทึกเหตุการณ์ (Fall Event Logs) จากอุปกรณ์ Edge
CREATE TABLE fall_events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    device_id VARCHAR(50) NOT NULL,
    severity ENUM('GREEN', 'YELLOW', 'RED') NOT NULL,
    keypoints_data JSON, -- เก็บพิกัดโครงกระดูก (ไม่มีภาพจริง)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);