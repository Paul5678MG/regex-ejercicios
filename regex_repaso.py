#1)
import re

text="El servidor principal está en 192.168.1.1, pero el de respaldo usa la IP 10.0.0.254. La dirección 999.999 es inválida."

pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
ips=re.findall(pattern,text)

print(f'IPs encontradas: {ips}')



#2)
import re

logs_text="ID: 101 - ACCESO: paul_admin, ID: 102 - ACCESO: guest_user, ID: 103 - ACCESO: root_sistemas"

pattern = r".+?\-.+?\:\ (\w+)"
accesos=re.findall(pattern,logs_text,flags=re.IGNORECASE)

print(f"Usuarios detectados: {accesos}")



#3)
import re 

pago_info="El pago de la matrícula es S/ 1200.50 y la cuota del carnet es S/ 15.00."

pattern=r"S/\ (\d+\.\d+)"

resultado=re.sub(pattern,"S/ [OCULTO]",pago_info)
print(resultado)


#4)
import re

cadena="Visita www.google.com, www.github.io y también www.trujillo-sistemas.edu.pe"

pattern=r"\.([a-zA-Z_-]+?)\."

dominios=re.findall(pattern,cadena)
print(dominios)


#5)
import re

codigos=["P1234A", "XP1234A", "P1234AB", "P123A"]

pattern=r"^P{1}\d{4}[A-Z]{1}$"

for i in codigos:
    prueba=re.fullmatch(pattern,i)
    if prueba:
        print(f"Codigo valido: {i}")
    else:
        print(f"Codigo invalido: {i}")
    print("----------------------------")


#6)
import re

text_precio="Precio_Unitario: 150.50, Costo: 45.00, Oferta: !!!9.99!!!"

pattern=r"[0-9]{1,}?\.[0-9]{2}?"

precios=re.findall(pattern,text_precio)
print(precios)

#FINAL
import re

datos_mixtos = ["Precio: 10.50", None, "Costo: 5.00", 100]

pattern=r"\d+?\.\d+?"
lista_encontrados=list()

for i in datos_mixtos:
    try:
        encontrado=re.findall(pattern,i)
        print(f"Encontrado: {encontrado}✅")
        lista_encontrados.extend(encontrado)
    except Exception as e:
        print(f"Error: {e}")
        print(f"Details: {type(e).__name__}")
    finally:
        print("------------------------------")
print(f'Listado: {lista_encontrados}')