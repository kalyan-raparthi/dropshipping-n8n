from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new')
def home():
    return render_template('new.html')


@app.route('/track')
def track():
    return render_template('track.html') 

@app.route('/track_s')
def seller_track():
    return render_template('track-s.html')

@app.route('/ror')
def seller_ror():
    return render_template('ror.html')

@app.route('/cancel')
def cancel():
    return render_template('cancel.html')

if __name__ == '__main__':
    app.run(debug=True)