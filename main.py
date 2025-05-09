from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, world!"}), 200


@app.route("/users", methods=["GET"])
def users():
    return jsonify({"badyss": "yoyoyo"}), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9900)
