# 🖥️ Kompyuter Texnologiya Sayti (Computer Technology Website)

A comprehensive Django-based web application for computer technology education and e-commerce, featuring computer parts comparison, educational videos, and online shopping functionality.

## 🌟 Features

### 🛒 E-commerce Module
- **Product Catalog**: Browse computer parts and accessories
- **Shopping Cart**: Add/remove items with quantity management
- **Product Categories**: Organized by product types
- **Product Details**: Detailed information with images and pricing

### 🎓 Educational Content
- **Video Tutorials**: Educational videos organized by categories
- **Number System Calculator**: Interactive tool for different number systems
- **Computer Comparison**: Compare different computer specifications
- **Laboratory Sections**: Educational content for computer technology

### 👤 User Management
- **User Registration & Authentication**: Secure login/logout system
- **User Profiles**: Personalized user experience
- **Shopping History**: Track user purchases

### 🔧 Technical Features
- **Responsive Design**: Mobile-friendly interface
- **Database Management**: PostgreSQL backend
- **File Upload**: Image handling for products
- **Admin Panel**: Comprehensive Django admin interface

## 🚀 Technology Stack

- **Backend**: Django 5.1.3
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Vercel, Railway, Render
- **Image Processing**: Pillow
- **Environment Management**: python-dotenv

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL
- pip or pipenv

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Matnazar-Matnazarov/Kompyuter_texnologiya_sayti.git
   cd Kompyuter_texnologiya_sayti
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   DATABASE_URL=your-database-url
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## 🗂️ Project Structure

```
Kompyuter_texnologiya_sayti/
├── app1/                    # Main application
│   ├── models.py           # Database models
│   ├── views.py            # View logic
│   ├── urls.py             # URL routing
│   ├── forms.py            # Form definitions
│   └── admin.py            # Admin interface
├── users/                   # User management app
├── config/                  # Django settings
├── templates/               # HTML templates
├── static/                  # Static files (CSS, JS, images)
├── media/                   # User-uploaded files
└── requirements.txt         # Python dependencies
```

## 🗄️ Database Models

### Core Models
- **Tovarslar_s**: Product catalog with categories
- **backet_s**: Shopping cart functionality
- **Video_turi & Page2**: Video content management
- **Protsessor, Operativka, Ram_xotira**: Computer specifications
- **Sanoq_sistema_model**: Number system calculations

## 🌐 Deployment

### Vercel Deployment
The project includes `vercel.json` configuration for Vercel deployment.

### Railway/Render Deployment
Configured for PostgreSQL databases on Railway and Render platforms.

## 🔧 Configuration

### Environment Variables
- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode (False for production)
- `DATABASE_URL`: PostgreSQL connection string
- `ALLOWED_HOSTS`: Allowed host domains

### Static Files
Static files are configured for production deployment with proper serving.

## 📱 API Endpoints

### Main Routes
- `/`: Home page
- `/lobaratoriya1/`: Laboratory section 1
- `/lobaratoriya2/`: Laboratory section 2 (videos)
- `/addtovar/`: Add products
- `/sanoq/sistema/`: Number system calculator
- `/kompyuter/solishtirish/`: Computer comparison tool

### User Management
- `/users/login/`: User login
- `/users/register/`: User registration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Matnazar** - Computer Technology Website Developer

## 🙏 Acknowledgments

- Django community for the excellent framework
- PostgreSQL for reliable database management
- All contributors and users of this project

## 📞 Support

For support and questions, please contact the development team or create an issue in the repository.

---

**Note**: This project is designed for educational purposes in computer technology and provides both learning resources and e-commerce functionality.
