from models import Car
from mixins import JsonMixin,  CreateMixin, ReadMixin, UpdateMixin, DeleteMixin

class Crud(JsonMixin, CreateMixin, ReadMixin, UpdateMixin, DeleteMixin):
    _file_name = 'db.json'
    _model = Car

    def help(self):
        print(
            """
            create - создание записи
            list - список записей
            details - получения записи 
            update - обновление записи
            delete - удаления записи
            help - список команд
            quit - выход
            """
        )


    def start(self):
        commands = {
            'create': self.create,
            'list': self.list,
            'details': self.get_car_by_id,
            'update': self.update,
            'delete': self.delete,
            'help': self.help
        }
        while True:
            try:
                command = input('Введите команду или help для списка команд ').lower().strip()
                if command in commands:
                    commands[command]()
                elif command == 'quit':
                    print('Выход из программы')
                    break
                else:
                    print('Нет такой команды')
            except KeyboardInterrupt:
                break
            except:
                print('Произошла ошибка')

car1 = Crud()

car1.start()


    

    