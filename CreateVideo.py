import os
import cv2

path = "Images/"


images = []


for file in os.listdir(path):

    name, extension = os.path.splitext(file)

    if extension.lower() in ['.jpg', '.jpeg', '.png']:

        file_name = os.path.join(path, file)


        images.append(file_name)


count = len(images)
frame = cv2.imread(images[0])


width, height, channels = frame.shape


size = (width, height)


print(size)


out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(count):
    img = cv2.imread(images[i])
    out.write(img)


print("Done")


out.release()
