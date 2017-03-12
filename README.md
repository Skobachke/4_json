# Prettify JSON

Эта программа была написана для представления данных из JSON файла в удобном виде.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash

$ python pprint_json.py 1.json
[
    {
        "Cells": {
            "Address": "улица Академика Павлова, дом 10", 
            "AdmArea": "Западный административный округ", 
            "ClarificationOfWorkingHours": null, 
            "District": "район Кунцево", 
            "IsNetObject": "да", 
            "Name": "Ароматный Мир", 
            "OperatingCompany": "Ароматный Мир", 
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ], 
            "TypeService": "реализация продовольственных товаров", 
            "WorkingHours": [
                {
                    "DayOfWeek": "понедельник", 
                    "Hours": "09:30-22:30"
                }, 
                {
                    "DayOfWeek": "вторник", 
                    "Hours": "09:30-22:30"
                }, 
                {
                    "DayOfWeek": "среда", 
                    "Hours": "09:30-22:30"
                }, 
                {
                    "DayOfWeek": "четверг", 
                    "Hours": "09:30-22:30"
                }, 
                {
                    "DayOfWeek": "пятница", 
                    "Hours": "09:30-22:30"
                }, 
                {
                    "DayOfWeek": "суббота", 
                    "Hours": "09:30-22:30"
                }, 
                {
                    "DayOfWeek": "воскресенье", 
                    "Hours": "09:30-22:30"
                }
            ], 
            "geoData": {
                "coordinates": [
                    37.39703804817934, 
                    55.740999719549094
                ], 
                "type": "Point"
            }, 
            "global_id": 14371450
        }, 
        "Id": "79742784-9ef3-4543-bc98-a219a8903c18", 
        "Number": 1
    }, 

```

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
