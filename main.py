from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

@app.route('/')
def sessions():
	return 'hello world'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)