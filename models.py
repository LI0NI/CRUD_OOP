from utils import Id

class Car:
    def __init__(
    self,
    brand: str,
    car_model:str,
    date:int,
    engine_volume: float,
    color:str,
    body_type: str,
    mileage:int,
    price: float
    ):
        self.id = Id().id_
        self.brand = brand
        self.car_model = car_model
        self.date = date
        self.engine_volume = engine_volume
        self.color = color
        self.body_type = body_type
        self.mileage = mileage
        self.price = price

    @property
    def as_dict(self):
        self.__dict__      
        return self.__dict__