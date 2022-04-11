from flask import Flask

app = Flask(__name__) #constructor of the flask

@app.route('/')
def base_route():
    return "Welcome to Praxis"


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8000)