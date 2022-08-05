import json

def load_candidates(file_name):
    """Загружает данные из файла.
    Возращает py list"""
    with open(file_name, encoding='utf-8') as json_file:
        py_file = json.load(json_file)
        return py_file

def get_all(list_of_dicts):
    """Выводит на экран всех кандидатов
    в виде одной строки"""
    total_string = '<pre>'
    for candidat in list_of_dicts:

        total_string +=(f'<p>Имя кандидата: {candidat["name"]}<br>')
        total_string +=(f'Позиция кандидата: {candidat["position"]}<br>')
        total_string +=(f'Скиллсет кандидата: {candidat["skills"]}</p>')
    total_string += '</pre>'
    return total_string

def get_by_pk(list_of_dicts, pk):

    """Возращает данные кандидата по pk
    в виде одной строки"""
    total_string = ''
    for candidat in list_of_dicts:
        if candidat['pk'] == pk:
            total_string += (f'<img src="{candidat["picture"]}">')
            total_string += (f'<pre><p>Имя кандидата: {candidat["name"]}<br>')
            total_string += (f'Позиция кандидата: {candidat["position"]}<br>')
            total_string += (f'Скиллсет кандидата: {candidat["skills"]}</p></pre>')


    return total_string

def get_by_skill(list_of_dicts, skill):
    """Возращает кандидатов, у которых есть
    определенный скилл"""
    total_string = '<pre>'
    for candidat in list_of_dicts:
        if skill.lower().strip() in candidat['skills'].lower():
            total_string += (f'<p>Имя кандидата: {candidat["name"]}<br>')
            total_string += (f'Позиция кандидата: {candidat["position"]}<br>')
            total_string += (f'Скиллсет кандидата: {candidat["skills"]}</p>')

    return total_string + '</pre>'




