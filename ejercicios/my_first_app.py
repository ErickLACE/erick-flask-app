from flask import Flask 
from flask import request

app = Flask(__name__) #name spaces

@app.route('/')
@app.route('/<name>')
def index(name='Nombre', lastname='lastname'):
    name = request.args.get('name', name) # using query .get()
    lastname = request.args.get('lastname', lastname)    
    return "Hola {} {}" .format(name, lastname)


@app.route('/calculator/<int:num1>/<int:num2>')
def calculator(num1,num2):
    sum = '{} + {} = {}'.format(num1, num2, int(num1) + int(num2))
    return sum
app.run(debug=True, port=7000, host='0.0.0.0' ) # show errors, port and host



