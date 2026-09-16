import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
from config.settings import Config

class Database:
    _instance = None
    _client = None
    _db = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._connect()
        return cls._instance

    @classmethod
    def _connect(cls):
        try:
            print("[INFO] Conectando a la base de datos MongoDB...")
            cls._client = MongoClient(Config.MONGO_URI, serverSelectionTimeoutMS=5000)
            
            # Forzar prueba de conexión activa
            cls._client.admin.command('ping')
            
            cls._db = cls._client[Config.MONGO_DB_NAME]
            print(f"[OK] Conexión exitosa a la base de datos: '{Config.MONGO_DB_NAME}'")
            
            # Inicializar índices para consultas de alto rendimiento (Power BI & Búsquedas)
            cls._init_indexes()

        except (ConnectionFailure, ServerSelectionTimeoutError) as err:
            print(f"[ERROR] No se pudo conectar a MongoDB: {err}")
            print("[CONSEJO] Asegúrate de que el servicio de MongoDB esté ejecutándose localmente.")
            sys.exit(1)

    @classmethod
    def _init_indexes(cls):
        """Crea índices para búsquedas rápidas e ingesta eficiente en Power BI."""
        try:
            cls._db.usuarios.create_index("email", unique=True)
            cls._db.marcas.create_index([("usuario_id", 1), ("fecha", -1)])
            cls._db.incidentes.create_index([("fecha_registro", -1), ("prioridad", 1)])
            print("[OK] Índices de base de datos validados.")
        except Exception as e:
            print(f"[WARN] Error creando índices: {e}")

    def get_db(self):
        return self._db

# Helper global para importar la BD directamente
def get_db():
    return Database().get_db()