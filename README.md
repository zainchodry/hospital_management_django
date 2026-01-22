# Hospital Management System

A comprehensive Django-based hospital management application designed to streamline healthcare operations, including patient records management, appointment scheduling, medical history tracking, and user notifications.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Models](#database-models)
- [User Roles](#user-roles)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### Core Functionality

- **User Management**: Role-based user system with multiple user types (Admin, Doctor, Nurse, Receptionist, Patient)
- **Patient Records**: Comprehensive medical record management including diagnoses, prescriptions, and medical reports
- **Appointment Scheduling**: Manage patient appointments with doctors, including status tracking (Pending, Approved, Rejected)
- **Medical History**: Maintain detailed patient medical history with notes and file attachments
- **Notifications System**: Real-time user notifications for appointment updates and system events
- **User Profiles**: Extended user profiles with personal information, medical details, and contact information

### User Features by Role

- **Patients**: Book appointments, view medical records, receive notifications
- **Doctors**: Manage appointments, create/update medical records, view patient history
- **Nurses**: Support patient management and record assistance
- **Receptionists**: Schedule appointments, manage patient inquiries
- **Admins**: Full system administration and user management

## 🛠️ Tech Stack

- **Backend Framework**: Django 5.2.10
- **Database**: SQLite (default, configurable)
- **Python Version**: 3.x
- **Authentication**: Django's built-in authentication system with custom user model
- **ORM**: Django ORM
- **Web Server**: Django development server / WSGI compatible servers

## 📁 Project Structure

```
hospital_management_django/
├── manage.py                      # Django management script
├── README.md                      # This file
├── .gitignore                     # Git ignore file
│
├── hospital_management/           # Project configuration
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Main URL configuration
│   ├── wsgi.py                   # WSGI application
│   ├── asgi.py                   # ASGI application
│   └── __init__.py
│
├── accounts/                      # User authentication & profiles
│   ├── models.py                 # User and Profile models
│   ├── views.py                  # Authentication views
│   ├── forms.py                  # User forms
│   ├── urls.py                   # App URLs
│   ├── admin.py                  # Admin interface
│   ├── signals.py                # Django signals
│   ├── tests.py                  # Unit tests
│   ├── apps.py                   # App configuration
│   └── migrations/               # Database migrations
│
├── records/                       # Medical records management
│   ├── models.py                 # MedicalRecord model
│   ├── views.py                  # Medical record views
│   ├── forms.py                  # Medical record forms
│   ├── urls.py                   # App URLs
│   ├── admin.py                  # Admin interface
│   ├── tests.py                  # Unit tests
│   ├── apps.py                   # App configuration
│   └── migrations/               # Database migrations
│
├── appointments/                  # Appointment management
│   ├── models.py                 # Appointment model
│   ├── views.py                  # Appointment views
│   ├── forms.py                  # Appointment forms
│   ├── urls.py                   # App URLs
│   ├── admin.py                  # Admin interface
│   ├── tests.py                  # Unit tests
│   ├── apps.py                   # App configuration
│   └── migrations/               # Database migrations
│
├── notifications/                 # Notification system
│   ├── models.py                 # Notification model
│   ├── views.py                  # Notification views
│   ├── urls.py                   # App URLs
│   ├── signals.py                # Signal handlers
│   ├── admin.py                  # Admin interface
│   ├── tests.py                  # Unit tests
│   ├── apps.py                   # App configuration
│   └── migrations/               # Database migrations
│
└── venv/                         # Python virtual environment
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd hospital_management_django
```

### Step 2: Create Virtual Environment

```bash
# On Linux/Mac
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install django==5.2.10
pip install pillow  # For image handling
```

Or use a requirements file (create one if needed):

```bash
pip install -r requirements.txt
```

### Step 4: Database Setup

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### Step 5: Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

## ⚙️ Configuration

### Django Settings

Key configurations in [hospital_management/settings.py](hospital_management/settings.py):

```python
# Debug mode (set to False in production)
DEBUG = True

# Allowed hosts (add your domain in production)
ALLOWED_HOSTS = []

# Installed apps include:
# - Django core apps
# - accounts (user management)
# - records (medical records)
# - appointments (appointment scheduling)
# - notifications (notification system)
```

### Environment Variables

For production, consider using environment variables:

```bash
export SECRET_KEY='your-secret-key'
export DEBUG=False
export ALLOWED_HOSTS='yourdomain.com'
```

### Static Files

```bash
python manage.py collectstatic
```

### Media Files

Media files (patient images, reports) are stored in:

- `media/patients/` - Patient images
- `media/reports/` - Medical reports

## 💻 Usage

### Running the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

### Admin Interface

Access the Django admin panel at: `http://127.0.0.1:8000/admin/`

Login with your superuser credentials to:

- Manage users and roles
- View and edit medical records
- Monitor appointments
- Manage notifications

## 🔌 API Endpoints

### Accounts App

- User registration and authentication
- Profile management
- Role-based access control

### Records App

- Create, read, update, delete medical records
- Upload medical reports
- View patient medical history

### Appointments App

- Create appointments
- View appointment status
- Update appointment status (approve/reject)
- Schedule management

### Notifications App

- Receive system notifications
- Mark notifications as read
- Notification history

## 📊 Database Models

### User Model

Extended Django User model with role-based access:

- Roles: Admin, Doctor, Nurse, Receptionist, Patient

### Profile Model

User profile with additional information:

- Personal details (age, phone, address)
- Medical information (blood group)
- Hospital assignment
- Profile image

### MedicalRecord Model

Patient medical records:

- Patient reference
- Doctor reference
- Diagnosis and prescription
- Medical notes
- Report file attachment

### Appointment Model

Appointment scheduling:

- Patient and Doctor assignment
- Date and time scheduling
- Appointment reason
- Status tracking (Pending, Approved, Rejected)

### Notification Model

User notifications:

- User reference
- Message content
- Read status
- Creation timestamp

## 👥 User Roles

| Role             | Permissions                                                        |
| ---------------- | ------------------------------------------------------------------ |
| **Admin**        | Full system access, user management, all operations                |
| **Doctor**       | Create/update medical records, manage patient appointments         |
| **Nurse**        | Support patient management, assist with records                    |
| **Receptionist** | Schedule appointments, manage patient inquiries                    |
| **Patient**      | Book appointments, view own medical records, receive notifications |

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

Run tests for a specific app:

```bash
python manage.py test accounts
python manage.py test records
python manage.py test appointments
python manage.py test notifications
```

## 🔒 Security Considerations

- Change `SECRET_KEY` in production
- Set `DEBUG = False` in production
- Use environment variables for sensitive information
- Implement HTTPS in production
- Use secure cookies and CSRF protection
- Regularly update Django and dependencies
- Implement proper authentication and authorization
- Validate all user inputs

## 🚀 Deployment

For production deployment:

1. Set `DEBUG = False`
2. Update `ALLOWED_HOSTS`
3. Use a production database (PostgreSQL recommended)
4. Configure static file serving
5. Use a production WSGI server (Gunicorn, uWSGI)
6. Set up proper logging and monitoring
7. Configure security headers
8. Use environment variables for sensitive data

Example with Gunicorn:

```bash
pip install gunicorn
gunicorn hospital_management.wsgi:application --bind 0.0.0.0:8000
```

## 📝 Development Workflow

1. Create a feature branch
2. Make your changes
3. Run tests to ensure nothing is broken
4. Create migrations if model changes are made
5. Submit a pull request for review

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Database Errors

```bash
# Reset migrations
python manage.py migrate --zero [app-name]
python manage.py migrate
```

### Static Files Issues

```bash
# Collect static files
python manage.py collectstatic --clear --noinput
```

### Import Errors

```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## 📞 Support

For issues and questions, please:

1. Check existing issues in the repository
2. Create a new issue with detailed description
3. Include error logs and steps to reproduce

## 🎯 Future Enhancements

- [ ] Real-time notifications using WebSockets
- [ ] Advanced medical record analytics
- [ ] Prescription management system
- [ ] Billing and insurance integration
- [ ] Video consultation features
- [ ] Mobile application
- [ ] HL7/FHIR compliance
- [ ] Advanced reporting and analytics dashboard
- [ ] Integration with external healthcare systems
- [ ] Two-factor authentication

---

**Last Updated**: January 2026

**Django Version**: 5.2.10

**Python Version**: 3.8+
