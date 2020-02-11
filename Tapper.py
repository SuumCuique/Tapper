from sys import argv
from PIL import Image
img = Image.open(argv[1])
pixels = list(img.getdata())
width, height = img.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
counter,result=0,0
for x in range(0,106):
    for y in range(0,17):
        result += (1 if pixels[y][105-x][1]==0 else 0)<<counter
        counter+=1
print(result*17)
