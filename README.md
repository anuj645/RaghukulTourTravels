# RaghukulTourTravels
📌 About The Project

Raghukul Tours & Travel is a complete tour and travel booking system where users can browse tour packages, register/login, make bookings, and manage them from a personal dashboard. Admins can manage packages, bookings, and contact messages through a built-in Django admin panel.

This project was built as a full-stack Django learning project covering authentication, CRUD operations, database design, and deployment-ready practices.


✨ Features


🔐 Custom Authentication — Email-based login & registration (no username)
🗺️ Tour Package Management — Create, Read, Update, Delete (CRUD) with image upload
📅 Booking System — Book tours with travel date, group size, and auto price calculation
👤 User Dashboard — View and manage all personal bookings
📬 Contact Form — Visitors can send messages, stored in admin panel
📧 Email Notifications — Booking confirmation emails on every booking
🛠️ Admin Panel — Full control over users, tours, bookings, and messages
💰 Discount System — Original vs discounted price with percentage badge
🔍 Filter by Category — Browse tours by type (Hill Station, Beach, Religious, etc.)
🔒 Soft Delete — Tours are deactivated, not permanently deleted



🛠️ Tech Stack

LayerTechnologyBackendDjango 6.0, Python 3.12DatabaseMySQL 8.0FrontendBootstrap 5.3, Font Awesome 6AuthCustom User Model (AbstractBaseUser)ImagesPillowEnvironmentpython-dotenv


📁 Project Structure

RaghukulToursTravel/
├── accounts/           # Custom user model, login, register
├── bookings/           # Booking model, views, forms
├── core/               # Homepage, dashboard, contact
├── tours/              # Tour packages CRUD
├── raghukul_tours/     # Project settings & URLs
├── templates/          # All HTML templates
│   ├── base.html
│   ├── accounts/
│   ├── bookings/
│   ├── core/
│   └── tours/
├── static/             # CSS, JS, images
├── .env                # Environment variables (not committed)
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md


⚙️ Setup Instructions

Prerequisites

Make sure you have these installed:


Python 3.10+
MySQL 8.0+
Git


1. Clone the Repository

bashgit clone https://github.com/yourusername/RaghukulToursTravel.git
cd RaghukulToursTravel

2. Create & Activate Virtual Environment

bashpython -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

3. Install Dependencies

bashpip install -r requirements.txt

4. Create MySQL Database

sqlCREATE DATABASE raghukul_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

5. Setup Environment Variables

Create a .env file in the root folder:

envSECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=raghukul_db
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=3306

6. Run Migrations

bashpython manage.py makemigrations
python manage.py migrate

7. Create Superuser (Admin)

bashpython manage.py createsuperuser

8. Run the Server

bashpython manage.py runserver

Visit http://127.0.0.1:8000 in your browser.


🔗 Key URLs

URLDescription/Homepage with featured tours/tours/All tour packages/tours/<slug>/Tour detail & booking button/bookings/book/<slug>/Book a tour/dashboard/User booking dashboard/contact/Contact form/accounts/register/Register new account/accounts/login/Login/admin/Django admin panel


🗃️ Database Models

CustomUser


Email-based login (no username)
Fields: email, first_name, last_name, phone


TourPackage


Fields: title, slug, category, description, highlights, itinerary
Pricing: price_per_person, discounted_price
Meta: duration_days, max_group_size, difficulty, destination, cover_image


Booking


Links User → TourPackage
Fields: travel_date, num_persons, total_price, status, special_requests
Status choices: Pending, Confirmed, Cancelled, Completed


ContactMessage


Fields: name, email, phone, subject, message, is_read



🎯 Key Concepts Demonstrated


Custom User Model with AbstractBaseUser and BaseUserManager
Django ORM — ForeignKey, related_name, on_delete strategies
Class-based vs Function-based views
ModelForms with custom validation (clean_<fieldname>)
Login required decorator (@login_required)
Staff member required decorator (@staff_member_required)
Soft delete pattern (is_active flag instead of DB deletion)
Environment variables with python-dotenv
Django messages framework for flash notifications
Media file handling with Pillow
Django Admin customization with list_editable, prepopulated_fields
