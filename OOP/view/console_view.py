from OOP.models.student import Student
from OOP.models.ScholarshipStudent import ScholarshipStudent
from OOP.repositories.student_repository import StudentRepository
from OOP.controller.student_controller import StudentController


def input_student() -> Student:
    sid = input("Mã sinh viên: ").strip()
    name = input("Họ tên: ").strip()
    birth_year = int(input("Năm sinh (vd 2002): ").strip())
    birth_place = input("Nơi sinh (vd HCM, Hà Nội): ").strip()
    gender = input("Giới tính (nam/nu/other): ").strip().lower()
    is_scholar = input("Có phải sinh viên học bổng? (y/n): ").strip().lower()

    if is_scholar == "y":
        scholarship_level = float(input("Mức học bổng (triệu/tháng): ").strip())
        return ScholarshipStudent(sid, name, birth_year, birth_place, gender, scholarship_level)
    else:
        return Student(sid, name, birth_year, birth_place, gender)


def show_stats(service: StudentController):
    print("\n=== THỐNG KÊ ===")
    g = service.stats_gender()
    print(f"Tổng sinh viên: {len(service.list_students())}")
    print(f"- Nam : {g['nam']}")
    print(f"- Nữ  : {g['nu']}")
    print(f"- Khác: {g['other']}")

    age_stats = service.stats_age()
    print(f"Độ tuổi: min = {age_stats['min']}, "
          f"max = {age_stats['max']}, "
          f"avg = {age_stats['avg']:.1f}")

    print("\nTheo nơi sinh:")
    birth_stats = service.stats_birth_place()
    for place, count in birth_stats.items():
        print(f"- {place}: {count} sv")


def run_app():
    # Use the students file in the project root. Using "../students.txt" points outside the project
    # when running from project root; use the default filename in the repository or an explicit
    # "students.txt" here so the app can read/write data correctly.
    repo = StudentRepository("students.txt")
    service = StudentController(repo)

    while True:
        print("\n===== QUẢN LÝ SINH VIÊN (OOP + TXT) =====")
        print("1. Thêm sinh viên")
        print("2. Xem danh sách sinh viên")
        print("3. Xem thống kê (giới tính, độ tuổi, nơi sinh)")
        print("0. Thoát")
        choice = input("Chọn: ").strip()

        if choice == "1":
            try:
                st = input_student()
                service.add_student(st)
                print(">> Đã thêm sinh viên thành công!")
            except Exception as e:
                print("Lỗi khi thêm sinh viên:", e)

        elif choice == "2":
            print("\n=== DANH SÁCH SINH VIÊN ===")
            for s in service.list_students():
                print(s.describe())  # đa hình

        elif choice == "3":
            show_stats(service)

        elif choice == "0":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")
