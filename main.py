from flask import Flask,jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    result = None
    numberA = None
    numberB = None
    operation = None
    status = 200

    if 'numberA' in request.args and 'numberB' in request.args and 'operation' in request.args:
        try:
            numberA = float(request.args['numberA'])
            numberB = float(request.args['numberB'])
            operation = request.args['operation']

            if operation == 'add':
                result = numberA + numberB
            elif operation == 'minus':
                result = numberA - numberB
            elif operation == 'multiply':
                result = numberA * numberB
            elif operation == 'divide':
                if numberB == 0:
                    result = "Error: Cannot divide by zero"
                    status = 400
                else:
                    result = numberA / numberB
        except ValueError:
            result = "Invalid input"
            status = 400

    return render_template('index.html', result=result, numberA=numberA, numberB=numberB, operation=operation, status=status)


# API route for URL-based operations
@app.route('/<operation>/<numberA>/<numberB>')
def calculate(operation, numberA, numberB):
    try:
        numberA = float(numberA)
        numberB = float(numberB)

        if operation == 'add':
            result = numberA + numberB
        elif operation == 'minus':
            result = numberA - numberB
        elif operation == 'multiply':
            result = numberA * numberB
        elif operation == 'divide':
            if numberB == 0:
                return jsonify({'status': 400, 'message': 'Error: Cannot divide by zero'})
            result = numberA / numberB
        else:
            return jsonify({'status': 400, 'message': 'Invalid operation'})

        return jsonify({'status': 200, 'result': result})

    except ValueError:
        return jsonify({'status': 400, 'message': 'Invalid numbers provided'})


if __name__ == '__main__':
    app.run(debug=True)
