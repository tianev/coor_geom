from flask import Flask, render_template, url_for, request, flash, session, redirect, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coorgeom.db'
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r' % self.id


menu = [{"name": "Главная", "url": "home"},
        {"name": "Теория", "url": "theory"},
        {"name": "Задачи", "url": "task"},
        {"name": "Обратная связь", "url": "contact"},
        {"name": "О сайте", "url": "about"}
]


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html", menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template("about.html", menu=menu)

@app.route('/theory')
def theory():
    return render_template("theory.html", menu=menu)

@app.route('/task')
def task():
    return render_template("task.html", menu=menu)

@app.route("/contact", methods=["POST", "GET"])
def contact():
    # print(request.form)
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='warning')

    return render_template('contact.html', title="Обратная связь", menu=menu)


@app.route("/profile/username")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(404)

    return f"Профиль пользователя: {username}"


@app.route("/login", methods=["POST", "GET"])
def login():
    print(request.form)
    print(session)
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "coor@geom.com" and request.form['psw'] == "123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title='Авторизация', menu=menu)



@app.errorhandler(404)
def pageNotFount(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu), 404

# with app.test_request_context():
#     print(url_for('index'))


if __name__=="__main__":
    app.run(debug=True)
