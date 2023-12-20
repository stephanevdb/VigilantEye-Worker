import random
from flask import Flask, request, send_from_directory
import string
from werkzeug.utils import secure_filename
import requests
import os
from time import sleep

state = 'idle'

worker_id =  ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

ipv4_capable = False
ipv4_address = None
ipv6_capable = False
ipv6_address = None

app = Flask(__name__)
UPLOAD_PATH = "UPLOADS"
upload_path = os.path.join(UPLOAD_PATH)
if not os.path.isdir(upload_path):
    os.mkdir(upload_path)

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
    output = f"{worker_id},{state}"
    return output

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    print("Uploading file...")
    if request.method == 'POST':
        f = request.files['file']
        print(os.path.join(upload_path, secure_filename(f.filename)))
        f.save(os.path.join(upload_path, secure_filename(f.filename)))
        print(f"File {f.filename} uploaded successfully")
        return 'file uploaded successfully'
    return "upload", 200

@app.route('/job', methods = ['GET', 'POST'])
def job():
    state = 'running'
    print("Job started")
    print("Running job...")
    # TODO
    print("Waiting for job...")
    state = 'idle'
    return "job"
  

@app.route("/")
def index():
    return "I'm a teapot!", 418

try:
    requests.post(f"http://{master_ip}:{master_port}/add_worker", data=init_message)
    print("Worker added successfully")
except requests.exceptions.RequestException as e:
    print("Error adding worker:", e)

print("Waiting for job...")

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0",port=8667)