from flask import Flask, jsonify, request
from telegram_parser import get_jokes

app = Flask(__name__)

@app.route('/api/jokes', methods=['GET'])
def jokes():
    limit = int(request.args.get('limit', 5))
    return jsonify(get_jokes(limit))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
