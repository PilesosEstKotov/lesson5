import os
import shutil
import platform
import random

def create_pack():
    pack_name = input("Введите название новой папки:\n")
    if not os.path.exists(pack_name):
        os.mkdir(pack_name)
        print(f"Папка '{pack_name}'создана")

def delete_file_and_pack():
    pack_or_file_name = input("Введите имя файла или папки для удаления: ")
    if os.path.isfile(pack_or_file_name):
        os.remove(pack_or_file_name)
        print(f"Файл '{pack_or_file_name}' удален.")
    elif os.path.isdir(pack_or_file_name):
        shutil.rmtree(pack_or_file_name)
        print(f"Папка '{pack_or_file_name}' удалена.")
    else:
        print(f"Файл или папка '{pack_or_file_name}' не найдены.")

def copy_file_and_pack():
    pack_or_file_name = input("Введите имя файла или папки, которую хотите скопировать: ")
    location = input("Введите место назначения: ")
    if os.path.isfile(pack_or_file_name):
        shutil.copy(pack_or_file_name, location)
        print(f"Файл '{pack_or_file_name}' скопирован в '{location}'.")
    elif os.path.isdir(pack_or_file_name):
        shutil.copytree(pack_or_file_name, location)
        print(f"Папка '{pack_or_file_name}' скопирована в '{location}'.")
    else:
        print(f"Файл или папка '{pack_or_file_name}' не найдены.")

def view_content():
    contents = os.listdir()
    for item in contents:
        print(item)

def view_packs_only():
    packs = [item for item in os.listdir() if os.path.isdir(item)]
    for pack in packs:
        print(pack)

def view_file_only():
    files = [item for item in os.listdir() if os.path.isfile(item)]
    for file in files:
        print(file)

def system_inf():
    print(f"Операционная система: {platform.system()}")
    print(f"Версия: {platform.version()}")
    print(f"Архитектура: {platform.architecture()[0]}")

def maker_inf():
    print("Автор программы: я")

def korean_game():
    famous_people = {
        "Михаил Горшенев (Князь)": "07.08.1973",
        "Андрей Князев (Княzz)": "13.02.1975",
        "Александр Балунов (Балу)": "15.07.1972",
        "Александр Щиголев (Щур)": "22.09.1970",
        "Яков Цветков (Яша)": "01.04.1974",
        "Андрей Лапин (Лапа)": "03.06.1971",
        "Дмитрий Гордеев (Грязный)": "10.11.1969",
        "Алексей Жидков (Жид)": "12.05.1974",
        "Павел Семёнов (Паук)": "09.03.1976",
        "Игорь Дорофеев (Гарик)": "18.11.1973"
    }

    def main():
        selected_people = random.sample(list(famous_people.keys()), 5)

        correct_answers = 0

        print("Угадайте дату рождения следующих участников группы 'Король и Шут':")
        for person in selected_people:
            user_answer = input(f"Когда родился {person}? (в формате день(dd).месяц(mm).год(yyyy)): \n")
            if user_answer == famous_people[person]:
                print("Правильно!")
                correct_answers += 1
            else:
                date_correct = famous_people[person].split(".")
                print(
                    f"Неправильно. Правильный ответ: {date_correct[0]} {num_to_month(date_correct[1])} {date_correct[2]} года.")

        print(f"\nИгра окончена. Правильных ответов: {correct_answers}. Неправильных ответов: {5 - correct_answers}.")
        if input("Хотите начать снова? (да/нет): ").lower() == "да":
            main()

    def num_to_month(num):
        months = {
            "01": "января",
            "02": "февраля",
            "03": "марта",
            "04": "апреля",
            "05": "мая",
            "06": "июня",
            "07": "июля",
            "08": "августа",
            "09": "сентября",
            "10": "октября",
            "11": "ноября",
            "12": "декабря"
        }
        return months.get(num, "неправильный месяц")

    if __name__ == "__main__":
        main()

def bank_account_info():
    account_balance = 0
    purchase_history = []

    while True:
        print('\n1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход\n')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            add_amount = float(input("Введите сумму для пополнения счета: "))
            account_balance += add_amount
            print(f"Счет пополнен на {add_amount}. Текущий баланс: {account_balance}")
        elif choice == '2':
            purchase_amount = float(input("Введите сумму покупки: "))
            if purchase_amount > account_balance:
                print("На счету недостаточно средств для совершения покупки.")
            else:
                purchase_name = input("Введите название покупки: ")
                account_balance -= purchase_amount
                purchase_history.append((purchase_name, purchase_amount))
                print(f"Покупка '{purchase_name}' на сумму {purchase_amount} успешно совершена.")
                print(f"Оставшийся баланс: {account_balance}")
        elif choice == '3':
            if not purchase_history:
                print("История покупок пуста.")
            else:
                print("История покупок:")
                for item, cost in purchase_history:
                    print(f"{item} - {cost}")
        elif choice == '4':
            print("До свидания!")
            break
        else:
            print('Неверный пункт меню, пожалуйста, попробуйте снова.')

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню')
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

def directory_change():
    new_path = input("Введите путь до новой рабочей директории: ")
    if os.path.exists(new_path):
        os.chdir(new_path)
        print(f"Рабочая директория изменена на {new_path}")
    else:
        print("Указанный путь не существует.")

print("""Меню:
1.создать папку
2.удалить (файл/папку)
3.копировать (файл/папку)
4.просмотр содержимого рабочей директории
5.посмотреть только папки
6.посмотреть только файлы
7.просмотр информации об операционной системе
8.создатель программы
9.играть в викторину
10.мой банковский счет
11.смена рабочей директории
12.выход\n""")

choice = input("Выберите один из вариантов:\n")

if choice == '1':
    create_pack()
elif choice == '2':
    delete_file_and_pack()
elif choice == '3':
    copy_file_and_pack()
elif choice == '4':
    view_content()
elif choice == '5':
    view_packs_only()
elif choice == '6':
    view_file_only()
elif choice == '7':
    system_inf()
elif choice == '8':
    maker_inf()
elif choice == '9':
    korean_game()
elif choice == '10':
    bank_account_info()
elif choice == '11':
    directory_change()
elif choice == '12':
    print("Ну всё тогда")
else:
    print("Неверный выбор. Выберите одно из чисел 1 - 12.")