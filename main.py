from flask import Flask, render_template, request

app = Flask(__name__)

html = """
<h1> Моя первая HTML страница</h1>
<p> Привет , Мир! </p>
<h1> Моя вторая HTML страница</h1>  
<p> Пока, Мир! </p
"""


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/about')
def about():
    return 'about.html'


@app.route('/sum/<int:num1>/<int:num2>')
def sum_num(num1, num2):
    s = num1 + num2
    return str(s)


@app.route('/len/<text>')
def str_len(text):
    return str(len(text))


@app.route('/web')
def web():
    return html


_users = [
    {'name': 'Ivan', 'Last_name': 'Ivanov', 'age': '444', 'average_mark': '4.8', },
    {'name': 'Vanya', 'Last_name': 'Petrov', 'age': '344', 'average_mark': '4.8', },
    {'name': 'Ivan', 'Last_name': 'Ivanov', 'age': '15', 'average_mark': '4.8', },
    {'name': 'Vanya', 'Last_name': 'Petrov', 'age': '440', 'average_mark': '4.8', }
]

_news = [{
    'id': 1,
    'title': 'Новость 1',
    'text': 'Текст новости 1',
    'date': '2020-01-01'
}, {
    'id': 2,
    'title': 'Новость 2',
    'text': 'Текст новости 2',
    'date': '2020-01-02'
}]


@app.route('/users/')
def table():
    return render_template('users.html', users=_users)


@app.route('/news')
def news():
    return render_template('news.html', news=_news)


if __name__ == '__main__':
    app.run(debug=True)
