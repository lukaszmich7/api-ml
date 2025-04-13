from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    a = float(request.args.get('num1', 0))
    b = float(request.args.get('num2', 0))

    result = 1 if (a + b) > 5.8 else 0

    response = {
        "features": {"num1": a, "num2": b},
        "prediction": result
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
