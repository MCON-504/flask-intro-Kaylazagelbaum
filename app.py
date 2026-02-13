from flask import Flask, current_app, request, jsonify

app = Flask(__name__)
@app.route('/')
def route_a():
    return "<h1>Welcome to My Flask API!</h1>"


@app.route('/about')
def route_b():
    return jsonify({"name": "Kayla Zagelbaum", "course": "MCON504-Backend Web Development", "semester": "Spring 2025"})

@app.route('/greet/<name>')
def greet(name):
    print(request)
    return f"<p>Hello {name}! Welcome to Flask</p>"

@app.route("/calculate")
def calculate():
    print(request)
    operation = request.args.get["operation"]
    operand1 = request.args["num1"]
    operand2 = request.args["num2"]
    if operation == "add":
        result = int(operand1) + int(operand2)
        return f"<p>result = '{result}'</p>"

@app.route("/echo:", methods=["POST"])
def echo():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    data["echoed"] = True

    return jsonify(data)

@app.route("/status/<int:code>")
def status(code):
    message = f"This is a {code} error"
    return message, code

if __name__ == '__main__':
    app.run(debug=True)