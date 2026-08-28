from random import randint

class Person:
    user_name = 'Антон'
    email = f'gaydamaka.anton52123@yandex.ru'
    password = f'12345Qwe'

class RandomData:
    user_name = 'Тест'
    email = f'test{randint(0, 999)}@yandex.ru'
    password = f'{randint(1000, 9999)}Qwe'