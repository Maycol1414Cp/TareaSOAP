from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def saludar(nombre):
    return "!Hola {}!".format(nombre)
def SumaDosNumeros(a,b):
    return f"La suma de {a} y {b} es: {a+b}"
def CadenaPalindromo(cad):
    cad.lower()
    return cad==cad[::-1]
dispatcher=SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8008/",
    action="http://localhost:8008/",
    namespace="http://localhost:8008/",
    trace=True,
    ns=True,
)
dispatcher.register_function(
    "saludar",
    saludar,
    returns={"saludo": str},
    args={"nombre": str}
)
dispatcher.register_function(
    "SumaDosNumeros",
    SumaDosNumeros,
    returns={"resultado": str},
    args={"a": int, "b": int}
)
dispatcher.register_function(
    "CadenaPalindromo",
    CadenaPalindromo,
    returns={"resultado": bool},
    args={"cad": str}

)
try:
    server=HTTPServer(("localhost",8008),SOAPHandler)
    server.dispatcher=dispatcher
    print("Servidor corriendo en el puerto 8008")
    server.serve_forever()
except KeyboardInterrupt:
    print("Servidor detenido")
    server.server_close()