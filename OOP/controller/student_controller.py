from typing import List, Dict
from OOP.models.student import Student
from OOP.repositories.student_repository  import StudentRepository


class StudentController:
    def __init__(self, repo: StudentRepository):
        #  khởi tạo repo, tức là nơi tương tác với dữ liệu sinh viên
        self.repo = repo

        #tạo tạo một mảng để lưu dữ liệu sinh viên được load ra
        self.students: List[Student] = self.repo.load_all()

    def add_student(self, student: Student) -> None:
        self.students.append(student)
        self.repo.save_all(self.students)

    def list_students(self) -> List[Student]:
        return self.students

    def stats_gender(self) -> Dict[str, int]:
        result = {"nam": 0, "nu": 0, "other": 0}
        for s in self.students:
            g = s.gender
            if g in result:
                # giới tính nam, nữ , hay other đều tăng
                result[g] += 1
            else:
                # khi điền giới tính là giá trị khác với nam, nữ, other thì cũng tăng other
                result["other"] += 1
        return result

    # đếm mỗi nơi sinh có bao nhiêu sinh viên
    def stats_birth_place(self) -> Dict[str, int]:
        result: Dict[str, int] = {}
        for s in self.students:
            place = s.birth_place.strip().lower()
            result[place] = result.get(place, 0) + 1
        return result

    # thống kê tuổi min, max, avg
    def stats_age(self) -> Dict[str, float]:
        if not self.students:
            return {"min": 0, "max": 0, "avg": 0}
        ages = [s.age for s in self.students]
        return {
            "min": min(ages),
            "max": max(ages),
            "avg": sum(ages) / len(ages),
        }