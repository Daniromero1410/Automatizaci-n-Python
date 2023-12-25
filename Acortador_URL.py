import pyshorteners

url = input("Por favor ingrese la URL: ")

#Servicio de TinyURL 
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(url)

print("Tu URL acortada es: "+ short_url)
