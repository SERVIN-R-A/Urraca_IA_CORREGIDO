import wikipedia
from googletrans import Translator

def buscar_en_internet(tema, idioma="es"):
    try:
        wikipedia.set_lang(idioma)
        resumen = wikipedia.summary(tema, sentences=2)
        return resumen
    except:
        return "No encontré resultados claros, pero seguiré investigando."

def traducir_texto(texto, destino="es"):
    try:
        traductor = Translator()
        traduccion = traductor.translate(texto, dest=destino)
        return traduccion.text
    except:
        return texto
