from datetime import datetime

class UsuarioModel:
    @staticmethod
    def crear_usuario(rut, nombre, email, password_hash, rol="GUARDIA"):
        return {
            "rut": rut,
            "nombre": nombre,
            "email": email,
            "password": password_hash,
            "rol": rol,  # GUARDIA, SUPERVISOR, ADMINISTRADOR
            "estado_turno": "FUERA_DE_TURNO",  # FUERA_DE_TURNO, EN_TURNO, EN_COLACION
            "inicio_turno_at": None,
            "inicio_colacion_at": None,
            "fecha_creacion": datetime.now()
        }