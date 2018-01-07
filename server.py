from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'numbers are great'

# root route
@app.route('/')
def index():
    print session
    if "response" in session:
        if session["response"] == "correct":
            show = "correct"
        elif session["response"] == "high":
            show = "high"
        elif session["response"] == "low":
            show = "low"
        elif session["response"] == "start":
            show = "start"
    else:
        show = "start"
    return render_template('index.html', response = show)

# guess route
@app.route('/guess', methods = ['POST'])
def user_guess():
    session["guess"] = int(request.form['guess'])
    import random
    if "randomNum" in session:
        if session["randomNum"] == None:
            session["randomNum"] = random.randrange(0, 101)
    else:
        session["randomNum"] = random.randrange(0, 101)
    if session["randomNum"] == session.get("guess"):
        session["response"] = "correct"
    elif session.get("guess") > session['randomNum']:
        session["response"] = "high"
    elif session.get("guess") < session['randomNum']:
        session["response"] = "low"
    print str(session['randomNum']) + " was the number!"
    return redirect('/')

@app.route('/reset')
def reset():
    session["response"] = "start"
    session["randomNum"] = None
    return redirect('/')

app.run(debug = True)
