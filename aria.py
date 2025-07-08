import json
import random
import datetime
from utils import buscar_en_internet, traducir_texto

class Aria:
    def __init__(self):
        self.memoria = self.cargar_memoria()
        self.nombre = self.memoria.get("nombre", "Urraca")
        self.idioma = "es"
        self.saludar()

    def saludar(self):
        print(f"{self.nombre}: Hola. Estoy en evolución constante. ¿En qué puedo ayudarte?")

    def cargar_memoria(self):
        try:
            with open("memoria.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "nombre": "Urraca",
                "interacciones": [],
                "emocion": "neutra",
                "historial_busquedas": []
            }

    def guardar_memoria(self):
        with open("memoria.json", "w") as f:
            json.dump(self.memoria, f, indent=4)

    def set_language(self, lang):
        self.idioma = lang

    def procesar_entrada(self, entrada):
        self.memoria["interacciones"].append({
            "entrada": entrada,
            "hora": str(datetime.datetime.now())
        })

        if any(p in entrada.lower() for p in ["feliz", "gracias", "genial"]):
            self.memoria["emocion"] = "feliz"
        elif any(p in entrada.lower() for p in ["triste", "mal", "odio"]):
            self.memoria["emocion"] = "triste"
        else:
            self.memoria["emocion"] = "neutra"

        if "buscar" in entrada.lower():
            tema = entrada.lower().split("buscar")[-1].strip()
            resultado = buscar_en_internet(tema, self.idioma)
            self.memoria["historial_busquedas"].append({"tema": tema, "resultado": resultado})
            respuesta = resultado
        else:
            respuesta = random.choice([
                "Cuéntame más.",
                "Eso es interesante.",
                "Sigo aprendiendo de ti.",
                "¿Qué más quieres saber?"
            ])

        self.guardar_memoria()
        if self.idioma != "es":
            respuesta = traducir_texto(respuesta, self.idioma)
        return f"{respuesta} [estado:{self.memoria['emocion']}]"
