import json


def load_data(filepath):
    with open(filepath, 'r') as js:  # открываем файл на чтение
        python_data = json.load(js) # загружаем из файла данные в словарь
        js.close()  # Закрываем файл
        return python_data


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4))


if __name__ == '__main__':
    json_file = input('Введите  путь до файла: ')
    data_from_json = load_data(json_file)
    pretty_print_json(data_from_json)