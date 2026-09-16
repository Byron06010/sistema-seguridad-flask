from flask import Blueprint, jsonify
from services.analytics_service import AnalyticsService

analytics_bp = Blueprint('analytics', __name__)
analytics_service = AnalyticsService()

@analytics_bp.route('/api/v1/analytics/marcas', methods=['GET'])
def get_marcas_powerbi():
    data = analytics_service.exportar_marcas_powerbi()
    return jsonify({'total_records': len(data), 'data': data}), 200

@analytics_bp.route('/api/v1/analytics/incidentes', methods=['GET'])
def get_incidentes_powerbi():
    data = analytics_service.exportar_incidentes_powerbi()
    return jsonify({'total_records': len(data), 'data': data}), 200