from .student import Student


class ScholarshipStudent(Student):
    def __init__(self, student_id: str, name: str, birth_year: int, birth_place: str, gender: str, scholarship_level: float):
        super().__init__(student_id, name, birth_year, birth_place, gender)
        try:
            self._scholarship_level = float(scholarship_level) if scholarship_level not in (None, "") else 0.0
        except Exception:
            self._scholarship_level = 0.0

    @property
    def scholarship_level(self) -> float:
        return self._scholarship_level

    @scholarship_level.setter
    def scholarship_level(self, value: float):
        try:
            self._scholarship_level = float(value)
        except Exception:
            raise ValueError("Mức học bổng phải là một số")

    def get_role(self) -> str:
        return "ScholarshipStudent"

    def describe(self) -> str:
        base = super().describe()
        return f"{base} - Học bổng: {self.scholarship_level:.1f} triệu/tháng"