from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        name = request.form["fname"]
        birthdate = request.form["age"]
        birthyear = int(birthdate.split("-")[0])
        edad = 2024 - birthyear
        return jsonify(name=name, agee=edad)
    return render_template("sample.html")

if __name__ == "__main__":
    app.run(debug=True)
