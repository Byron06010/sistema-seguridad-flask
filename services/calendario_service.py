from database.connection import get_db
from models.calendario_model import CalendarioModel
from datetime import datetime, date

class CalendarioService:
    def __init__(self):
        self.db = get_db()
        self.calendario_model = CalendarioModel(self.db)

    def obtener_turnos(self, usuario_id):
        if not usuario_id:
            return []
        
        turnos_raw = self.calendario_model.obtener_por_usuario(usuario_id)
        turnos_procesados = []
        
        for t in turnos_raw:
            turno_limpio = {}
            for k, v in t.items():
                # Convertir ObjectIds a string
                if k == '_id' or k == 'usuario_id':
                    turno_limpio[k] = str(v)
                # Convertir fechas de datetime o date a string ISO (ej: "2026-06-06")
                elif isinstance(v, (datetime, date)):
                    turno_limpio[k] = v.isoformat()
                else:
                    turno_limpio[k] = v
                    
            turnos_procesados.append(turno_limpio)
            
        return turnos_procesados

    def programar_turno(self, usuario_id, data):
        if not usuario_id:
            raise ValueError("Usuario no autenticado")
        
        fecha = data.get('fecha') # Formato 'YYYY-MM-DD'
        tipo_turno = data.get('tipo_turno', 'LIBRE')
        puesto = data.get('puesto', 'Puesto Principal')
        observaciones = data.get('observaciones', '')

        if not fecha:
            raise ValueError("La fecha del turno es obligatoria.")

        self.calendario_model.guardar_o_actualizar(
            usuario_id=usuario_id,
            fecha=fecha,
            tipo_turno=tipo_turno,
            puesto=puesto,
            observaciones=observaciones
        )
        return True

    def eliminar_turno(self, usuario_id, fecha):
        if not usuario_id:
            raise ValueError("Usuario no autenticado")
        
        if not fecha:
            raise ValueError("La fecha es obligatoria para eliminar el turno.")

        self.calendario_model.eliminar(usuario_id, fecha)
        return True