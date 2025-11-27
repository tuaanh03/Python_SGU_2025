from .person import Person


class Student(Person):
    def __init__(self, student_id: str, name: str, birth_year: int, birth_place: str, gender: str):
        super().__init__(name, birth_year, birth_place)
        self._student_id = student_id
        g = (gender or "").strip().lower()
        if g == 'khac':
            g = 'other'
        if g not in ('nam', 'nu', 'other'):
            g = 'other'
        self._gender = g

    # tính đóng gói
    @property
    def student_id(self) -> str:
        return self._student_id

    @student_id.setter
    def student_id(self, value: str):
        if not value:
            raise ValueError("Mã sinh viên không được rỗng")
        self._student_id = value

    @property
    def gender(self) -> str:
        return self._gender

    @gender.setter
    def gender(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Giới tính phải là chuỗi")
        v = value.strip().lower()
        if v == 'khac':
            v = 'other'
        if v not in ('nam', 'nu', 'other'):
            raise ValueError("Giới tính phải là 'nam', 'nu' hoặc 'other'")
        self._gender = v

    def get_role(self) -> str:
        return "Student"

    def describe(self) -> str:
        return (f"[{self.student_id}] {self.name} - {self.age} tuổi - "
                f"{self.gender} - Nơi sinh: {self.birth_place} - Loại: {self.get_role()}")
