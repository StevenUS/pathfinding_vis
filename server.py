from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Run algorithm
    # Send data structure
    frames = [{ "test": "testing" }]
    return render_template('index.html', frames=frames)

app.run(port=3000)