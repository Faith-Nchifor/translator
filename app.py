from flask import Flask,request
from trans_model_infer import translate

app = Flask(__name__)

@app.route('/')
def hello_world():
    print(request.args)
    return 'Hello, World!'

# translate
@app.route('/translate') 
def get_file():
    text = request.args.get('sentence')
    return translate(text)

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=5000)