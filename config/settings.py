import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave_secreta_super_segura')
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://127.0.0.1:27017/')
    MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME', 'sistema_seguridad')
    
    # Atributos requeridos por run.py
    PORT = int(os.environ.get('PORT', 5000))
    DEBUG = os.environ.get('DEBUG', 'True').lower() in ['true', '1', 't']