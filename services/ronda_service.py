from database.connection import get_db
from models.ronda_model import RondaModel

class RondaService:
    def __init__(self):
        self.db = get_db()
        self.ronda_model = RondaModel(self.db)

    def obtener_ronda_activa(self, usuario_id):
        if not usuario_id:
            return None
        ronda = self.ronda_model.buscar_activa(usuario_id)
        if ronda:
            ronda['_id'] = str(ronda['_id'])
            ronda['usuario_id'] = str(ronda['usuario_id'])
        return ronda

    def iniciar_ronda(self, usuario_id, data):
        if not usuario_id:
            raise ValueError("Usuario no identificado en sesión")
        if self.ronda_model.buscar_activa(usuario_id):
            raise ValueError("Ya tienes una ronda activa en proceso")

        sector = data.get('sector', 'Ronda General / Sin Sector')
        inicio_iso = data.get('inicio_iso')
        inicio_fecha = data.get('inicio_fecha')
        inicio_hora = data.get('inicio_hora')

        return self.ronda_model.iniciar(
            usuario_id=usuario_id,
            sector=sector,
            inicio_iso=inicio_iso,
            inicio_fecha=inicio_fecha,
            inicio_hora=inicio_hora
        )

    def finalizar_ronda(self, usuario_id, data):
        ronda_activa = self.ronda_model.buscar_activa(usuario_id)
        if not ronda_activa:
            raise ValueError("No hay ninguna ronda activa para finalizar.")

        self.ronda_model.finalizar(
            ronda_id=ronda_activa['_id'],
            fin_fecha=data.get('fin_fecha', ''),
            fin_hora=data.get('fin_hora', ''),
            duracion=data.get('duracion', '00:00:00')
        )
        return True

    def obtener_historial_rondas(self):
        return self.ronda_model.obtener_finalizadas()