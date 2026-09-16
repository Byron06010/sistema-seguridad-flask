from datetime import datetime

class MarcaModel:
    @staticmethod
    def crear_marca(usuario_id, nombre_usuario, tipo_marca, observaciones=""):
        return {
            "usuario_id": usuario_id,
            "nombre_usuario": nombre_usuario,
            "tipo_marca": tipo_marca,  # INICIO_TURNO, SALIDA_COLACION, RETORNO_COLACION, FIN_TURNO
            "fecha_hora": datetime.now(),
            "observaciones": observaciones
        }