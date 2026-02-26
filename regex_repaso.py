#1)
import re

text="El servidor principal está en 192.168.1.1, pero el de respaldo usa la IP 10.0.0.254. La dirección 999.999 es inválida."

pattern=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
ips=re.findall(pattern,text)

print(f'IPs encontradas: {ips}')
