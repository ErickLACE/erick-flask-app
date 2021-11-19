from flask import Flask 

app = Flask(__name__) #name spaces

@app.route('/')
def index():
    return "Hola mundo mi primer app en Flask..."


app.run(debug=True, port=7000, host='0.0.0.0' ) # show errors, port and host



