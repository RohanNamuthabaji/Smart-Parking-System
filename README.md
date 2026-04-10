# 🚗 Smart Parking System

A full-stack web application that allows users to book parking slots dynamically with real-time slot availability visualization.

## 📌 Project Overview

The Smart Parking System is designed to automate parking slot management. Users can register, log in, and book available parking slots. The system visually represents slot availability using color indicators (green for available, red for booked).

## ✨ Features

* 🔐 User Registration & Login System
* 🚗 Parking Slot Booking
* 🟩🟥 Real-time Slot Availability (Green = Free, Red = Booked)
* 💳 Payment Simulation
* 📊 Booking Data Stored in MySQL Database
* 🌐 Web-based Interface

## 🛠️ Technologies Used

* **Frontend:** HTML, CSS
* **Backend:** Python (Flask)
* **Database:** MySQL
* **Version Control:** Git & GitHub

## 🧱 System Architecture

User → Web Interface → Flask Backend → MySQL Database

## 📂 Project Structure

SmartParkingSystem/
│
├── app.py
├── templates/
│   ├── index.html
│   └── dashboard.html
├── README.md

## ⚙️ Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/Smart-Parking-System.git
cd Smart-Parking-System
```

### Step 2: Install Dependencies

```bash
pip install flask mysql-connector-python
```

### Step 3: Setup Database

Open MySQL and run:

```sql
CREATE DATABASE smart_parking;

USE smart_parking;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50)
);

CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    slot INT,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Step 4: Update Database Credentials

Edit `app.py` and update your MySQL password:

```python
password="your_password"
```

### Step 5: Run the Application

```bash
python app.py
```

### Step 6: Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🧪 How It Works

1. User registers and logs in
2. Dashboard displays available parking slots
3. User selects a slot
4. System stores booking in database
5. Slot turns red (booked)

---

## 📸 Screenshots
<img width="1917" height="1015" alt="Screenshot 2026-03-18 155929" src="https://github.com/user-attachments/assets/e8016fe0-623d-44ae-9919-7f0c821492cd" />
<img width="792" height="856" alt="Screenshot 2026-03-18 160559" src="https://github.com/user-attachments/assets/8f6bc831-2b6f-4f9a-a1b7-c3d046ef9c39" />
<img width="950" height="553" alt="Screenshot 2026-03-18 161157" src="https://github.com/user-attachments/assets/9e0d94fd-67eb-404f-a2b2-8f0eaaa146db" />
<img width="948" height="432" alt="Screenshot 2026-03-18 161753" src="https://github.com/user-attachments/assets/076b0fe9-513d-4f77-8f79-9b2484bf1147" />
<img width="950" height="533" alt="Screenshot 2026-03-18 161540" src="https://github.com/user-attachments/assets/6a8533fb-0494-44e8-9a7c-1aebcbc7cf3a" />



## 🚀 Future Enhancements

* 📷 QR Code-based ticket system
* 📊 Admin dashboard
* 💳 Real payment gateway integration
* 📱 Mobile responsive UI
* ☁️ Cloud deployment

---

## 👨‍💻 Author

Developed by NAMUTHABAJI ROHAN

---

## 📄 License

This project is for educational purposes.
