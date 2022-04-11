from flask import Flask, request
from flasgger import Swagger
import pickle
from sklearn.linear_model import LogisticRegression


app = Flask(__name__) #constructor of the flask
Swagger(app)

pickled_model_file = open('pickle_iris_model.pkl','rb')
classifier = pickle.load(pickled_model_file)

@app.route('/')
def home():
    return 'Welcome to iris classifier'

@app.route('/predict')
def predict_flower():
    
    """Lets try the Swagger from Flasgger
    ---
    parameters: 
        - name: sepal_length
          in: query
          type: number
          required: true
        - name: sepal_width
          in: query
          type: number
          required: true
        - name: petal_length
          in: query
          type: number
          required: true
        - name: petal_width
          in: query
          type: number
          required: true
    responses: 
        200: 
            description: The result is
    """
    sl = request.args.get('sepal_length')
    sw = request.args.get('sepal_width')
    pl = request.args.get('petal_length')
    pw = request.args.get('petal_width')

    result = classifier.predict([[sl,sw,pl,pw]])


    return f'This is {result}'

if __name__ == "__main__":
    app.run(debug = True)


