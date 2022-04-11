from flask import Flask, request

app = Flask(__name__) #constructor of the flask

@app.route('/')
def base_route():
    return "Welcome to Praxis"

@app.route("/my_name/<name>")
def print_name(name):
    return f"Happy Leaning {name} in Praxis BLR" 

@app.route("/hello", methods = ["GET","POST"])
def hello():
    stu_name = request.args.get("StudentName")
    numb = request.args.get("RollNumber")
    return f"Studnet name is {stu_name} and Roll number is {numb}"

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8000, debug = True)


    ##http://192.168.1.9:8000/hello?StudentName=Sagar&RollNumber=28 