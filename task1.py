import pickle

class CountryCapitalDictionary:
    def __init__(self, filename='countries.dat'):
        self.data = {}
        self.filename = filename
    
    def add(self, country, capital):
        self.data[country] = capital
        print(f'Добавлено: {country} - {capital}')
    
    def remove(self, country):
        if country in self.data:
            del self.data[country]
            print(f'Удалено: {country}')
        else:
            print(f'Ошибка: Страна {country} не найдена')
    
    def find(self, country):
        return self.data.get(country, 'Страна не найдена')
    
    def edit(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital
            print(f'Изменено: {country} - {new_capital}')
        else:
            print(f'Ошибка: Страна {country} не найдена')
    
    def save(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.data, f)
        print('Данные сохранены')
    
    def load(self):
        try:
            with open(self.filename, 'rb') as f:
                self.data = pickle.load(f)
            print('Данные загружены')
            return True
        except FileNotFoundError:
            print('Файл не найден. Будет создан новый словарь.')
            return False
    
    def show_all(self):
        print("\nСписок стран и столиц:")
        for country, capital in self.data.items():
            print(f"{country}: {capital}")
        print()



if __name__ == "__main__":
    db = CountryCapitalDictionary()
    
    db.load()
    
    while True:
        print("\n1. Добавить страну и столицу")
        print("2. Удалить страну")
        print("3. Найти столицу")
        print("4. Изменить столицу")
        print("5. Показать все данные")
        print("6. Сохранить данные")
        print("7. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            country = input("Введите название страны: ")
            capital = input("Введите название столицы: ")
            db.add(country, capital)
        elif choice == '2':
            country = input("Введите название страны для удаления: ")
            db.remove(country)
        elif choice == '3':
            country = input("Введите название страны для поиска: ")
            print(f"Столица: {db.find(country)}")
        elif choice == '4':
            country = input("Введите название страны: ")
            capital = input("Введите новую столицу: ")
            db.edit(country, capital)
        elif choice == '5':
            db.show_all()
        elif choice == '6':
            db.save()
        elif choice == '7':
            db.save()
            break
        else:
            print("Неверный ввод. Попробуйте снова.")