# def dossier(name, surname, year, city, email, phone):
#    print(f'Пользователь {name} {surname},', end=' ')
#    print(f'родился в {year} году,', end=' ')
#    print(f'проживает в городе {city},', end=' ')
#    print(f'Контактные данные: email {email}, телефон: {phone}')

# usr_name = input('Введите имя: ')
# usr_sname = input('Введите фамилию: ')
# usr_year = input('Введите год рождения: ')
# usr_city = input('Введите город: ')
# usr_email = input('Введите email: ')
# usr_phone = input('Введите номер телефона: ')

# dossier(name=usr_name, surname=usr_sname, year=usr_year, city=usr_city, email=usr_email, phone=usr_phone)

def dossier(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone, sep=' ')


dossier(name='Vasya', surname='Pupkin', year='1932', city='Karaganda', email='vasya@pupkin.io', phone='123 45 67')