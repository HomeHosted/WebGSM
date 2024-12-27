from flask import Flask, render_template
import os

app = Flask(__name__, template_folder=os.path.abspath(os.path.join('app', 'frontend', 'templates')))

@app.route("/")
def index():
    # Render the index.html file from the templates folder
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8082)
