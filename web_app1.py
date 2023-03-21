from app import main
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')

def display():
    days, hours, minutes, seconds = main()
    
    return render_template('layout.html', days=days, hours=hours, minutes=minutes, seconds=seconds)


if __name__ == '__main__':
    app.run(debug=True, port=3000)