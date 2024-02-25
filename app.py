from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flocate')
def flocator():
    return render_template('flocator.html')

@app.route('/flocate')
def update():
    return render_template('update.html')

if __name__ == '__main__':
    app.run(debug=True)