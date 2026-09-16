from flask import Blueprint, request, session, jsonify
from services.incidente_service import IncidenteService

incidente_bp = Blueprint('incidente', __name__)
incidente_service = IncidenteService()

@incidente_bp.route('/api/incidentes', methods=['POST'])
def registrar_incidente():
    try:
        usuario_id = session.get('usuario_id')
        
        # Si no hay sesión válida por alguna razón, se registra de todos modos para probar
        if not usuario_id:
            print("[WARN] Guardando incidente sin usuario_id activo en sesión.")
            usuario_id = "000000000000000000000000"

        data = request.get_json(force=True) or {}
        print(f"[BACKEND] Recibido payload de incidente: {data}")

        res = incidente_service.crear_incidente(
            usuario_id=usuario_id,
            titulo=data.get('titulo', 'Sin Título'),
            categoria=data.get('categoria', 'OTRO'),
            prioridad=data.get('prioridad', 'BAJA'),
            ubicacion=data.get('ubicacion', ''),
            descripcion=data.get('descripcion', '')
        )
        
        return jsonify(res), 200

    except Exception as e:
        print(f"[ERROR CRÍTICO CONTROLLER]: {e}")
        return jsonify({"ok": False, "mensaje": str(e)}), 500