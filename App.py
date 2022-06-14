from flask import Flask, render_template, url_for, request, flash


app = Flask(__name__)
app.config['SECRET_KEY'] ='ksjvjdbvre4698g78ge7fee'

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
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено')
        else:
            flash('Ошибка отправки')

    return render_template('contact.html', menu=menu)

# with app.test_request_context():
#     print(url_for('index'))


if __name__=="__main__":
    app.run(debug=True)
