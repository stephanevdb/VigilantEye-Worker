import random
from flask import Flask, request
import string
import requests
import os
from time import sleep


worker_id =  ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

ipv4_capable = False
ipv4_address = None
ipv6_capable = False
ipv6_address = None

app = Flask(__name__)


master_ip = os.getenv('MASTER_IP')

if not master_ip:
    master_ip = '127.0.0.1'
if ':' in master_ip:
    master_ip = f'[{master_ip}]'
master_port = os.getenv('MASTER_PORT')
if not master_port:
    master_port = 8666

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

init_message = f"{worker_id},{ipv4_capable},{ipv4_address},{ipv6_capable},{ipv6_address}"

print("worker_id: ", worker_id)
print("ipv4_capable: ", ipv4_capable, "| ipv4_address: ", ipv4_address)
print("ipv6_capable: ", ipv6_capable, "| ipv6_address: ", ipv6_address)
print("master_ip: ", master_ip, "| master_port: ", master_port)




@app.route('/ping')
def ping():  
    return 'pong'

@app.route('/job')
def job():
    return "job"
  


try:
    requests.post(f"http://{master_ip}:{master_port}/add_worker", data=init_message)
    print("Worker added successfully")
except requests.exceptions.RequestException as e:
    print("Error adding worker:", e)

print("Waiting for job...")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8667)