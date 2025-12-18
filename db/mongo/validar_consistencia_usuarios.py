from pymongo import MongoClient
import re

client = MongoClient("mongodb://localhost:27017")
db = client["qa_testing"]
collection = db["test_usuarios"]

email_regex = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

print("🔍 Validando consistencia de usuarios...\n")

errores = []

for user in collection.find():
    user_id = str(user.get("_id"))

    # Validar nombre
    if "nombre" not in user or not user["nombre"]:
        errores.append(f"{user_id}: Falta campo obligatorio 'nombre'")

    # Validar email
    email = user.get("email")
    if not email:
        errores.append(f"{user_id}: Falta campo obligatorio 'email'")
    elif not email_regex.match(email):
        errores.append(f"{user_id}: Email inválido → {email}")

    # Validar activo
    if "activo" not in user:
        errores.append(f"{user_id}: Falta campo obligatorio 'activo'")
    elif not isinstance(user["activo"], bool):
        errores.append(f"{user_id}: Campo 'activo' no es boolean")

# Resultado final
if errores:
    print("❌ Inconsistencias encontradas:\n")
    for e in errores:
        print(" -", e)
else:
    print("✔ Todos los registros son consistentes")

print("\n✅ Validación de consistencia finalizada")

























