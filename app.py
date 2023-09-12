from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/credits')
def credits():
    return render_template('credits.html')

@app.route('/work')
def work():
    return render_template('work.html')

@app.route('/music')
def music():
    return render_template('music.html')
# ... add other routes

if __name__ == '__main__':
    app.run(debug=True)
