from flask import Flask, render_template, redirect, url_for

import datetime

app = Flask(__name__)


# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров. Например, создать страницы
# «Одежда», «Обувь» и «Куртка», используя базовый шаблон.


@app.route('/')
def index():
    return render_template('base.html', utc_dt=datetime.datetime.utcnow())


@app.route('/clothes/')
def clothes():
    return render_template('clothes.html', utc_dt=datetime.datetime.utcnow())


@app.route('/shoes/')
def shoes():
    return render_template('shoes.html', utc_dt=datetime.datetime.utcnow())


@app.route('/jacket/')
def jacket():
    return render_template('jacket.html', utc_dt=datetime.datetime.utcnow())


if __name__ == '__main__':
    app.run(debug=True, port=2020)
