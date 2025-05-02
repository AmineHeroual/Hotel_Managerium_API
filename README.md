# 🏨 Hotel Management System

This is a **Django-based** project for managing hotel reservations, room bookings, maintenance requests, invoicing, and client reviews.

---

### 📦 Project Structure

- `users/` — User management (authentication, clients, technicians).
- `rooms/` — Room management.
- `reservations/` — Reservation and booking system.
- `invoices/` — Invoice generation and tracking.
- `maintenance/` — Maintenance requests and issue tracking.
- `reviews/` — Customer reviews and ratings.
- `admin.py` — Admin site customization for easy management.

---

### 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/hotel-management-system.git
cd hotel-management-system
```
## 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```
## 3. Install dependencies

```bash
pip install -r requirements.txt
```
## 4. Set up the database

```bash
python manage.py makemigrations
python manage.py migrate
```

## 5. Create a superuser

```bash
python manage.py createsuperuser
```

## 6. Run the development server

```bash
python manage.py runserver
```
