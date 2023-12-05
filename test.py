import cv2
import numpy as np
import pickle
import os
import re
import random
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
# Tải mô hình SVM đã được huấn luyện
with open('model.pkl', 'rb') as f:
    clf = pickle.load(f)
def calculate_hog(image):
    winSize = (28, 28)
    blockSize = (14, 14)
    blockStride = (7, 7)
    cellSize = (7, 7)
    nbins = 9

    hog = cv2.HOGDescriptor(winSize, blockSize, blockStride, cellSize, nbins)
    hog_features = hog.compute(image)
    return hog_features.flatten() # type: ignore

# Đường dẫn đến thư mục chứa ảnh cần phân loại
image_directory = 'test'
test_dir = os.path.join("test")
test_files = os.listdir(test_dir)
num_test_images = len(test_files)
#Biến

# Duyệt qua tất cả các tệp ảnh trong thư mục
results = []
correct =0
correct_counts = [0] * 10
correct_fail_counts = [0] * 10
for filename in os.listdir(image_directory):
    def get_i(filename):
        path_parts = filename.split(".")
        image_name = path_parts[0]
        match = re.match("img00(\d+)-(\d+)", image_name)
        if match is None:
            return -1
            
        return int(match.group(1)) - 1
    i = get_i(filename)
    if i == -1:
        i = 9
    if filename.endswith(".png"):
        # Đọc ảnh
        image_path = os.path.join(image_directory, filename)
        image_to_classify = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # Trích xuất đặc trưng HOG và dự đoán chữ số
        hog_features = calculate_hog(image_to_classify)
        predicted_digit = clf.predict([hog_features])[0]
        if predicted_digit == int(i):
            correct += 1
            print(image_path, "Đúng với : Sample:", predicted_digit)
            correct_counts[int(i)] += 1
        else:
            print(image_path, "Sample:", predicted_digit, "Sai so với", i)
            correct_fail_counts[int(i)] += 1

        results.append((filename, predicted_digit))
print("Đúng :",correct)
print("Số lượng ảnh kiểm thử :",num_test_images)
accuracy = correct / num_test_images
print("Accuracy:", accuracy*100, "%")

for digit in range(10):
    print(f'Số được gán nhãn đúng {digit}: {correct_counts[digit]}')
    print(f'Số được gán nhãn sai {digit}: {correct_fail_counts[digit]}')
bar_colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'orange', 'purple', 'brown']
x = [f'Sample {digit}' for digit in range(10)]
y = [(correct_counts[digit] / (correct_counts[digit] + correct_fail_counts[digit])) for digit in range(10)]
for i, v in enumerate(y):
    plt.text(i, v + 0.01, f'{v:.2%}', ha='center', va='bottom')
# Plotting the bar chart

plt.bar(x, y, color=bar_colors)
plt.show()
# Hiển thị biểu đồ
# colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown']

# plt.figure(figsize=(12, 6))
# x = range(len(results))
# y = [digit for _, digit in results]
# color_labels = [colors[digit] for _, digit in results]

# plt.scatter(x, y, c=color_labels, marker='o', s=50)
# plt.xlabel('Image Index')
# plt.ylabel('Predicted Digit')
# plt.title('Predicted Digits')

# # Tạo một custom legend cho biểu đồ
# legend_labels = [f'Digit {digit}' for digit in range(10)]
# #legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[digit], markersize=10) for digit in range(10)]
# legend_handles = [Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in colors]
# plt.legend(legend_handles, legend_labels)



plt.show()
output_directory = 'output_images'
os.makedirs(output_directory, exist_ok=True)

# Create a dictionary to store 16 images for each class
images_by_class = {digit: [] for digit in range(10)}

# Sort the results into separate lists for each class
for filename, digit in results:
    if len(images_by_class[digit]) < 20:
        images_by_class[digit].append(filename)

# Display the 16 images for each class
for digit, filenames in images_by_class.items():
    plt.figure(figsize=(7, 7))
    plt.suptitle(f'Images for Digit {digit}')
    for i, filename in enumerate(filenames):
        image_path = os.path.join(image_directory, filename)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        plt.subplot(4, 5, i + 1)
        plt.imshow(image, cmap='gray')
        plt.axis('off')
    plt.show()

