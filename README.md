# PlantaSanitus🌿 - Smart Agriculture Platform

[![Official Website](https://img.shields.io/badge/Official%20Website-https%3A%2F%2Fplantasanitus.com-brightgreen.svg)](https://plantasanitus.com)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange.svg)](https://www.tensorflow.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green.svg)](https://flask.palletsprojects.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-Academic%20Educational-purple.svg)]()

> **Final Year Computer Science & Engineering Capstone Project**  
> **Developed by:** Rifanshiya J S  
> **Official Web Domain:** [https://plantasanitus.com](https://plantasanitus.com)

---

## 📖 Project Overview

**PlantaSanitus🌿** ([https://plantasanitus.com](https://plantasanitus.com)) is an enterprise Smart Agriculture Platform integrating artificial intelligence (AI), computer vision, explainable AI (XAI), multi-image diagnostics, weather intelligence, soil health NPK analytics, an agro-medicine e-commerce marketplace, live order tracking, multi-farm management, CIA Triad security compliance, and a multilingual voice/text AI assistant.

---

## 🚀 Key Modules & System Capabilities

1. **Multi-Role Authentication & Account Manager**:
   - Distinct account roles: **Farmer** (default), **Agro-Medicine Seller**, and **Admin**.
   - User account registration, login authentication, profile manager, and secure session logout.
2. **AI & Explainable AI (XAI) Multi-Image Diagnostics**:
   - Upload 1 to 3 leaf photos for multi-angle AI consensus.
   - Severity classification (🟢 Mild / 🟡 Moderate / 🔴 Severe), treatment urgency, and estimated recovery timeline.
   - Explainable AI (XAI) feature analysis pinpointing leaf lesions and chlorosis halos.
3. **Agro-Chemical Dosage Calculator**:
   - Input field size in acres (e.g. `2 Acres`) to calculate exact fungicide volume (`480 ml`) and water required (`160 L`).
   - Spraying schedule generator (Day 1 ➔ Day 7 ➔ Day 14).
4. **Weather Intelligence & Disease Risk Forecasting**:
   - Real-time weather widget (temperature, humidity, wind speed, rain outlook).
   - Fungal disease risk forecasting (e.g. 85% Powdery Mildew risk alert).
5. **Soil Health NPK & pH Analyzer**:
   - Analyzes pH, Nitrogen (N), Phosphorus (P), and Potassium (K) test values and calculates organic/chemical fertilizer requirements per acre.
6. **Agro-Medicine E-Commerce Marketplace & CIA Secured Payments**:
   - Organic & chemical products catalog with AI-recommendation badges and verified seller tags.
   - Detailed product page with QR Code usage guides and video tutorial links pointing to `https://plantasanitus.com`.
   - Shopping cart, digital payment gateway simulation (UPI, Luhn-checked Credit Card, COD), HMAC tokenization, live delivery tracking timeline, and 1-click order cancellation.
7. **Seller Studio & Admin Control Panel**:
   - Sellers manage products and receive low inventory alerts (<= 15 units).
   - System Admins audit users, scans, and marketplace listings.
8. **AgriBot AI Voice & Multilingual Assistant**:
   - Voice speech input/output and text chat in regional languages (Tamil, Hindi, Telugu, Kannada, English).
9. **Farmer Community Forum & Government Schemes**:
   - Community Q&A forum with expert verification tags.
   - Catalog of government crop insurance (PMFBY), subsidies (PKVY), and organic certification guides.

---

## 📁 Project Structure

```
Plant-Disease-Detection/
├── database.py                 # Master SQLite database engine (Users, Scans, Products, Orders, Farms)
├── app.py                      # Master Flask application server
├── predict.py                  # Computer Vision, Multi-Image & XAI Engine
├── disease_info.py             # 38-class medical knowledge base
├── weather_service.py          # Weather Intelligence service
├── soil_service.py             # Soil Health NPK calculator
├── qr_service.py               # Product QR Code generator for https://plantasanitus.com
├── payment_service.py          # Luhn & UPI Secured Digital Payment Gateway
├── security_service.py         # CIA Triad Security Enforcement & Audit
├── ai_chatbot.py               # AgriBot AI Voice & Text module
├── static/
│   ├── css/style.css           # Glassmorphic UI design system
│   ├── js/main.js             # Cart, XAI, Dosage calculator, Voice Chat scripts
│   ├── js/i18n.js             # Dynamic translation engine (English, Tamil, Hindi, Spanish, etc.)
│   ├── uploads/                # User leaf photos & product images
│   └── samples/                # Built-in demo leaf samples
├── templates/                  # HTML templates (base, index, login, register, account, dashboards, etc.)
├── requirements.txt            # Python dependencies
└── README.md                   # System documentation
```

---

## ⚡ Quick Start Guide

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Master Application Server
```bash
python app.py
```
Open **[https://plantasanitus.com](https://plantasanitus.com)** (or local dev environment `http://127.0.0.1:5000`).

---

## 👨‍💻 Developed By

**Rifanshiya J S**  
Final Year Computer Science & Engineering Student  
*Department of Computer Science and Engineering*
