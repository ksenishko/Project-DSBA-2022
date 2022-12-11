from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='./templates')

@app.route('/')
def html_template():
    return render_template("index.html")

@app.route('/example')
def html_template3():
    return render_template("plot_example.html")

@app.route('/all_plots')
def html_template2():
    return render_template("all_plots.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4999, debug=True)
