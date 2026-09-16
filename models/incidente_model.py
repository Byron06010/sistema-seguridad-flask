from datetime import datetime

class IncidenteModel:
    @staticmethod
    def crear_incidente(usuario_id, nombre_usuario, titulo, categoria, prioridad, descripcion, ubicacion=""):
        return {
            "usuario_id": usuario_id,
            "nombre_usuario": nombre_usuario,
            "titulo": titulo,
            "categoria": categoria,  # ACCESO, ROBO, MANTENCION, EMERGENCIA, OTRO
            "prioridad": prioridad,  # BAJA, MEDIA, ALTA, CRITICA
            "descripcion": descripcion,
            "ubicacion": ubicacion,
            "estado": "ABIERTO",     # ABIERTO, EN_PROCESO, RESUELTO
            "fecha_registro": datetime.now()
        }