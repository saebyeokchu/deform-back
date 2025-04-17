# 🛠️ deform-back — Littleblock Backend (Django)

**deform-back** is the backend server for [Littleblock](https://littleblock.co.kr), a creative platform that allows users to design pixel-style LEGO art.  
This project powers the core business logic, API, and admin features of the Littleblock ecosystem.

Built with **Python Django**, this backend connects to the **Next.js frontend**, handles content creation APIs, and integrates directly with a **WooCommerce-powered WordPress shopping mall**.

---

## 🔧 Features

- ⚙️ Django-based REST API backend for the Littleblock editor
- 🔐 `.env`-based secure settings using `python-dotenv` & `python-decouple`
- 🛒 WooCommerce REST API integration for syncing products/orders with WordPress
- 📦 Modular Django app structure for future extensibility
- 🧾 Handles design storage, user content, and communication with frontend

---

## ⚙️ Tech Stack

| Layer             | Tech                               |
|------------------|------------------------------------|
| Backend Framework | Django 4.x                         |
| Environment Mgmt  | `python-dotenv`, `python-decouple` |
| API Integration   | WooCommerce REST API (WordPress)   |
| Auth & Security   | Django Auth + dotenv secrets       |
| Database          | PostgreSQL / SQLite (local)        |
| Deployment        | AWS / Docker / Gunicorn (optional) |

---

## 📁 Project Structure

```bash
deform-back/
├── core/                   # Django app with main business logic
├── deform_back/            # Django settings and root config
├── .env                    # Environment-specific variables (never push to Git!)
├── requirements.txt        # Python package dependencies
├── manage.py               # Django entry point
└── README.md
```

---

## 🔐 Environment Setup

Before running the project, create a `.env` file in the root directory:

```env
DEBUG=True
SECRET_KEY=your_django_secret
ALLOWED_HOSTS=localhost,127.0.0.1

# WooCommerce Credentials
WC_CONSUMER_KEY=your_key
WC_CONSUMER_SECRET=your_secret
WC_STORE_URL=https://shop.littleblock.co.kr

# Database (optional)
DATABASE_URL=sqlite:///db.sqlite3
```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/saebyeokchu/deform-back.git
cd deform-back
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations and Start Server

```bash
python manage.py migrate
python manage.py runserver
```

---

## 🔗 WooCommerce Integration

The backend communicates with the WordPress + WooCommerce store at:

```
https://shop.littleblock.co.kr
```

You can:
- Sync product data
- Manage orders from the frontend
- Update inventory or item states via Django views or cron jobs

WooCommerce API usage is secured via consumer keys stored in `.env`.

---

## ✨ Example API Endpoint

```http
GET /api/designs/
POST /api/designs/
```

> Handles block-based user designs from the frontend editor (deform)

---

## 📦 Future Enhancements

- [ ] OAuth2 user authentication for persistent sessions
- [ ] Admin panel customization for product sync
- [ ] GraphQL interface for faster queries
- [ ] Dockerfile and production deployment automation

---

## 🙌 Contributing

Feel free to fork and contribute if you're interested in:

- Django backend development
- WooCommerce or WordPress API
- Creative tools for makers & designers

---

## 📄 License

MIT License

---

Made with 💡 by [@saebyeokchu](https://github.com/saebyeokchu)  
Powering the creative backend of **[Littleblock](https://littleblock.co.kr)** 🧱
