from datetime import datetime
from database.connection import get_db
from bson.objectid import ObjectId

class TurnoService:
    def __init__(self):
        self.db = get_db()

    def registrar_marca(self, usuario_id, tipo_marca, observaciones=""):
        marca = {
            "usuario_id": ObjectId(usuario_id),
            "tipo_marca": tipo_marca,  # INICIO_TURNO, SALIDA_COLACION, RETORNO_COLACION, FIN_TURNO
            "fecha_hora": datetime.now(),
            "observaciones": observaciones
        }
        self.db.marcas.insert_one(marca)

        # Mapeo de estados del usuario
        estados = {
            "INICIO_TURNO": "EN_TURNO",
            "SALIDA_COLACION": "EN_COLACION",
            "RETORNO_COLACION": "EN_TURNO",
            "FIN_TURNO": "FUERA_DE_TURNO"
        }
        nuevo_estado = estados.get(tipo_marca, "FUERA_DE_TURNO")
        
        self.db.usuarios.update_one(
            {"_id": ObjectId(usuario_id)},
            {"$set": {"estado_turno": nuevo_estado}}
        )

        return {"ok": True, "mensaje": f"Marcación '{tipo_marca}' registrada con éxito", "nuevo_estado": nuevo_estado}

    def obtener_ultimo_inicio(self, usuario_id):
        marca = self.db.marcas.find_one(
            {"usuario_id": ObjectId(usuario_id), "tipo_marca": "INICIO_TURNO"},
            sort=[("fecha_hora", -1)]
        )
        if marca and "fecha_hora" in marca:
            return marca["fecha_hora"].isoformat()
        return None