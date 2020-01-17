from sys import argv
from PIL import Image
img = Image.open(argv[1])
pixels = list(img.getdata())
width, height = img.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
counter,string,mas=0,0,{}
for x in range(0,106):
    mas[x] = {}
    for y in range(0,17):
        mas[x][y] = 1 if pixels[y][105-x][1]==0 else 0
        string += mas[x][y]<<counter
        counter+=1
print(string*17)