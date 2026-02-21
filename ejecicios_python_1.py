#1)
puertos_objetivo=[21, 22, 80, 443 , 3306]
contador=0

def monitoreo(*lista):
    puertos_criticos=list()
    for puerto in puertos_objetivo:
        if puerto == (22 or 21):
            puertos_criticos.append(puerto)
            print(f"Puerto crítico detectado: {puerto}. Se requiere cifrado fuerte.")
        elif puerto == 3306:
            puertos_criticos.append(puerto)
            print(f"Puerto: {puerto}. Base de datos detectada. Verificar acceso desde Trujillo.")
        else:
            print(f"Puerto {puerto} bajo monitoreo estandar.")
    return puertos_criticos

puertos_criticos=monitoreo(*puertos_objetivo)
print(f'''
PUERTOS CRITICOS:
-----------------
{puertos_criticos}
Cantidad: {len(puertos_criticos)}
      ''')



#2)
db_amenazas={
    "CVE-001":{
        "descripcion": "Inyección SQL",
        "gravedad": "Alta",
        "estado": "No resuelto"
    },
    "CVE-002":{
        "descripcion": "Cross-Site Scripting (XSS)",
        "gravedad": "Media",
        "estado": "Resuelto"
    }
}

def consultar_amenaza(codigo, **detalles):
    try:
        for code,info in detalles.items():
            if code == codigo:
                print(f"Amenaza detectada: {info.get("descripcion",0)}")
                print(f"Gravedad: {info.get("gravedad",0)}")
                print(f"Estado: {info.get("estado",0)}")
                return
            else:
                raise KeyError("Registrar nueva amenaza")
    except KeyError as e:
        print(f"Error: {e}")
        print(f"Details: {type(e).__name__}")

consultar_amenaza("CVE-001",**db_amenazas)


#3)
import re

cadena = "USR:admin_IP:192.168.1.1_LVL:high;USR:guest_IP:10.0.0.5_LVL:low;"

lista_cadena=cadena.split(";")
print(f"Eventos: {lista_cadena}")

pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
lista_ips=[re.findall(pattern,evento)[0] for evento in lista_cadena if re.findall(pattern,evento)]
print(f"IPs extraídas: {lista_ips}")

pattern1=r"USR:([^_]+)_IP"
cadena_editada=re.sub(pattern1,"USR:[REDACTED]_IP",cadena)
print(f"Cadena editada: {cadena_editada}")

#4)
tokens_activos={
    "TK-96":"ADMIN",
    "TK-97":"USER",
    "TK-98":"USER",
    "TK-99":"GUEST"
}

class TokenInvalido(Exception):
    def __init__(self,err):
        print(f"Error: {err}")

def verificar_acceso(token_id):
    try:
        if token_id in tokens_activos:
            if tokens_activos[token_id]=="ADMIN":
                print("[ACCESO TOTAL] Bienvenido, Paul.")
            elif tokens_activos[token_id]=="GUEST":
                print("[ACCESO LIMITADO] Solo lectura.")
            elif tokens_activos[token_id]=="USER":
                print("[ACCESO COMÚN] Lectura y edición")
        else:
            raise TokenInvalido("[ALERTA] Token inválido detectado.")
    except TokenInvalido as e:
        print(f"Details: {type(e).__name__}")
    else:
        print("No hubo tokens invalidos.")
    finally:
        print("Verificación completada")

verificar_acceso("TK-96")

#5)
import re

def extraer_vulnerabilidades(ruta):
    with open(ruta, "r",encoding="UTF-8") as file:
        text=file.read()
        
        pattern=r"CVE{1}\-{1}\d{4}\-\d{4}"
        
        codigos=re.findall(pattern,text)
        print(f"Codigos: {codigos}")
        
        codigos_unicos=set(codigos)
        print(f"Codigos unicos: {codigos_unicos}")
        
        with open("ejercicios_repaso_FINAL\\extraccion.txt", "w",encoding="UTF-8") as file:
            file.write(text)
            file.write("\n----------------------------------\n")
            file.write(f"Codigos: {codigos}\n")
            file.write(f"Codigos unicos: {codigos_unicos}")
    return f"Extracción exitosa✅"

extraer_vulnerabilidades("ejercicios_repaso_FINAL\\escaneo.txt")