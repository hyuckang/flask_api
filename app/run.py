from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def hello_server():
    return render_template('index.html')

@app.route("/hello")
def hello():
    return jsonify({"response" : "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1234, debug=True)