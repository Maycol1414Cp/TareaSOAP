from zeep import Client
client=Client("http://localhost:8008")
result=client.service.saludar("Michael")
print(result)
Ejerc1=client.service.SumaDosNumeros(2,3)
print(Ejerc1)
Ejerc2=client.service.CadenaPalindromo("reconocer")
print(Ejerc2)