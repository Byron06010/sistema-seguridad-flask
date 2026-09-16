from flask import Flask
from config.settings import Config

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_object(Config)

    # Registro de Blueprints (Controladores)
    from controllers.auth_controller import auth_bp
    from controllers.turno_controller import turno_bp
    from controllers.incidente_controller import incidente_bp
    from controllers.analytics_controller import analytics_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(turno_bp)
    app.register_blueprint(incidente_bp)
    app.register_blueprint(analytics_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    print(f"[INFO] Servidor iniciando en http://127.0.0.1:{Config.PORT}")
    app.run(host='0.0.0.0', port=Config.PORT, debug=Config.DEBUG)