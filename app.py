from flask import Flask, render_template, url_for
app=Flask(__name__)
@app.route('/home')
def show_home():
    return render_template('index.html')
app.run(debug=True)
