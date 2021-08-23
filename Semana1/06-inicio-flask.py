from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    print("Me llamaron !!!")
    return {
        "message": "Holaaaaa..."
    }

app.run(debug=True)