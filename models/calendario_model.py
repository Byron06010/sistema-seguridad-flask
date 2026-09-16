from bson.objectid import ObjectId

class CalendarioModel:
    def __init__(self, db):
        self.db = db
        self.collection = db.calendario_turnos  # Revisa si tu colección se llama así o similar

    def obtener_por_usuario(self, usuario_id):
        try:
            uid = ObjectId(usuario_id)
        except Exception:
            uid = usuario_id
        
        # Retorna todos los turnos del usuario como lista
        return list(self.collection.find({"usuario_id": uid}))

    def guardar_o_actualizar(self, usuario_id, fecha, tipo_turno, puesto, observaciones):
        try:
            uid = ObjectId(usuario_id)
        except Exception:
            uid = usuario_id

        self.collection.update_one(
            {"usuario_id": uid, "fecha": fecha},
            {
                "$set": {
                    "tipo_turno": tipo_turno,
                    "puesto": puesto,
                    "observaciones": observaciones
                }
            },
            upsert=True
        )

    def eliminar(self, usuario_id, fecha):
        try:
            uid = ObjectId(usuario_id)
        except Exception:
            uid = usuario_id

        # Borra el turno de MongoDB basándose en el usuario y la fecha exacta
        self.collection.delete_one({
            "usuario_id": uid,
            "fecha": fecha
        })