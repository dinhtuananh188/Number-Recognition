import os
import random
import shutil

# Tạo thư mục DuPhong nếu chưa tồn tại
if not os.path.exists("DuPhong"):
    os.mkdir("DuPhong")

# Lấy danh sách tất cả các thư mục Sample
dirs = os.listdir(".")
dirs = [d for d in dirs if d.startswith("Sample")]

# Lặp qua từng thư mục Sample
for dir in dirs:
    # Lấy danh sách tất cả các file trong thư mục
    files = os.listdir(dir)

    # Lấy 900 file ngẫu nhiên
    files = random.sample(files, 50)

    # Chuyển các file ngẫu nhiên sang thư mục DuPhong
    for file in files:
        shutil.copy(os.path.join(dir, file), "DuPhong")

    # Xóa các file trong thư mục Sample gốc
    for file in files:
        os.remove(os.path.join(dir, file))
