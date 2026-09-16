from database.connection import get_db
from models.usuario_model import UsuarioModel
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

class AuthService:
    def __init__(self):
        self.db = get_db()

    def registrar_usuario(self, rut, nombre, email, password, rol="GUARDIA"):
        if self.db.usuarios.find_one({"email": email}):
            return {"ok": False, "mensaje": "El correo ya está registrado."}
        
        pwd_hash = generate_password_hash(password)
        nuevo_usuario = UsuarioModel.crear_usuario(rut, nombre, email, pwd_hash, rol)
        self.db.usuarios.insert_one(nuevo_usuario)
        return {"ok": True, "mensaje": "Usuario creado exitosamente."}

    def autenticar(self, email, password):
        user = self.db.usuarios.find_one({"email": email})
        if user and check_password_hash(user["password"], password):
            return {"ok": True, "usuario": user}
        return {"ok": False, "mensaje": "Credenciales inválidas."}

    def obtener_por_id(self, user_id):
        return self.db.usuarios.find_one({"_id": ObjectId(user_id)})