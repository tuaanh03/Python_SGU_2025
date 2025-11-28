import numpy as np
# 1. Tạo mảng và truy cập
a=np.arange(3)
print(" Mảng a:\n", a)
#Tạo mảng 1 chiều gồm các số từ 0 → 2 (không bao gồm 3).



a1=np.arange(12).reshape(3,4)
print(" Mảng a1 (reshape 3x4):\n", a1)
# np.arange(12) → tạo dãy 0 đến 11
#
# reshape(3,4) → biến thành ma trận 3 hàng, 4 cột



b=np.ones((1,2))
print("mảng b (matrix 1x2 toàn 1):\n", b)
# Tạo ma trận kích thước 1 hàng × 2 cột
# Tất cả phần tử = 1

c=np.full((3,2,2),9)
print("mảng c (matrix 3x2x2 toàn 9):\n", c)
# Tạo tensor (mảng nhiều chiều) kích thước 3 × 2 × 2,
# và mọi giá trị đều bằng 9.
#
# ➤ Cấu trúc hình khối 3 lớp, mỗi lớp 2×2:

# [
#   [[9 9],
#    [9 9]],
#
#   [[9 9],
#    [9 9]],
#
#   [[9 9],
#    [9 9]]
# ]


d=np.eye(3)
print("mảng d (ma trận đơn vị 3x3): \n", d)
# Tạo ma trận đơn vị 3×3, trong đó:
#
# Đường chéo chính = 1
#
# Các phần tử khác = 0


#Ma trận ngẫu nhiên 3x3
M_rand = np.random.randint(1, 10, size=(3, 3))
print(" Ma trận ngẫu nhiên:\n", M_rand)
# Tạo ma trận 3×3 gồm các số ngẫu nhiên từ 1 → 9.



# Ma trận vuông với đường chéo chính 1,2,3
M_diag = np.diag([1, 2, 3])
print(" Ma trận đường chéo:\n", M_diag)
#Tạo ma trận đường chéo với các số 1, 2, 3 nằm trên đường chéo chính.