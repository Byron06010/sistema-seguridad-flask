from datetime import datetime
from database.connection import get_db
from bson.objectid import ObjectId

class IncidenteService:

    def crear_incidente(self, usuario_id, titulo, categoria, prioridad, ubicacion, descripcion):
        db = get_db()
        
        # Validación de ObjectId por si viene un string no válido
        try:
            user_obj_id = ObjectId(usuario_id)
        except Exception:
            user_obj_id = usuario_id

        doc = {
            "usuario_id": user_obj_id,
            "titulo": str(titulo),
            "categoria": str(categoria),
            "prioridad": str(prioridad),
            "ubicacion": str(ubicacion),
            "descripcion": str(descripcion),
            "fecha_registro": datetime.now()
        }
        
        resultado = db.incidentes.insert_one(doc)
        print(f"[MONGO SUCCESS] Guardado en colección 'incidentes' con _id: {resultado.inserted_id}")
        
        return {"ok": True, "id": str(resultado.inserted_id)}