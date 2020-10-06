# Copyright (c) 2020 Anastasiia Birillo

class VkCity:
    def __init__(self, data: dict) -> None:
        self.id = data['id']
        self.title = data.get('title')

    def __str__(self):
        return f"[{', '.join(map(lambda key: f'{key}={self.__dict__[key]}', self.__dict__))}]"


class VkUser:
    def __init__(self, data: dict) -> None:
        self.id = data['id']
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.sex = data.get('sex')
        self.domain = data.get('domain')
        self.city = data.get('about')
        self.city = VkCity(data.get('city')) if data.get('city') is not None else None

    def __str__(self):
        return f"[{', '.join(map(lambda key: f'{key}={self.__dict__[key]}', self.__dict__))}]"