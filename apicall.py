import requests

# Define the API endpoint
url = 'https://api.example.com/data'

# Make a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}')


    # post
    import requests

# Define the API endpoint
url = 'https://api.example.com/data'

# Define the data to send in the request body
payload = {'key1': 'value1', 'key2': 'value2'}

# Make a POST request to the API
response = requests.post(url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}')


#Both
from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a route for GET request
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')  # Get 'name' parameter from query string, default to 'World'
    return jsonify({'message': f'Hello, {name}!'})

# Define a route for POST request
@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.json  # Get JSON data from request body
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

#with auth get
import requests

# Define the API endpoint
url = 'https://api.example.com/data'

# Define the headers
headers = {
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
    'Accept': 'application/json',
    'User-Agent': 'my-app'
}

# Define the query parameters
params = {
    'param1': 'value1',
    'param2': 'value2'
}

# Make the GET request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON data
    print(data)
else:
    print(f'Error: {response.status_code}, {response.text}')


#With auth post
import requests

# Define the API endpoint
url = 'https://api.example.com/data'

# Define the headers
headers = {
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Define the data payload
payload = {
    'key1': 'value1',
    'key2': 'value2'
}

# Make the POST request
response = requests.post(url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON data
    print(data)
else:
    print(f'Error: {response.status_code}, {response.text}')


    #Full example
    from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    
    # Here you can process the data (e.g., save to a database, etc.)
    # For demonstration, we'll just return the data received.
    
    return jsonify({
        'name': name,
        'age': age
    }), 200

if __name__ == '__main__':
    app.run(debug=True)



import requests

url = 'http://127.0.0.1:5000/submit'
data = {'name': 'John Doe', 'age': 30}

response = requests.post(url, json=data)
print(response.json())

