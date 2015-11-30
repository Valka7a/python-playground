import web

urls = (
	'/', 'Index',
	'/about', 'About'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index:
	def GET(self):
		print web.input()
		greeting = "Hello World"
		return render.index(greeting = greeting)

class About:
	def GET(self):
		content = "WaT"
		return render.about(content = content)

if __name__ == "__main__":
	app.run()