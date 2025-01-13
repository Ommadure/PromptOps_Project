from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data.get('operation')
    num1 = data.get('num1')
    num2 = data.get('num2')

    try:
        num1, num2 = float(num1), float(num2)
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Division by zero is not allowed'}), 400
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operation'}), 400
        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
