import ipinfo
import time
from threading import Thread

access_token = '84546d1f1eb9a9'
handler = ipinfo.getHandler(access_token)

def ipinfo (ip):
    try:
        details = handler.getDetails(ip)
        print("_____________________________________")
        print(f'IP: {ip.rstrip()}')
        print(f'City: {details.city}')
        print(f'Region: {details.region}')
        print(f'Country: {details.country}')
        print(f'Location: {details.loc}')
        print(f'ISP: {details.org}')
        print(f'Timezone: {details.timezone}')
        print("_____________________________________\n")
    except Exception:
        print("Error al verificar ip")

def ip_info_seq ():
    print("Iniciando proceso secuencial")
    start_time = time.time()
    ip_file = open("src/ip.txt")
    ips = ip_file.readlines()
    for ip in ips:
        ipinfo(ip)
    end_time = time.time()
    str1 = "USANDO PROCESO SECUENCIAL\n"
    str2 = f'It took {end_time - start_time: 0.4f} second(s) to complete.'
    return str1+str2

def ip_info_par ():
    print("Iniciando procesos en paralelo")
    start_time2 = time.time()
    ip_file = open("src/ip.txt")
    ips = ip_file.readlines()
    threads = []
    for ip in ips:
        t = Thread(target=ipinfo, args=(ip,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end_time2 = time.time()   
    str1 = "USANDO PROCESOS PARALELOS\n"
    str2 = f'It took {end_time2 - start_time2: 0.4f} second(s) to complete.'
    return str1 + str2


result_seq = ip_info_seq () #tiempo promedio 20.133 segundos
result_par = ip_info_par () #tiempo promedio 0.045 segundos
print(result_seq)
print(result_par)