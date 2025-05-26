from datetime import datetime
import random

print("Chatbot: ¡Hola! Soy el asistente virtual de la biblioteca. ¿En qué puedo ayudarte hoy?")

catalogo = {
    "tecnología": ["Introducción a la IA", "Fundamentos de Redes", "Programación en Python"],
    "literatura": ["Cien Años de Soledad", "Romeo y Julieta", "El Principito"],
    "ciencia": ["Física para Principiantes", "Biología Moderna", "Química Básica"],
    "romance juvenil": ["Todos los lugares que mantuvimos en secreto", "Nosotros en la luna", "El arte de ser nosotros"]
}

metodos_pago = [
    "Efectivo",
    "Tarjeta de crédito/débito",
    "Transferencia bancaria",
    "Pago móvil (Yape, Plin, etc.)",
    "Pago en línea (PayPal)"
]

bancos = ["Banco Pichincha", "Banco Guayaquil", "Banco del Pacífico", "Produbanco", "Banco Bolivariano"]

def generar_numero_cuenta():
    return "".join(str(random.randint(0,9)) for _ in range(12))

climas_simulados = {
    "quito": ["18°C con cielos nublados", "17°C con lluvias ligeras", "19°C parcialmente soleado"],
    "guayaquil": ["30°C con sol radiante", "29°C y húmedo", "28°C con nubes dispersas"],
    "manta": ["26°C con brisa marina", "27°C soleado", "25°C con algunas nubes"],
    "cuenca": ["16°C y llovizna", "15°C con niebla", "17°C nublado"],
    "el carmen": ["27°C con calor moderado", "28°C soleado", "26°C con algo de humedad"],
}

def obtener_clima(ciudad):
    ciudad = ciudad.lower()
    if ciudad in climas_simulados:
        return f"El clima actual en {ciudad.title()} es {random.choice(climas_simulados[ciudad])}."
    else:
        return f"No tengo datos del clima para '{ciudad}'. Prueba con otra ciudad de Ecuador."

def dias_entrega():
    return random.randint(1, 10)

def esta_disponible(titulo):
    titulo = titulo.lower()
    for libros in catalogo.values():
        for libro in libros:
            if titulo == libro.lower():
                return True, libro
    return False, None

while True:
    user_input = input("Tú: ").lower()

    if user_input == "hola":
        print("Chatbot: ¡Hola! ¿Te interesa consultar libros, métodos de pago, clima o información general?")

    elif user_input in ["¿cómo estás?", "como estás"]:
        print("Chatbot: ¡Estoy bien! Listo para ayudarte con tu búsqueda en la biblioteca y más. 😊")

    elif user_input in ["categorías", "mostrar categorías", "qué categorías hay"]:
        print("Chatbot: Las categorías disponibles son:")
        for categoria in catalogo:
            print(f"- {categoria.title()}")

    elif user_input in ["¿qué libros tienen?", "libros disponibles", "mostrar libros"]:
        print("Chatbot: Tenemos libros en las siguientes categorías:")
        for categoria in catalogo:
            print(f"- {categoria.title()}: {', '.join(catalogo[categoria])}")

    elif user_input.startswith("¿tienen libros de") or user_input.startswith("tienen libros de"):
        tema = user_input.replace("¿tienen libros de", "").replace("tienen libros de", "").replace("?", "").strip()
        if tema in catalogo:
            print(f"Chatbot: Sí, tenemos libros de {tema.title()}: {', '.join(catalogo[tema])}")
        else:
            print(f"Chatbot: Lo siento, no tenemos libros específicamente de '{tema}', pero puedes intentar con otra categoría.")

    elif user_input.startswith("¿está disponible el libro") or user_input.startswith("está disponible el libro"):
        titulo = user_input.replace("¿está disponible el libro", "").replace("está disponible el libro", "").replace("?", "").strip()
        disponible, libro_real = esta_disponible(titulo)
        if disponible:
            print(f"Chatbot: Sí, el libro '{libro_real}' está disponible.")
            dias = dias_entrega()
            print(f"Chatbot: Si no lo tienes contigo, tarda aproximadamente {dias} días en llegar.")
        else:
            print(f"Chatbot: No encontré el libro '{titulo}' en nuestro catálogo.")

    elif user_input.startswith("compara libros") or user_input.startswith("compara libro"):
        try:
            libros_a_comparar = user_input.replace("compara libros", "").replace("compara libro", "").strip()
            libro1, libro2 = [x.strip() for x in libros_a_comparar.split(" y ")]
        except:
            print("Chatbot: Por favor, usa el formato: compara libros [Libro 1] y [Libro 2]")
            continue

        disp1, real1 = esta_disponible(libro1)
        disp2, real2 = esta_disponible(libro2)

        respuesta = "Comparación de libros:\n"
        respuesta += f"- '{libro1}': {'Disponible' if disp1 else 'No disponible'}\n"
        respuesta += f"- '{libro2}': {'Disponible' if disp2 else 'No disponible'}\n"

        if disp1 and disp2:
            dias1 = dias_entrega()
            dias2 = dias_entrega()
            respuesta += f"Tiempo estimado de llegada:\n- '{real1}': {dias1} días\n- '{real2}': {dias2} días"
        print("Chatbot:", respuesta)

    elif user_input in ["métodos de pago", "formas de pago", "cómo puedo pagar"]:
        print("Chatbot: Los métodos de pago aceptados son:")
        for metodo in metodos_pago:
            print(f"- {metodo}")
        print("Chatbot: Si deseas información sobre transferencia bancaria, solo pregunta 'transferencia bancaria'.")

    elif user_input == "transferencia bancaria":
        print("Chatbot: Aquí tienes los bancos y números de cuenta para hacer la transferencia:")
        for banco in bancos:
            cuenta = generar_numero_cuenta()
            print(f"- {banco}: Cuenta No. {cuenta}")
    elif user_input.startswith("quiero comprar"):
        titulo = user_input.replace("quiero comprar", "").strip()
        disponible, libro_real = esta_disponible(titulo)
        if disponible:
            print(f"Chatbot: El libro '{libro_real}' está disponible para la compra.")
            print("Chatbot: Los métodos de pago disponibles son:")
            for metodo in metodos_pago:
                print(f"- {metodo}")
            print("Chatbot: Si deseas información detallada sobre transferencia bancaria, solo pregunta 'transferencia bancaria'.")
        else:
            print(f"Chatbot: Lo siento, no tenemos el libro '{titulo}' disponible para la compra.")

    elif user_input in ["¿en qué país estamos?", "país"]:
        print("Chatbot: La biblioteca está ubicada en Ecuador 🇪🇨")

    elif user_input in ["¿qué fecha es hoy?", "fecha actual"]:
        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        print(f"Chatbot: Hoy es {fecha_actual}")

    elif user_input in ["¿qué hora es?", "hora actual"]:
        hora_actual = datetime.now().strftime("%H:%M:%S")
        print(f"Chatbot: La hora actual es {hora_actual}")

    elif user_input in ["clima actual", "¿qué clima hace?", "temperatura actual"]:
        ciudad = input("Chatbot: ¿De qué ciudad deseas saber el clima?\nTú: ").strip()
        print("Chatbot:", obtener_clima(ciudad))

    elif user_input in ["adiós", "bye", "salir"]:
        print("Chatbot: ¡Adiós! Recuerda que la biblioteca está abierta de lunes a viernes. 📚")
        break

    else:
        print("Chatbot: No entendí eso.Puedes hacer otra pregunta.")
