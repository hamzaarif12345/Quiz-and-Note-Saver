from flask import render_template
from website import create_app

@app.route('/hello/<name>')
def hello(name,github,linkedin,mail,number,address ):
    return render_template('portfolio.html', name=name,github=github,linkedin=linkedin,mail=mail,number=number,address=address, )
    

