from PIL import Image
from PIL import ImageEnhance
import numpy as np
import math
import random
import string
import os


def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

# определим имя директории, которую создаём
path = "C:/Users/Иван/Pictures"
os.makedirs(path)

# загружаем фото
def LineSegmentation(ImagePath):
    ima = Image.open(ImagePath)
    # увеличиваем контрастность
    ImageEnhance.Contrast(ima)
    # закидываем изображение в numpy массив
    arr = np.array(ima)
    # определяем среднюю яркость изображения и корректируем ее
    np_mean  = np.mean(arr) + np.mean(arr)/100 * 7

    # определяем высоту всего изображения
    Height = arr.shape
    minHeight = Height[0]
    
    string_average_array = []
    # В цикле определяем среднюю яркость каждой пиксельной  строчки изображения
    for i in range(Height[0]):
        string_average_array.append(np.mean(arr[i,:]))

    # flag для определения начала и конца текстово строки
    flag = 0 
    list_with_start_index = []
    list_with_end_index = []
    # В цикле выясняем является ли пискельная
    # строка началом или концом текстовой строки
    for i in range(len(string_average_array)-3):
        if all(string_average_array[i-2:i] > np_mean) and all(string_average_array[i:i + 3] < np_mean) and flag == 0:
            flag = 1
            list_with_start_index.append(i)
        if flag == 1 and all(string_average_array[i:i+2] > np_mean):
            flag = 0
            list_with_end_index.append(i)
    # определям наименьшую высоту текстовой границы
    for i in range(len(list_with_end_index)):
        if list_with_end_index[i]-list_with_start_index[i] < minHeight:
            minHeight = list_with_end_index[i]-list_with_start_index[i]
    #  с помощью newHeight и списков координат начала и концов строк
    #  увелеичиваем границы текстовых строк
    for i in range(len(list_with_end_index)):
        list_with_start_index[i] = list_with_start_index[i] - int(math.ceil(minHeight * 0.3))
        list_with_end_index[i] = list_with_end_index[i] + int(math.ceil(minHeight * 0.3))
        end_array = arr[list_with_start_index[i]: list_with_end_index[i]]
        # сохраняем полученные строки

        img = Image.fromarray(end_array, 'RGB')
        img.save("/Users/Иван/PycharmProjects/OCR abstract/LineImage/"+"TextLine"+str(i)+'.png') # Создайте и укажите путь до папки,в которую будут сохраняться изобажения


path ='C:\\Users\\Иван\\Downloads\\a.png' # укажите путь до изображения
LineSegmentation(path)
# print('средняя яроксть изображения  = ', np_mean)
# Plt для вывода изображения
# plt.gray()
# plt.imshow(ima)
# plt.colorbar()
# plt.show()

