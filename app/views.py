from app import app

@app.route('/test')
def test():
	return 'The rummikub_solver app is running.'

@app.route('/')
def index():
	return "Hello, World!"
