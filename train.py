import cv2
import time
import numpy as np
from sklearn import svm
import os
# Định nghĩa hàm tính HOG cho ảnh
start_time = time.time()
def calculate_hog(image):
    winSize = (28, 28)
    blockSize = (14, 14)
    blockStride = (7, 7)
    cellSize = (7, 7)
    nbins = 9

    hog = cv2.HOGDescriptor(winSize, blockSize, blockStride, cellSize, nbins)
    hog_features = hog.compute(image)
    return hog_features.flatten()
      
end_time = time.time()
print("Time to extract HOG features:", end_time - start_time) 
# Đọc dữ liệu huấn luyện từ các thư mục Sample0 đến Sample9
X_train = []
y_train = []

for digit in range(10):
    sample_dir = os.path.join(f'Sample{digit}')
    for filename in os.listdir(sample_dir):
        if filename.endswith(".png"):
            image_path = os.path.join(sample_dir, filename)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            hog_features = calculate_hog(image)
            X_train.append(hog_features)
            y_train.append(digit)
start_time = time.time()
# Tạo mô hình SVM và huấn luyện nó
clf = svm.SVC(gamma='scale')
clf.fit(X_train, y_train)
end_time = time.time()
print("Time to train SVM:", end_time - start_time)
# Lưu mô hình SVM đã được huấn luyện
import pickle

with open('model.pkl', 'wb') as f:
    pickle.dump(clf, f)
