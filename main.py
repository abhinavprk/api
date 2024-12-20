from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/text-info', methods=['POST'])
def text_info():
    data = request.get_json()
    response = {
        "message": "Received the data!",
        "data": data
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
