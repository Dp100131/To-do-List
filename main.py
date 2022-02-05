from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

todos = ['Comprar café.', 'Enviar solicitud de compra.', 'Entregar producto.']

@app.errorhandler(404)
def not_fount(error):
    
    return render_template('404.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response

@app.route('/hello')
def hello():

    user_ip = request.cookies.get('user_ip') 

    contex = {

        'user_ip': user_ip, 
        'todos': todos
        
    }
    
    return render_template('hello.html', **contex)



if __name__ == '__main__':

    app.run(debug=True)