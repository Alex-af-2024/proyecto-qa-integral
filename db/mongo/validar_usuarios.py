from pymongo import MongoClient

# Conexión
client = MongoClient("mongodb://localhost:27017")

# Base de datos y colección
db = client["local"]
collection = db["usuarios_test"]

print("🔍 Iniciando validaciones MongoDB...\n")

# Validación 1: existen usuarios activos
active_users = list(collection.find({"activo": True}))

if len(active_users) > 0:
    print(f"✔ Existen usuarios activos: {len(active_users)} encontrado(s)")
else:
    print("⚠ No existen usuarios activos")



print("\n✅ Validación MongoDB finalizada")
