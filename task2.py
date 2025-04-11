import pickle
import os

class MusicCatalog:
    def __init__(self, filename='music_catalog.dat'):
        self.catalog = {}
        self.filename = filename
        self.load()
    
    def add_artist(self, artist, album):
        if artist in self.catalog:
            if album not in self.catalog[artist]:
                self.catalog[artist].append(album)
                print(f'Добавлен альбом "{album}" для {artist}')
            else:
                print(f'Альбом "{album}" уже существует для {artist}')
        else:
            self.catalog[artist] = [album]
            print(f'Добавлен новый исполнитель {artist} с альбомом "{album}"')
    
    def remove_artist(self, artist):
        if artist in self.catalog:
            del self.catalog[artist]
            print(f'Исполнитель {artist} и все его альбомы удалены')
        else:
            print(f'Исполнитель {artist} не найден')
    
    def remove_album(self, artist, album):
        if artist in self.catalog:
            if album in self.catalog[artist]:
                self.catalog[artist].remove(album)
                print(f'Альбом "{album}" удален у {artist}')
                if not self.catalog[artist]:
                    del self.catalog[artist]
                    print(f'Исполнитель {artist} удален, так как больше нет альбомов')
            else:
                print(f'Альбом "{album}" не найден у {artist}')
        else:
            print(f'Исполнитель {artist} не найден')
    
    def find_artist(self, artist):
        return self.catalog.get(artist, None)
    
    def find_album(self, album):
        return [artist for artist, albums in self.catalog.items() if album in albums]
    
    def edit_artist(self, old_name, new_name):
        if old_name in self.catalog:
            self.catalog[new_name] = self.catalog.pop(old_name)
            print(f'Исполнитель {old_name} переименован в {new_name}')
        else:
            print(f'Исполнитель {old_name} не найден')
    
    def edit_album(self, artist, old_album, new_album):
        if artist in self.catalog:
            if old_album in self.catalog[artist]:
                index = self.catalog[artist].index(old_album)
                self.catalog[artist][index] = new_album
                print(f'Альбом "{old_album}" изменен на "{new_album}" для {artist}')
            else:
                print(f'Альбом "{old_album}" не найден у {artist}')
        else:
            print(f'Исполнитель {artist} не найден')
    
    def save(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.catalog, f)
        print(f'Каталог сохранен в {self.filename}')
    
    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                self.catalog = pickle.load(f)
            print(f'Каталог загружен из {self.filename}')
        else:
            print('Файл каталога не найден. Создан новый каталог.')
    
    def show_all(self):
        print("\n=== МУЗЫКАЛЬНЫЙ КАТАЛОГ ===")
        for artist, albums in self.catalog.items():
            print(f"\nИсполнитель: {artist}")
            print("Альбомы:")
            for album in albums:
                print(f"  - {album}")
        print("\n" + "="*30 + "\n")


def main():
    catalog = MusicCatalog()
    
    while True:
        print("\n1. Добавить исполнителя/альбом")
        print("2. Удалить исполнителя")
        print("3. Удалить альбом")
        print("4. Найти альбомы по исполнителю")
        print("5. Найти исполнителей по альбому")
        print("6. Изменить имя исполнителя")
        print("7. Изменить название альбома")
        print("8. Показать весь каталог")
        print("9. Сохранить каталог")
        print("0. Выйти")
        
        choice = input("\nВыберите действие: ")
        
        if choice == '1':
            artist = input("Введите имя исполнителя: ")
            album = input("Введите название альбома: ")
            catalog.add_artist(artist, album)
        elif choice == '2':
            artist = input("Введите имя исполнителя для удаления: ")
            catalog.remove_artist(artist)
        elif choice == '3':
            artist = input("Введите имя исполнителя: ")
            album = input("Введите название альбома для удаления: ")
            catalog.remove_album(artist, album)
        elif choice == '4':
            artist = input("Введите имя исполнителя: ")
            albums = catalog.find_artist(artist)
            if albums:
                print(f"\nАльбомы {artist}:")
                for album in albums:
                    print(f"  - {album}")
            else:
                print("Исполнитель не найден")
        elif choice == '5':
            album = input("Введите название альбома: ")
            artists = catalog.find_album(album)
            if artists:
                print(f"\nАльбом '{album}' есть у следующих исполнителей:")
                for artist in artists:
                    print(f"  - {artist}")
            else:
                print("Альбом не найден")
        elif choice == '6':
            old_name = input("Введите текущее имя исполнителя: ")
            new_name = input("Введите новое имя исполнителя: ")
            catalog.edit_artist(old_name, new_name)
        elif choice == '7':
            artist = input("Введите имя исполнителя: ")
            old_album = input("Введите текущее название альбома: ")
            new_album = input("Введите новое название альбома: ")
            catalog.edit_album(artist, old_album, new_album)
        elif choice == '8':
            catalog.show_all()
        elif choice == '9':
            catalog.save()
        elif choice == '0':
            catalog.save()
            print("Выход из программы")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()