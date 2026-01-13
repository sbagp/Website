from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/cinematography')
def cinematography():
    return render_template('sitio/cinematography.html')

@app.route('/commercial')
def commercial():
    return render_template('sitio/commercial.html')

@app.route('/expo')
def expo():
    return render_template('sitio/expo.html')

@app.route('/contact')
def contact():
    return render_template('sitio/contact.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    
