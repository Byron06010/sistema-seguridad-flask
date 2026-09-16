from datetime import datetime
import json
from flask import Blueprint, render_template, session, redirect, url_for, request, jsonify
from bson.objectid import ObjectId
from database.connection import get_db
from services.ronda_service import RondaService
from services.calendario_service import CalendarioService

turno_bp = Blueprint('turno', __name__)
ronda_service = RondaService()
calendario_service = CalendarioService()

@turno_bp.route('/control-turno')
@turno_bp.route('/dashboard')
def dashboard_page():
    usuario_id = session.get('usuario_id') or session.get('user_id')
    
    db = get_db()
    usuario = None
    if usuario_id:
        try:
            usuario = db.usuarios.find_one({"_id": ObjectId(usuario_id)})
        except Exception:
            usuario = db.usuarios.find_one({"_id": usuario_id})

    # Consultar Incidentes
    incidentes_raw = list(db.incidentes.find().sort("fecha_registro", -1))
    incidentes = []
    for inc in incidentes_raw:
        inc['_id'] = str(inc['_id'])
        fecha = inc.get("fecha_registro")
        inc["fecha_formateada"] = fecha.strftime('%Y-%m-%d %H:%M:%S') if isinstance(fecha, datetime) else str(fecha or '-')
        incidentes.append(inc)

    # Rondas
    rondas = ronda_service.obtener_historial_rondas()
    ronda_activa = ronda_service.obtener_ronda_activa(usuario_id) if usuario_id else None

    # Timestamp de inicio de turno general
    inicio_turno_iso = session.get('inicio_turno_iso', '')
    if not inicio_turno_iso and usuario:
        inicio_turno_iso = usuario.get('inicio_turno_iso', '')

    # Obtener turnos de calendario y mapearlos como un diccionario por fecha ('YYYY-MM-DD') para el frontend
    turnos_raw = calendario_service.obtener_turnos(usuario_id) if usuario_id else []
    turnos_dict = {t['fecha']: t for t in turnos_raw}

    return render_template(
        'dashboard/control_turno.hbs',
        usuario=usuario,
        incidentes=incidentes,
        rondas=rondas,
        ronda_activa=ronda_activa,
        inicio_turno_iso=inicio_turno_iso,
        turnos_calendario_json=json.dumps(turnos_dict)
    )

@turno_bp.route('/api/rondas/iniciar', methods=['POST'])
def api_iniciar_ronda():
    usuario_id = session.get('usuario_id') or session.get('user_id')
    if not usuario_id:
        return jsonify({"ok": False, "mensaje": "Sesión no válida"}), 401

    data = request.get_json() or {}
    try:
        ronda_id = ronda_service.iniciar_ronda(usuario_id, data)
        return jsonify({"ok": True, "mensaje": "Ronda iniciada", "id": ronda_id}), 201
    except Exception as e:
        return jsonify({"ok": False, "mensaje": str(e)}), 400

@turno_bp.route('/api/rondas/finalizar', methods=['POST'])
def api_finalizar_ronda():
    usuario_id = session.get('usuario_id') or session.get('user_id')
    if not usuario_id:
        return jsonify({"ok": False, "mensaje": "Sesión no válida"}), 401

    data = request.get_json() or {}
    try:
        ronda_service.finalizar_ronda(usuario_id, data)
        return jsonify({"ok": True, "mensaje": "Ronda finalizada correctamente"}), 200
    except Exception as e:
        return jsonify({"ok": False, "mensaje": str(e)}), 400

@turno_bp.route('/api/calendario/guardar', methods=['POST'])
def api_guardar_turno():
    usuario_id = session.get('usuario_id') or session.get('user_id')
    if not usuario_id:
        return jsonify({"ok": False, "mensaje": "Sesión no válida"}), 401

    data = request.get_json() or {}
    try:
        calendario_service.programar_turno(usuario_id, data)
        return jsonify({"ok": True, "mensaje": "Turno guardado en calendario correctamente"}), 200
    except Exception as e:
        return jsonify({"ok": False, "mensaje": str(e)}), 400
    
@turno_bp.route('/api/calendario/eliminar', methods=['POST'])
def api_eliminar_turno():
    usuario_id = session.get('usuario_id') or session.get('user_id')
    if not usuario_id:
        return jsonify({"ok": False, "mensaje": "Sesión no válida"}), 401

    data = request.get_json() or {}
    fecha = data.get('fecha')
    
    if not fecha:
        return jsonify({"ok": False, "mensaje": "Fecha no especificada"}), 400

    try:
        # Llamamos al servicio real para que borre el registro en la base de datos
        calendario_service.eliminar_turno(usuario_id, fecha)
        return jsonify({"ok": True, "mensaje": "Turno eliminado correctamente de la base de datos"}), 200
    except Exception as e:
        return jsonify({"ok": False, "mensaje": str(e)}), 400