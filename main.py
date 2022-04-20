from flask import Flask,request #import flask
from flasgger import Swagger ### 

app = Flask(__name__) #constructor of the flask
Swagger(app)


@app.route('/')
def base_route():
    return "Welcome to Praxis"

@app.route("/my_name/<name>")
def print_name(name):
    return f"Happy Leaning {name} in Praxis BLR" 

@app.route("/hello", methods = ["GET"])
def hello():

    """"Lets try the Swagger from Flasgger
    ---
    parameters: 
        - name: StudnetName
          in: query
          type: string
          required: true
        - name: RollNo
          in: query
          type: string
          required: true
    responses: 
        200: 
            description: The result is
    """
    try:
        stu_name =  request.args.get("StudnetName")
        numb = request.args.get("RollNo")
        return f"Student name is {stu_name} and Roll no is {numb}",201
    except Exception as e:
        return f"Error occured with message : {e}",401
    

if __name__ == "__main__":
    app.run(debug=True )
