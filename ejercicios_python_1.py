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

print(extraer_vulnerabilidades("ejercicios_repaso_FINAL\\escaneo.txt"))



#6)
def consolidar_reportes(archivo_destino, *archivos_origen):
    try:
        lista_final=list()
        for log in archivos_origen:
            with open(log, "r", encoding="UTF-8") as file:
                text=file.readlines()
                error_o_critico=[x for x in text if "ERROR" in x or "CRITICO" in x]
                lista_final.extend(error_o_critico)
        with open(archivo_destino, "a",encoding="UTF-8") as file:
            for i,linea in enumerate(lista_final):
                file.write(f"{i+1}.- {linea}")
            file.write(f"\nErrores: {len(lista_final)}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print(f"Details: {type(e).__name__}")
    except Exception as e:
        print(f"Error: {e}")
        print(f"Details: {type(e).__name__}")
    return f"Errores encontrados: {len(lista_final)}"

print(consolidar_reportes("ejercicios_repaso_FINAL\\reporte.txt", "ejercicios_repaso_FINAL\\log1.txt", "ejercicios_repaso_FINAL\\log2.txt", "ejercicios_repaso_FINAL\\log3.txt"))



#7)
import re

def buscar_credenciales_expuestas(ruta):
    contras_expuestas=[]
    pattern = r'(password|pwd)\s*=\s*["\'](.*?)["\']'
    with open(ruta, "r", encoding="UTF-8") as file:
        text=file.readlines()
        for line in text:
            contra_hardcodeada=re.search(pattern,line)
            if contra_hardcodeada:
                print("[RIESGO] Credencial expuesta detectada",contra_hardcodeada)
                print(f"Linea: {line}")
                contras_expuestas.append(contra_hardcodeada.group(0))
    return contras_expuestas


lista=buscar_credenciales_expuestas("ejercicios_repaso_FINAL\\credenciales.txt")
print(f"Credenciales Expuestas: {lista}")



#8)
import re

def sanitizar_nombres(*nombres_sucios):
    pattern= r"[^a-zA-Z\s]"
    limpios=[re.sub(pattern,"",nombre).title() for nombre in nombres_sucios if len(re.sub(pattern,"",nombre)) >= 3]
    return limpios

nombres_sucios = ["juan123", "ana!@#", "maría", "pe!p3e", "  "]
print(sanitizar_nombres(*nombres_sucios))



#9)
ips = ["192.168.1.1", "10.0.0.1", "8.8.8.8", "172.16.50.25"]

def verificar_ips(*ips):
    if ips:
        for ip in ips:
            if ip.startswith("192.168."):
                print("[LOCAL] Acceso permitido")
            elif ip.startswith("10."):
                print("[VPN] Acceso seguro")
            else:
                print("[EXTERNO] Bloqueado por seguridad")
    else:
        return f"No hay IPs para verificar❌"
    return f"Verificación exitosa✅"

print(verificar_ips(*ips))



#10)
precios = [150, 200, 85, 310, 50]

precios_con_descuento=list(map(lambda x: x*0.85 ,precios))
precio_mayores_100=list(filter(lambda x: x>100 , precios_con_descuento))

print(precio_mayores_100)



#11)
logs = [" error: humedad baja ", " CRITICO: sensor desconectado ", " error: temperatura alta "]

logs_limpios=list(map(lambda x: x.strip().upper() ,logs))
print(logs_limpios)
