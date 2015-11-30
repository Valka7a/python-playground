from flask import request

@app.route('/login', methods = ['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
           return log_the_user_in(request.form['username'])
       else:
           error = 'Invalid username/password'
   # the code below is executed if the request method
   # was GET or the credentials were invalid
   return render_template('login.html', error = error)


# To access parameters submitted in the URL(?key=value) you can use the args
# attribute:
searchword = request.args.get('key', '')

"""
We recommend accessing URL parameters with get or by catching the KeyError
because users might change the URL and presenting them a 400 bad request page
in that case is not user friendly.
"""
