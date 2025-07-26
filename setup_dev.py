#!/usr/bin/env python3
"""
Development Setup Script for Kompyuter Texnologiya Sayti

This script automates the initial setup for developers.
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a shell command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def create_env_file():
    """Create .env file from template if it doesn't exist."""
    env_file = Path('.env')
    env_example = Path('env.example')
    
    if not env_file.exists() and env_example.exists():
        print("📝 Creating .env file from template...")
        try:
            with open(env_example, 'r') as source:
                content = source.read()
            
            # Generate a new secret key
            import secrets
            new_secret_key = secrets.token_urlsafe(50)
            content = content.replace('your-secret-key-here', new_secret_key)
            
            with open(env_file, 'w') as target:
                target.write(content)
            
            print("✅ .env file created successfully")
            print("⚠️  Please update the .env file with your actual configuration")
            return True
        except Exception as e:
            print(f"❌ Failed to create .env file: {e}")
            return False
    elif env_file.exists():
        print("ℹ️  .env file already exists")
        return True
    else:
        print("⚠️  env.example not found, please create .env file manually")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ is required")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def setup_virtual_environment():
    """Set up virtual environment."""
    venv_path = Path('venv')
    if venv_path.exists():
        print("ℹ️  Virtual environment already exists")
        return True
    
    return run_command('python -m venv venv', 'Creating virtual environment')

def install_dependencies():
    """Install Python dependencies."""
    # Determine the correct pip command based on OS
    if os.name == 'nt':  # Windows
        pip_cmd = 'venv\\Scripts\\pip'
    else:  # Unix/Linux/Mac
        pip_cmd = 'venv/bin/pip'
    
    return run_command(f'{pip_cmd} install -r requirements.txt', 'Installing dependencies')

def run_migrations():
    """Run Django migrations."""
    # Determine the correct python command based on OS
    if os.name == 'nt':  # Windows
        python_cmd = 'venv\\Scripts\\python'
    else:  # Unix/Linux/Mac
        python_cmd = 'venv/bin/python'
    
    success = True
    success &= run_command(f'{python_cmd} manage.py makemigrations', 'Creating migrations')
    success &= run_command(f'{python_cmd} manage.py migrate', 'Running migrations')
    return success

def create_superuser():
    """Create a superuser account."""
    print("👤 Would you like to create a superuser account? (y/n): ", end='')
    response = input().lower().strip()
    
    if response in ['y', 'yes']:
        # Determine the correct python command based on OS
        if os.name == 'nt':  # Windows
            python_cmd = 'venv\\Scripts\\python'
        else:  # Unix/Linux/Mac
            python_cmd = 'venv/bin/python'
        
        return run_command(f'{python_cmd} manage.py createsuperuser', 'Creating superuser')
    
    print("ℹ️  Skipping superuser creation")
    return True

def main():
    """Main setup function."""
    print("🚀 Setting up Kompyuter Texnologiya Sayti development environment...")
    print("=" * 60)
    
    # Check prerequisites
    if not check_python_version():
        sys.exit(1)
    
    # Setup steps
    steps = [
        ("Creating .env file", create_env_file),
        ("Setting up virtual environment", setup_virtual_environment),
        ("Installing dependencies", install_dependencies),
        ("Running migrations", run_migrations),
        ("Creating superuser", create_superuser),
    ]
    
    success_count = 0
    for step_name, step_func in steps:
        print(f"\n📋 Step {success_count + 1}: {step_name}")
        if step_func():
            success_count += 1
        else:
            print(f"❌ Setup failed at step: {step_name}")
            break
    
    print("\n" + "=" * 60)
    if success_count == len(steps):
        print("🎉 Setup completed successfully!")
        print("\n📋 Next steps:")
        print("1. Update .env file with your actual configuration")
        print("2. Activate virtual environment:")
        if os.name == 'nt':  # Windows
            print("   venv\\Scripts\\activate")
        else:  # Unix/Linux/Mac
            print("   source venv/bin/activate")
        print("3. Run the development server:")
        print("   python manage.py runserver")
        print("4. Open http://127.0.0.1:8000 in your browser")
    else:
        print(f"⚠️  Setup completed with {success_count}/{len(steps)} steps successful")
        print("Please check the errors above and complete the setup manually")

if __name__ == "__main__":
    main() 