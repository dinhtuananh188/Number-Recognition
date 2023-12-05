import datetime
import os
import cv2
import time
import numpy as np
from sklearn.svm import SVC

import pickle

# Tạo dữ liệu huấn luyện
train_data = []  
train_labels = []

for i in range(0,10):
  train_path = os.path.join("Sample" + str(i))

  for img_path in os.listdir(train_path):  
    img = cv2.imread(os.path.join(train_path, img_path))
    train_data.append(img)
    train_labels.append(i)

# Trích xuất HOG features
def extract_hog_features(img):
  gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  hog_descriptor = cv2.HOGDescriptor()  
  hog_features = hog_descriptor.compute(gray_img)
  return hog_features

start_time = time.time()
train_features = np.array([extract_hog_features(img) for img in train_data])
end_time = time.time()
print("Time to extract HOG features:", end_time - start_time)

start_time = time.time()
clf = SVC(kernel="linear", C=1)
clf.fit(train_features, train_labels)
end_time = time.time()
print("Time to train SVM:", end_time - start_time)
print(train_features)

now = datetime.datetime.now()

# Sử dụng biến này để tạo tên file mới
filename = str(now.hour) + str(now.minute) + "_" + str(now.day) + str(now.month) + str(now.year) + ".pkl"

# Sử dụng hàm pickle.dump() để lưu mô hình vào file mới
with open(filename, "wb") as f:
    pickle.dump(clf, f)
