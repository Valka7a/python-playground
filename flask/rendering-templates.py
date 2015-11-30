from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
# if request http://mysite/hello/  - will return Hello World
# if request http://mysite/hello/valyo - will return Hello valyo
# see template/hello.html 
def hello(name = None):
    return render_template('hello.html', name = name)


if __name__ == '__main__':
    app.debug = True
    app.run()
