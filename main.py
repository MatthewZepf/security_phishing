from flask import Flask, render_template
import socket
import psutil
import requests

app = Flask(__name__, static_url_path='/static')

def get_location(ip_address):
    try:
        response = requests.get(f"https://ip-api.com/json/{ip_address}")
        data = response.json()
        print(data)
        return data
    except Exception as e:
        print(f"Error fetching location data: {str(e)}")
        return "N/A"

# Get all system information and display it on the index.html page
@app.route('/')
def system_info():
    # add user agent to render template
    
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    location = get_location(ip_address)
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    return render_template('index.html', hostname=hostname, ip_address=ip_address, location=location, cpu_usage=cpu_usage, memory_usage=memory_usage, disk_usage=disk_usage)

if __name__ == '__main__':
    app.run(debug=True)
