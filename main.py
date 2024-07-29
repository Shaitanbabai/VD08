# импортируем Flask и библиотеку Request
from flask import Flask, render_template, request
import requests

# импортируем объект класса Flask
app = Flask(__name__)


# формируем путь и методы GET и POST
@app.route('/', methods=['GET', 'POST'])
# создаем функцию с переменной weather, где мы будем сохранять погоду
def index():
    weather = None
# формируем условия для проверки метода. Форму мы пока не создавали, n/
# но нам из неё необходимо будет взять только город.
    if request.method == 'POST':  # этот определенный город мы будем брать для запроса API
        city = request.form['city']  # создаем переменную для вызова города
        weather = get_weather(city)  # создаем переменную для сохранения результата
    return render_template("index.html", weather=weather)  # передаем переменную weather ф форму html


# в функции прописываем город, который мы будем вводить в форме
def get_weather(city):
    api_key = "332abe57c6bdac6e4098f87ef75d2024"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    # Адрес, по которому мы будем отправлять запрос. Не забываем указывать f строку.
    response = requests.get(url)  # для получения результата нам понадобится модуль requests
    return response.json()  # прописываем формат возврата результата


if __name__ == "__main__":
    app.run(debug=True)
