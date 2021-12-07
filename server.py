from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
@app.route('/')
def index():
    if 'views' in session:
        session['views'] += 1
    else:
        session['views'] = 0
    return render_template('index.html', viewCount=session['views'])

@app.route('/destroy_session')
def reset():
    session['views'] = 0
    return redirect('/')

app.run(debug=True)
