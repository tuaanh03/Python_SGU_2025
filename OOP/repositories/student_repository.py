import os
from typing import List
from OOP.models.student import Student
from OOP.models.ScholarshipStudent import ScholarshipStudent

class StudentRepository:
    def __init__(self, filename: str = "students.txt"):
        self.filename = filename
        if not os.path.exists(self.filename):
            open(self.filename, "w", encoding="utf-8").close()


    def load_all(self) -> List[Student]:
        students: List[Student] = []
        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) < 6:
                    continue

                sid, name, by_str, bplace, gender, role = parts[:6]
                birth_year = int(by_str)

                scholarship = 0.0
                if len(parts) >= 7 and parts[6]:
                    try:
                        scholarship = float(parts[6])
                    except ValueError:
                        scholarship = 0.0

                if role == "ScholarshipStudent":
                    st = ScholarshipStudent(
                        sid, name, birth_year, bplace, gender, scholarship
                    )
                else:
                    st = Student(sid, name, birth_year, bplace, gender)

                students.append(st)
        return students

    def save_all(self, students: List[Student]) -> None:
        with open(self.filename, "w", encoding="utf-8") as f:
            for st in students:
                if isinstance(st, ScholarshipStudent):
                # //kiểm tra xem st ( đối tượng) có phải là một thể hiện của lớp ScholarshipStudent không
                    role = "ScholarshipStudent"
                    scholarship = st.scholarship_level
                else:
                    role = "Student"
                    scholarship = ""
                line = "|".join([
                    st.student_id,
                    st.name,
                    str(st.birth_year),
                    st.birth_place,
                    st.gender,
                    role,
                    str(scholarship),
                ])
                f.write(line + "\n")