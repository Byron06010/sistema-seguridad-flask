from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()

@auth_bp.route('/')
def login_page():
    if "usuario_id" in session:
        return redirect(url_for('turno.dashboard_page'))
    return render_template('auth/login.hbs')

@auth_bp.route('/register')
def register_page():
    if "usuario_id" in session:
        return redirect(url_for('turno.dashboard_page'))
    return render_template('auth/register.hbs')

@auth_bp.route('/api/auth/register', methods=['POST'])
def register_api():
    data = request.json
    res = auth_service.registrar_usuario(
        rut=data.get('rut'),
        nombre=data.get('nombre'),
        email=data.get('email'),
        password=data.get('password'),
        rol=data.get('rol', 'GUARDIA')
    )
    status_code = 201 if res['ok'] else 400
    return jsonify(res), status_code

@auth_bp.route('/api/auth/login', methods=['POST'])
def login_api():
    data = request.json
    res = auth_service.autenticar(data.get('email'), data.get('password'))
    
    if res['ok']:
        user = res['usuario']
        session['usuario_id'] = str(user['_id'])
        session['nombre'] = user['nombre']
        session['rol'] = user['rol']
        return jsonify({'ok': True, 'mensaje': 'Autenticación exitosa'}), 200
    
    return jsonify(res), 401

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login_page'))