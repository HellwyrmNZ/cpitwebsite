from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html', content="Suck a man's dick")

@app.route('/dicksucking/')
def dick_sucking():
    return render_template('dick.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)