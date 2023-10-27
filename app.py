import random
import string
import requests

ipv4_capable = False
ipv4_address = None
ipv6_capable = False
ipv6_address = None

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


worker_id =  ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
print("worker_id: ", worker_id)
print("ipv4_capable: ", ipv4_capable, "| ipv4_address: ", ipv4_address)
print("ipv6_capable: ", ipv6_capable, "| ipv6_address: ", ipv6_address)
print("hello, world!")
