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

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/music')
def music():
    return render_template('music.html')
# ... add other routes

if __name__ == '__main__':
    app.run(debug=True)
