from flask import Flask, request

app = Flask(__name__)

saved_data = ""

@app.route('/')
def index():
    return open("index.html", "r").read()

@app.route('/submit', methods=['POST'])
def submit():
    global saved_data
    data = request.json['data']
    saved_data = data
    return "Data submitted successfully!"

@app.route('/get_data')
def get_data():
    return saved_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
