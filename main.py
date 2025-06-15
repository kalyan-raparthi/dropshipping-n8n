from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') 


@app.route('/track')
def track():
    return render_template('track.html') 

@app.route('/track_s')
def seller():
    return render_template('track-s.html')

@app.route('/ror')
def seller():
    return render_template('ror.html')


if __name__ == '__main__':
    app.run(debug=True)