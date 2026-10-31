import json
import lasvocales

# --- CARGAMOS TU DICCIONARIO PRINCIPAL ---
try:
    with open("palabras.json", "r", encoding="utf-8") as f:
        frases_principales = json.load(f)
except:
    frases_principales = {
        "おはようございます": "buenos dias",
        "こんにちは": "buenas tardes"
    }

# --- FUNCIÓN PARA MOSTRAR CUALQUIER CATEGORÍA ---
def mostrar(nombre, datos):
    print(f"\n--- {nombre.upper()} ---")
    if not datos:
        print("Vacío")
        return
    for jp, es in datos.items():
        print(f"{jp} : {es}")

# --- MENÚ JEFE - EL QUE CONTROLA LA FILA ---
if __name__ == "__main__":
    print("✅ Memoria lista. Todos en fila esperando órdenes.")
    
    while True:
        print("\n--- DICCIONARIO POR CATEGORIAS ---")
        print("1. Ver solo vocales (desde lasvocales.py)")
        print("2. Ver frases principales (desde palabras.json)")
        print("3. Ver TODO junto")
        print("4. Salir")
        
        op = input("Elige: ").strip()
        
        if op == "1":
            mostrar("vocales", lasvocales.las_vocales)
        elif op == "2":
            mostrar("frases principales", frases_principales)
        elif op == "3":
            mostrar("vocales", lasvocales.las_vocales)
            mostrar("frases principales", frases_principales)
        elif op == "4":
            print("¡Hasta luego!")
            break
        else:
            print("❌ Opción mala")

