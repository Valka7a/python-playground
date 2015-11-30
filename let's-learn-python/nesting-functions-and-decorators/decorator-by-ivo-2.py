def route(route):
    current_route = '/home'

    def check_route(callback):
        if current_route == route:
            callback()

    return check_route

@route('/home')
def homepage():
    print 'homepage stuff here'
