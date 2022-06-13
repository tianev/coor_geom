from flask import Flask, render_template, url_for, request, flash


app = Flask(__name__)
app.config['SECRET_KEY'] ='ksjvjdbvre4698g78ge7fee'

menu = [{"name": "Теория", "url": "Theory"},
        {"name": "Задачи", "url": "Tasks"},
        {"name": "Обратная связь", "url": "contact"}
]


@app.route('/')
@app.route('/home')
def index():
    print(url_for('index'))
    return render_template("index.html", menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template("about.html", title="О сайте", menu="menu")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено')
        else:
            flash('Ошибка отправки')

    return render_template('contact.html', title="Обратная связь", menu=menu)

# with app.test_request_context():
#     print(url_for('index'))


if __name__=="__main__":
    app.run(debug=True)
