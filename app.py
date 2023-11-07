import random
import string
import requests
import os
from time import sleep

#os.environ['MASTER_IP'] = '127.0.0.1'


worker_id =  ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
ipv4_capable = False
ipv4_address = None
ipv6_capable = False
ipv6_address = None

master_ip = os.getenv('MASTER_IP')


try:
    ipv4_address = requests.get('https://api.ipify.org').text
    ipv4_capable = True
except requests.exceptions.RequestException as e:
    print("Error getting IPv4 address:", e)

try:
    ipv6_address = requests.get('https://api6.ipify.org').text
    ipv6_capable = True
except requests.exceptions.RequestException as e:
    print("Error getting IPv6 address:", e)



print("worker_id: ", worker_id)
print("ipv4_capable: ", ipv4_capable, "| ipv4_address: ", ipv4_address)
print("ipv6_capable: ", ipv6_capable, "| ipv6_address: ", ipv6_address)
print("connect_ip: ", master_ip)
print("Waiting for job...")

while True:
    sleep(1)