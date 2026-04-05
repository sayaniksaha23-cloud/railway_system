# Railway Ticket Booking System (CLI)

## 📌 Overview
This is a modular, interactive command-line Railway Ticket Booking System built in Python.

The system allows users to:
- Select routes
- Choose train types and classes
- Enter passenger details
- Calculate fares using a 6-step pricing model
- Apply promo codes
- View final booking summary

---

## 🧱 Project Structure

railway_system/
│
├── core/
│   ├── main.py
│   ├── booking.py
│   ├── passenger.py
│   ├── fare.py
│   ├── promo.py
│   ├── routes.py
│   ├── constants.py
│   ├── utils.py
│   ├── __init__.py
│
├── pyproject.toml  
├── README.md
---

## 🚀 How to Run

### 1. Create virtual environment
```bash
python -m venv venv
```

### 2. Activate environment
```bash
venv\Scripts\activate
```

### 3. Install in development mode
```bash
pip install -e .
```

### 4. Run the CLI tool
```bash
railway
```
---

## 🧠 Features

- Fully interactive CLI
- Modular architecture (separation of concerns)
- 6-step fare calculation logic
- Senior citizen discount
- Baggage fee calculation
- Promo code system
- Crash-proof input handling

---

## 🎯 Promo Codes

| Code       | Discount |
|------------|----------|
| ADG20      | 20% off  |
| WINTER500  | ₹500 off |

---

## ⚠️ Notes

- All inputs are validated to prevent crashes
- Only one promo code can be applied per booking
- Total fare never drops below ₹0
