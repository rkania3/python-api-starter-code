from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    msg = {
        "page": "home" 
    }

    return jsonify(data=msg, meta={"status": "ok"})

if __name__ == '__main__':
    app.run()
