from datetime import datetime, timedelta

# Список користувачів з їхніми датами народження
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Smith1", "birthday": "1990.03.05"},
    {"name": "Jane Smith1", "birthday": "1990.03.07"},
    {"name": "Jane Smith1", "birthday": "1990.03.10"},
]

def prepared_users(users):
    # Список підготовлених користувачів
    formated_users = []
    # Ітерація по кожному користувачеві зі списку
    for user in users:
        try:
            # Парсимо дату народження
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
            # Додаємо користувача з підготовленою датою народження
            formated_users.append({"name": user['name'], 'birthday': birthday})
        except ValueError:
            # Виводимо повідомлення про помилку
           print(f'Некоректна дата народження для користувача {user["name"]}')
    return formated_users


def find_next_weekday(d, weekday: int):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + timedelta(days=days_ahead)


def get_upcoming_birthdays(prepared_users):
    # Список майбутніх днів народження
    upcoming_birthdays = []
    # Кількість днів для перевірки на наближені дні народження
    days = 7
    # Поточна дата
    today = datetime.today().date()
    # Ітерація по підготовленим користувачам
    for user in prepared_users:
        # Заміна року на поточний для дня народження цього року
        birthday_this_year = user["birthday"].replace(year=today.year)

        # Якщо дата народження вже пройшла цього року
    if birthday_this_year < today:
        # Переносимо наступний рік
        birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Якщо день народження в межах вказаного періоду
    if 0 <= (birthday_this_year - today).days <= days:
        # Якщо день народження випадає на суботу або неділю
        if birthday_this_year.weekday() >= 5:
            # Знаходимо наступний понеділок
            birthday_this_year = find_next_weekday(birthday_this_year, 0)

            # Форматуємо дату у рядок
        congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')
        # Додаємо дані про майбутній день народження
        upcoming_birthdays.append({
            "name": user["name"],
            "congratulation_date": congratulation_date_str
        })
    return upcoming_birthdays

formatted_users = prepared_users(users)
upcoming_birthdays = get_upcoming_birthdays(formatted_users)
print(upcoming_birthdays)