# 🚀 Deployment Guide

This guide covers deploying the Kompyuter Texnologiya Sayti to various platforms.

## 📋 Prerequisites

- Python 3.11+
- Git
- PostgreSQL database
- Environment variables configured

## 🔧 Environment Setup

1. **Copy environment template**
   ```bash
   cp env.example .env
   ```

2. **Configure environment variables**
   Edit `.env` file with your actual values:
   ```env
   SECRET_KEY=your-actual-secret-key
   DEBUG=False
   DATABASE_URL=your-postgresql-connection-string
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   ```

## 🌐 Vercel Deployment

### 1. Install Vercel CLI
```bash
npm install -g vercel
```

### 2. Deploy
```bash
vercel
```

### 3. Configure Environment Variables
In Vercel dashboard:
- Go to your project settings
- Add environment variables from your `.env` file

### 4. Database Setup
- Use Vercel Postgres or external PostgreSQL service
- Update `DATABASE_URL` in environment variables

## 🚂 Railway Deployment

### 1. Connect Repository
- Go to [Railway](https://railway.app)
- Connect your GitHub repository

### 2. Configure Environment
- Add environment variables in Railway dashboard
- Set up PostgreSQL database

### 3. Deploy
Railway will automatically deploy on push to main branch.

## ☁️ Render Deployment

### 1. Create New Web Service
- Go to [Render](https://render.com)
- Connect your GitHub repository
- Choose "Web Service"

### 2. Configure Build Settings
```bash
Build Command: pip install -r requirements.txt
Start Command: gunicorn config.wsgi:application
```

### 3. Environment Variables
Add all required environment variables in Render dashboard.

### 4. Database
- Create PostgreSQL database in Render
- Use the provided connection string

## 🐳 Docker Deployment

### 1. Create Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### 2. Build and Run
```bash
docker build -t kompyuter-texnologiya .
docker run -p 8000:8000 kompyuter-texnologiya
```

## 🔒 Production Security Checklist

- [ ] `DEBUG=False` in production
- [ ] Strong `SECRET_KEY` configured
- [ ] HTTPS enabled
- [ ] Database credentials secured
- [ ] Static files properly served
- [ ] Media files configured
- [ ] Logging enabled
- [ ] Error monitoring set up

## 📊 Monitoring and Logs

### Application Logs
- Check Django logs in `/logs/django.log`
- Monitor application errors
- Set up error tracking (Sentry recommended)

### Database Monitoring
- Monitor database connections
- Check query performance
- Set up database backups

## 🔄 CI/CD Pipeline

### GitHub Actions Example
```yaml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Deploy to Railway
      run: |
        # Add your deployment commands here
```

## 🆘 Troubleshooting

### Common Issues

1. **Static Files Not Loading**
   - Run `python manage.py collectstatic`
   - Check `STATIC_ROOT` configuration

2. **Database Connection Errors**
   - Verify `DATABASE_URL` format
   - Check database credentials
   - Ensure database is accessible

3. **CSRF Token Errors**
   - Add domain to `CSRF_TRUSTED_ORIGINS`
   - Check HTTPS configuration

4. **Media Files Not Uploading**
   - Verify `MEDIA_ROOT` permissions
   - Check file upload settings

### Support
For deployment issues, check:
- Platform-specific documentation
- Django deployment checklist
- Application logs
- Database logs

## 📈 Performance Optimization

1. **Enable Caching**
   - Configure Redis or Memcached
   - Use Django cache framework

2. **Database Optimization**
   - Add database indexes
   - Optimize queries
   - Use database connection pooling

3. **Static Files**
   - Use CDN for static files
   - Enable compression
   - Optimize images

4. **Application**
   - Enable Django debug toolbar in development
   - Profile application performance
   - Optimize database queries 