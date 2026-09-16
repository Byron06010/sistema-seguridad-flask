from flask import request, jsonify, session, render_template
from service.ronda_service import RondaService

ronda_service = RondaService()

def crear_ronda_controller():
    try:
        # Intenta obtener el ID de usuario desde varios nombres típicos de sesión
        usuario_id = session.get('usuario_id') or session.get('user_id') or session.get('id')
        
        data = request.get_json()
        if not data:
            return jsonify({'ok': False, 'mensaje': 'No se recibieron datos JSON'}), 400

        ronda_id = ronda_service.registrar_ronda(usuario_id, data)
        return jsonify({'ok': True, 'mensaje': 'Ronda registrada exitosamente', 'id': ronda_id}), 201

    except Exception as e:
        print(f"❌ EXCEPCIÓN EN CREAR_RONDA_CONTROLLER: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'ok': False, 'mensaje': str(e)}), 500