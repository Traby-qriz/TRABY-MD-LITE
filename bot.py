from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Configuration
WHATSAPP_API_URL = 'https://your-whatsapp-api-url/v1/messages'
ACCESS_TOKEN = os.getenv('WHATSAPP_ACCESS_TOKEN')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(data)  # Log incoming messages
    return '', 200

def send_message(to, message):
    url = WHATSAPP_API_URL
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'to': to,
        'type': 'text',
        'text': {
            'body': message
        }
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Make it accessible externally