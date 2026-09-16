from datetime import datetime
from bson.objectid import ObjectId

class RondaModel:
    def __init__(self, db):
        self.collection = db['rondas']

    def buscar_activa(self, usuario_id):
        if not usuario_id:
            return None
        uid = ObjectId(usuario_id) if isinstance(usuario_id, str) and len(usuario_id) == 24 else usuario_id
        return self.collection.find_one({
            "usuario_id": uid,
            "estado": "EN_PROCESO"
        })

    def iniciar(self, usuario_id, sector, inicio_iso, inicio_fecha, inicio_hora):
        uid = ObjectId(usuario_id) if isinstance(usuario_id, str) and len(usuario_id) == 24 else usuario_id
        doc = {
            "usuario_id": uid,
            "sector": sector,
            "inicio_iso": inicio_iso,
            "inicio_fecha": inicio_fecha,
            "inicio_hora": inicio_hora,
            "fin_fecha": "",
            "fin_hora": "",
            "duracion": "",
            "estado": "EN_PROCESO",
            "created_at": datetime.utcnow()
        }
        res = self.collection.insert_one(doc)
        return str(res.inserted_id)

    def finalizar(self, ronda_id, fin_fecha, fin_hora, duracion):
        rid = ObjectId(ronda_id) if isinstance(ronda_id, str) and len(ronda_id) == 24 else ronda_id
        self.collection.update_one(
            {"_id": rid},
            {"$set": {
                "fin_fecha": fin_fecha,
                "fin_hora": fin_hora,
                "duracion": duracion,
                "estado": "FINALIZADA"
            }}
        )

    def obtener_finalizadas(self):
        cursor = self.collection.find({"estado": "FINALIZADA"}).sort("_id", -1)
        rondas = []
        for doc in cursor:
            rondas.append({
                "_id": str(doc.get("_id")),
                "usuario_nombre": "Guardia / Inspector",
                "sector": doc.get("sector", "Sin Sector"),
                "inicio_fecha": doc.get("inicio_fecha", ""),
                "inicio_hora": doc.get("inicio_hora", ""),
                "fin_fecha": doc.get("fin_fecha", ""),
                "fin_hora": doc.get("fin_hora", ""),
                "duracion": doc.get("duracion", "")
            })
        return rondas