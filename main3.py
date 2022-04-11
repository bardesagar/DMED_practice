from flask import Flask

app = Flask(__name__) #constructor of the flask

@app.route('/')
def base_route():
    return "Welcome to Praxis"

@app.route("/my_name")
def print_name():
    return "Happy Leaning in Praxis BLR"

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8000)