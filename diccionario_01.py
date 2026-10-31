import json
import lasvocales

# --- 1. NUESTRO DICCIONARIO EN MEMORIA ---
diccionario = {
    "おはようございます": "buenos dias",
    "こんにちは": "buenas tardes",
    "こんばんは": "buenas noches",
    "おやすみなさい": "buenas noches irse a dormir",
    "いってきます": "ya vuelvo hasta luego",
    "いってらっしゃい": "que te vaya bien hasta luego",
    "ただいま": "ya llegue estoy en casa",
    "おかえりなさい": "bienvenido de vuelta",
    "いらっしゃいませ": "bienvenido para tiendas",
    "ようこそ": "bienvenido en general"
}

# --- 2. CARGAR DESDE EL ARCHIVO ---
try:
    with open("palabras.json", "r", encoding="utf-8") as f:
        diccionario = json.load(f)
    print("✅ Memoria cargada desde palabras.json")
except FileNotFoundError:
    print("⚠️ No hay palabras.json, se usará la memoria inicial.")
except json.JSONDecodeError:
    print("⚠️ El JSON está dañado.")
except Exception as e:
    print(f"⚠️ Error inesperado: {e}")

# --- 3. FUNCIONES ---
def ver_todas():
    if not diccionario:
        print("El diccionario está vacío.")
        return
    for jp, es in diccionario.items():
        print(jp, " : ", es)
    # También muestra lo que viene de lasvocales
    print("\n--- Vocales desde lasvocales.py ---")
    for jp, es in lasvocales.las_vocales.items():
        print(jp, " : ", es)

def guardar():
    try:
        with open("palabras.json", "w", encoding="utf-8") as f:
            json.dump(diccionario, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"⚠️ No se pudo guardar: {e}")

def agregar():
    jp = input("Japonés: ").strip()
    es = input("Español: ").strip()
    if jp == "" or es == "":
        print("❌ No puedes dejar campos vacíos.")
        return
    diccionario[jp] = es
    guardar()
    print("✅ Palabra guardada.")

def borrar():
    jp = input("¿Qué palabra borrar?: ").strip()
    if jp in diccionario:
        del diccionario[jp]
        guardar()
        print("🗑️ Eliminada.")
    else:
        print("❌ No existe.")

def combinar_archivo():
    nombre = input("Nombre del archivo a combinar (ej: lasvocales.json): ").strip()
    try:
        with open(nombre, "r", encoding="utf-8") as f:
            nuevas = json.load(f)
        diccionario.update(nuevas)
        guardar()
        print(f"📦 Combinado {nombre} con éxito!")
    except FileNotFoundError:
        print("❌ Ese archivo no existe.")
    except json.JSONDecodeError:
        print("❌ No es un JSON válido.")

# --- 4. AQUÍ ES DONDE VA EL TRUCO ---
# Todo lo de abajo solo se ejecuta si corres diccionario_01.py directamente
# Si otro archivo hace "import diccionario_01", esto NO se ejecuta y no crea bucle
if __name__ == "__main__":
    print(f"Vocales cargadas: {lasvocales.las_vocales}")

    while True:
        print("\n--- DICCIONARIO ESPAÑOL-JAPONÉS ---")
        print("1. Ver todas")
        print("2. Agregar")
        print("3. Borrar")
        print("4. Combinar archivo")
        print("5. Salir")
        
        opcion = input("Elige: ").strip()
        
        if opcion == "1":
            ver_todas()
        elif opcion == "2":
            agregar()
        elif opcion == "3":
            borrar()
        elif opcion == "4":
            combinar_archivo()
        elif opcion == "5":
            print("¡Saliendo!")
            break
        else:
            print("❌ Opción inválida")