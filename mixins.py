import json


class JsonMixin:
    def get_db_content(self):
        try:
            with open(self._file_name, 'r') as file:
                return json.load(file)
        except json.decoder.JSONDecodeError:
            return {'cars': [], 'counter': 0}

    def write_to_db(self, data):
        with open(self._file_name, 'w') as file:
            json.dump(data, file, indent=4)


class CreateMixin:
    def create(self):
        brand = str(input('марка '))
        car_model = str(input('модель '))
        date = int(input('год выпуска '))
        engine_volume = format(float(input('объем двигателя ')), '.1f')
        color = str(input('цвет '))
        body_type = str(input('тип кузова '))
        mileage = int(input('пробег '))
        price = format(float(input('цена ')), '.2f')
        model = self._model(brand=brand, car_model=car_model, date=date, engine_volume=float(engine_volume),
                            color=color, body_type=body_type, mileage=mileage, price=float(price))
        data = self.get_db_content()
        data['cars'].append(model.as_dict)
        data.update(counter=len(data['cars']))
        self.write_to_db(data)
        print('Успешно добавлено')


class ReadMixin:
    def list(self):
        data = self.get_db_content()
        print(data)

    def get_car_by_id(self):
        user_id = input('Введите id ')
        data = self.get_db_content()
        cars = data['cars']
        res = list(filter(lambda x: x['id'] == user_id, cars))
        print(res[0] if res else 'Не найдено')
        return res[0] if res else None


class UpdateMixin:
    def update(self):
        model = self._model
        data = self.get_db_content()
        car = self.get_car_by_id()
        if car is not None:
            data['cars'].remove(car)
            brand = str(input('марка ')) or car['brand']
            car_model =  str(input('модель ')) or car['car_model']
            date = int(input('год выпуска ')) or car['date']
            engine_volume = format(float(input('объем двигателя ')), '.1f') or car['engine_volume']
            color = str(input('цвет ')) or car['color']
            body_type = str(input('тип кузова')) or car['body_type']
            mileage = int(input('пробег ')) or car['mileage']
            price = format(float(input('цена ')), '.2f') or car['price']
            new_car = model(brand=brand, car_model=car_model, date=date, engine_volume=engine_volume, 
                            color=color, body_type=body_type, mileage=mileage, price=price)
            new_car.__dict__['id'] = car['id']
            data['cars'].append(new_car.as_dict)
            self.write_to_db(data)
            print('Успешно обновлено')
        else:
            print('ID не найдено')


class DeleteMixin:
    def delete(self):
        data = self.get_db_content()
        car = self.get_car_by_id()
        if car is not None:
            data['cars'].remove(car)
            data.update(counter=len(data['cars']))
            self.write_to_db(data)
            print('Успешно удален')
        else:
            print('Такого ID не существует')