#! /bin/pyhton

from PIL import Image, ImageDraw
import colorsys, random

## Setup block
dimensions = (256,256)
iterate_max = 150
colors_max = 15
scale = 1/(dimensions[0]/2)
center = (0.5, 0.5)
fractals=15

img = Image.new("RGB", dimensions)
d = ImageDraw.Draw(img)


for j in range(0,1200):
    scale = (1-j/10000)/(dimensions[0]/2)
    print("j = ", j)
    palette = [0] * colors_max
    for i in range(colors_max):
        f = 1-abs((float(i)/colors_max-1)**15)
        r, g, b = colorsys.hsv_to_rgb(.66+f/3, 1-f/2, f)
        palette[i] = (int(r*255), int(g*255), int(b*255))

    def iterate_mandelbrot(c, z = 0):
        for n in range(iterate_max + 1):
            z = z*z +c
            if abs(z) > 2:
                return n
        return None


    for y in range(dimensions[1]):
        for x in range(dimensions[0]):
            c = complex(x * scale - center[0], y * scale - center[1])
            
            for i in range(0,1):
                n = iterate_mandelbrot(complex((random.randint(4,6)/10), (random.randint(5,7)/10)), c)  # Use this for Julia set
                #n = iterate_mandelbrot(complex(0.3,0.7),c)
                #n = iterate_mandelbrot(c)            # Use this for Mandelbrot set

            if n is None:
                v = random.randint(1,15)
            else:
                v = n/100.0
                
            
            
            d.point((x, y), fill = palette[int(v * (colors_max-1))])
            
    #img.show()
    img.save(str(j)+".png")
