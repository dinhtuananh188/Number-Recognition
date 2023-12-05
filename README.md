# Number-Recognition
# Hướng dẫn Sử Dụng và Mô Tả Dự Án

## Mục Đích Dự Án
Dự án này sử dụng máy học để nhận diện chữ số từ hình ảnh sử dụng mô hình Support Vector Machine (SVM) và đặc trưng Histogram of Oriented Gradients (HOG).

## Cài Đặt

### Dự Án Huấn Luyện (`train.py`)

1. **Clone Repository:**
   - Sao chép repository về máy tính của bạn:

     git clone https://github.com/dinhtuananh188/Number-Recognition.git


2. **Cài Đặt Thư Viện:**
   - Đảm bảo bạn đã cài đặt các thư viện cần thiết. Bạn có thể sử dụng pip để cài đặt chúng:

     pip install opencv-python numpy scikit-learn


3. **Chuẩn Bị Dữ Liệu Huấn Luyện:**
   - Dữ liệu huấn luyện được lưu trong các thư mục `Sample0` đến `Sample9`. Mỗi thư mục chứa ảnh tương ứng với một chữ số.

4. **Rút Trích Đặc Trưng HOG và Huấn Luyện SVM:**
   - Chạy script Python để rút trích đặc trưng HOG và huấn luyện mô hình SVM:

     python train.py

   - Mô hình SVM được lưu vào tệp `model.pkl`.

### Dự Án Kiểm Thử (`test.py`)

1. **Cài Đặt Thư Viện:**
   - Đảm bảo bạn đã cài đặt các thư viện cần thiết. Bạn có thể sử dụng pip để cài đặt chúng:

     pip install opencv-python numpy scikit-learn matplotlib


2. **Tải Mô Hình SVM:**
   - Đảm bảo bạn đã tải mô hình SVM từ tệp `model.pkl`.

3. **Chuẩn Bị Ảnh Kiểm Thử:**
   - Đặt ảnh kiểm thử trong thư mục `test`.

4. **Dự Đoán và Đánh Giá Trên Ảnh Kiểm Thử:**
   - Chạy script Python để dự đoán và đánh giá:

     python test.py

   - Kết quả sẽ được hiển thị thông qua terminal, và biểu đồ chính xác theo từng chữ số sẽ được tạo ra.

5. **Hiển Thị Hình Ảnh Kết Quả:**


## Lưu Ý
- Để sử dụng mô hình đã được huấn luyện, đảm bảo bạn đã cài đặt các thư viện cần thiết và đã tải mô hình từ tệp `model.pkl`.
