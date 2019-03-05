# import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageEnhance
import numpy as np
import matplotlib.pyplot as plt
import os
# загружаем фото, закидываемаем в numpy массив


def WordSegmentation(ImagePath, filename):
    img = Image.open(ImagePath)
    ImageEnhance.Contrast(img)
    arr = np.array(img)
    original_arr = np.array(img)

    average_bright_of_image = np.mean(arr) * 1.07
    height = arr.shape
    # размазываем картинку, для более отчеливого разрыва между словами
    for i in range(len(arr)-1):
        for j in range(height[1]-1):
            if arr[i][j][0] < average_bright_of_image:
                arr[i][j] = [0, 25, 5]
                arr[i+1][j] = [0, 25, 5]

    # Для всех пиксельных столбцов исходного изображения строки находим их средние значения яркости
    column_average_array = []
    for i in range(height[1]):
        column_average_array.append(np.mean(arr[:, i]))

    start_average_coefficient = np.mean(column_average_array) * 1.5
    end_average_coefficient = np.mean(column_average_array) * 1.5
    list_with_start_index = []
    list_with_end_index = []
    flag = 0
    # plt.imshow(arr)
    # plt.show()
    for i in range(height[1]-7):
        # print(i , column_average_array)
        # print(list_with_start_index)
        # print(list_with_end_index)
        if flag == 0 and all(column_average_array[i:i+4] < start_average_coefficient) and column_average_array[i-1] > start_average_coefficient:
            list_with_start_index.append(i)
            flag = 1
        if flag == 1 and all(column_average_array[i:i+4] > end_average_coefficient )  and all(column_average_array[i-3:i] < end_average_coefficient):
            list_with_end_index.append(i)
            flag = 0
    print(column_average_array[184:200])
    print(start_average_coefficient)
    for i in range(len(list_with_end_index)):
        original_arr[:, list_with_start_index[i]] = [0, 200, 3]
        original_arr[:, list_with_end_index[i]] = [200, 4, 5]
        # end_array = original_arr[:, 21: 129]
        end_array = original_arr[:, list_with_start_index[i]: list_with_end_index[i]]
        # сохраняем полученные строки
        img = Image.fromarray(end_array, 'RGB')

        img.save("/Users/Иван/PycharmProjects/OCR abstract/WordImage/" +filename + "Word" + str(i) + '.png')
     # plt.imshow(original_arr)
    # plt.show()
    # img = Image.fromarray(original_arr , 'RGB')
    # img.show()
array_with_line = os.listdir('/Users/Иван/PycharmProjects/OCR abstract/LineImage/')
for i in array_with_line:
    path=os.getcwd()+'\\LineImage'+'\\'+i
    WordSegmentation(path, i)
# img = Image.fromarray(original_arr, 'RGB')
# plt.imshow(arr)
# plt.show()
# img.show()
# print(os.getcwd())
