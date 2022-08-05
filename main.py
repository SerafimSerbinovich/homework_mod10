# импортируем фласк и вспомогательные функции
from flask import Flask
import utils

# создаем экземпляр класса
app = Flask(__name__)

# получаем список словарей с данными кандидатов
candidates = utils.load_candidates('candidates.json')

# создаем представление для роута "/"
@app.route('/')
def main_page():
    return f'{utils.get_all(candidates)}'


# создаем представление для роута "/candidates/<x>/"
@app.route('/candidates/<x>/')
def page_profile(x):
    return f'{utils.get_by_pk(candidates, int(x))}'


# создаем представление для роута "/skills/<x>/"
@app.route('/skills/<x>/')
def slill_profile(x):
    return f'{utils.get_by_skill(candidates, x)}'

app.run()