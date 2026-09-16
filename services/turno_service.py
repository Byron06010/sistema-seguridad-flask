from datetime import datetime
from database.connection import get_db
from bson.objectid import ObjectId

class TurnoService:
    def __init__(self):
        self.db = get_db()

    def registrar_marca(self, usuario_id, tipo_marca, observaciones=""):
        uid = ObjectId(usuario_id) if len(str(usuario_id)) == 24 else usuario_id
        ahora = datetime.now()

        estados = {
            "INICIO_TURNO": "EN_TURNO",
            "SALIDA_COLACION": "EN_COLACION",
            "RETORNO_COLACION": "EN_TURNO",
            "FIN_TURNO": "FUERA_DE_TURNO"
        }
        nuevo_estado = estados.get(tipo_marca, "FUERA_DE_TURNO")

        if tipo_marca == "INICIO_TURNO":
            # Crear un único documento para el turno que arranca
            nuevo_turno = {
                "usuario_id": uid,
                "inicio": ahora,
                "salida_colacion": None,
                "retorno_colacion": None,
                "fin": None,
                "estado": "EN_TURNO",
                "observaciones_inicio": observaciones
            }
            resultado = self.db.marcas.insert_one(nuevo_turno)
            turno_id = resultado.inserted_id
            
            # Actualizar estado del usuario
            self.db.usuarios.update_one({"_id": uid}, {"$set": {"estado_turno": "EN_TURNO", "turno_activo_id": turno_id}})
            return {"ok": True, "mensaje": "Turno iniciado con éxito", "nuevo_estado": "EN_TURNO"}

        else:
            # Buscar el turno activo actual del usuario (el último que no tenga 'fin')
            turno_activo = self.db.marcas.find_one(
                {"usuario_id": uid, "fin": None},
                sort=[("inicio", -1)]
            )

            if not turno_activo:
                return {"ok": False, "mensaje": "No hay un turno activo para actualizar."}

            turno_id = turno_activo["_id"]
            update_data = {"estado": nuevo_estado}

            # Mapear el tipo de marca al campo correspondiente en el documento único
            if tipo_marca == "SALIDA_COLACION":
                update_data["salida_colacion"] = ahora
            elif tipo_marca == "RETORNO_COLACION":
                update_data["retorno_colacion"] = ahora
            elif tipo_marca == "FIN_TURNO":
                update_data["fin"] = ahora
                # Limpiar la referencia de turno activo en el usuario al cerrar
                self.db.usuarios.update_one({"_id": uid}, {"$unset": {"turno_activo_id": ""}})

            # Actualizar el documento único en MongoDB
            self.db.marcas.update_one(
                {"_id": turno_id},
                {"$set": update_data}
            )

            # Actualizar estado del usuario
            self.db.usuarios.update_one({"_id": uid}, {"$set": {"estado_turno": nuevo_estado}})

            return {"ok": True, "mensaje": f"Marcación '{tipo_marca}' registrada en el turno", "nuevo_estado": nuevo_estado}

    def obtener_ultimo_inicio(self, usuario_id):
        uid = ObjectId(usuario_id) if len(str(usuario_id)) == 24 else usuario_id
        turno = self.db.marcas.find_one(
            {"usuario_id": uid, "fin": None},
            sort=[("inicio", -1)]
        )
        if turno and "inicio" in turno and isinstance(turno["inicio"], datetime):
            return turno["inicio"].isoformat()
        return None