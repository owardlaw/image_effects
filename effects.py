import cv2
import numpy as np
import random

def effects(file, type, speed, show, scale_percent, blowup):
    img = cv2.imread(file)
    origional = img.shape
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    arr = cv2.resize(img, dim)
    img = [ [ (int(p[0]),int(p[1]),int(p[2])) for p in row ] for row in arr ]

    copy=[]

    for i in range(len(img)):
        row = []
        for j in range(len(img[i])):
            row.append((0,0,0))
        copy.append(row)

    for c in range(0,255, speed):
        if type == "color":
            one = random.randrange(0,255)
            two = random.randrange(0,255)
            three = random.randrange(0,255)

        for i in range(len(copy)):
            if type == "line":
                one = random.randrange(0,255)
                two = random.randrange(0,255)
                three = random.randrange(0,255)

            for j in range(len(copy[i])):
                if type == "pixel":
                    one = random.randrange(0,255)
                    two = random.randrange(0,255)
                    three = random.randrange(0,255)
                if img[i][j][0] <  255-c:
                    copy[i][j] = (one,two,three)

                else:
                    copy[i][j] = img[i][j]

        if (c%show)==0:
            arr = np.asarray(copy, dtype=np.uint8)
            arr = cv2.cvtColor(arr, cv2.COLOR_BGR2RGB)
            arr = cv2.resize(arr, (origional[1]*blowup, origional[0]*blowup))
            cv2.imshow('image', arr)
            cv2.waitKey(1)

    return copy

def color(file, rgb, speed, show, scale_percent, blowup):
    img = cv2.imread(file)
    origional = img.shape
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    arr = cv2.resize(img, dim)
    img = [ [ (int(p[0]),int(p[1]),int(p[2])) for p in row ] for row in arr ]

    copy=[]

    for i in range(len(img)):
        row = []
        for j in range(len(img[i])):
            row.append((0,0,0))
        copy.append(row)

    for c in range(0,255, speed):
        for i in range(len(copy)):

            for j in range(len(copy[i])):
                if img[i][j][0] <  255-c:
                    copy[i][j] = rgb
                else:
                    copy[i][j] = img[i][j]

        if (c%show)==0:
            arr = np.asarray(copy, dtype=np.uint8)
            arr = cv2.cvtColor(arr, cv2.COLOR_BGR2RGB)
            arr = cv2.resize(arr, (origional[1]*blowup, origional[0]*blowup))
            cv2.imshow('image', arr)
            cv2.waitKey(1)

    return copy

'''
Color Parameters: (
    file path,
    RBG color for background,
    amount of iterations,
    refresh rate,
    downscaling of image for speed,
    upscaling of image for display
    )

Effects Parameters: (
    file path,
    Effect type (pixel, color, line),
    amount of iterations,
    refresh rate,
    downscaling of image for speed,
    upscaling of image for display
    )
'''

# Test Examples (slowest is "pixel")
test_black = color("images/dream.jpg",(0,0,0), 5, 2, 30, 2)
test_color = effects("images/dream.jpg",'pixel', 7, 7, 30, 2)
test_color = effects("images/dream.jpg",'color', 5, 5, 50, 2)
test_color = effects("images/dream.jpg",'line', 5, 5, 50, 2)
