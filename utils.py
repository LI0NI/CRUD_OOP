import uuid

class Id:
    def __init__(self) -> None:
        self._id = self.generate_id()

    @staticmethod
    def generate_id():
        return str(uuid.uuid4())[:6]
        

    @property
    def id_(self):
        return self._id

