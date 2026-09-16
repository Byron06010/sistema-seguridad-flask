from database.connection import get_db
from datetime import datetime

class AnalyticsService:
    def __init__(self):
        self.db = get_db()

    def exportar_marcas_powerbi(self):
        marcas = list(self.db.marcas.find({}, {"_id": 0}))
        for m in marcas:
            if isinstance(m.get("fecha_hora"), datetime):
                m["fecha_hora"] = m["fecha_hora"].strftime("%Y-%m-%d %H:%M:%S")
        return marcas

    def exportar_incidentes_powerbi(self):
        incidentes = list(self.db.incidentes.find({}, {"_id": 0}))
        for i in incidentes:
            if isinstance(i.get("fecha_registro"), datetime):
                i["fecha_registro"] = i["fecha_registro"].strftime("%Y-%m-%d %H:%M:%S")
        return incidentes