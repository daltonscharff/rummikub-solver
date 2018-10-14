from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

@app.route('/test')
def test():
	return 'The rummikub_solver app is running...'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
