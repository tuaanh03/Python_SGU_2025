from abc import ABC, abstractmethod
from datetime import datetime

CURRENT_YEAR = datetime.now().year


class Person(ABC):
    def __init__(self, name: str, birth_year: int, birth_place: str):
        self._name = name
        self._birth_year = birth_year
        self._birth_place = birth_place

    # Đóng gói bằng property
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("Tên không được rỗng")
        self._name = value

    @property
    def birth_year(self) -> int:
        return self._birth_year

    @birth_year.setter
    def birth_year(self, value: int):
        if value < 1900 or value > CURRENT_YEAR:
            raise ValueError("Năm sinh không hợp lệ")
        self._birth_year = value

    @property
    def birth_place(self) -> str:
        return self._birth_place

    @birth_place.setter
    def birth_place(self, value: str):
        self._birth_place = value

    @property
    def age(self) -> int:
        return CURRENT_YEAR - self._birth_year

    @abstractmethod
    def get_role(self) -> str:
        """Lớp con bắt buộc phải override."""
        pass

