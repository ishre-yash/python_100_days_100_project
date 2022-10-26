from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(template_name_or_list="index.html")

app.run(debug=True)