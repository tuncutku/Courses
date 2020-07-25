from typing import List, Dict, TypeVar, Type
from abc import ABCMeta, abstractmethod
from common.database import Database

T = TypeVar("T", bound="Model")


class Model(metaclass=ABCMeta):
    collection: str

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def save(self):
        raise NotImplementedError

    @abstractmethod
    def remove(self):
        raise NotImplementedError

    @classmethod
    def all(cls: Type[T]) -> List[T]:
        elements_from_db = Database.get_all(cls.collection)
        return [cls(*elem) for elem in elements_from_db]

    @classmethod
    def find_one_by(cls: Type[T], item_id) -> T:
        return cls(*Database.get_one(cls.collection, item_id))

    # @classmethod
    # def find_many_by(cls: Type[T], attribute: str, value: str) -> List[T]:
    #     return [cls(**elem) for elem in Database.find(cls.collection, {attribute: value})]
