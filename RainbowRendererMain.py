from PIL import Image
print("Start")
def getStandardScreenDefinitions(orientation, quality):
    if orientation == "landscape":
        if quality == "SD":
            return (720, 405)
        elif quality == "HD":
            return (1920, 1080)
        elif quality == "UHD":
            return (3840, 2160)
        elif quality == "4K":
            return (4096, 2160)
        else:
            raise Exception("Not Standard Landscape Screen Size")
    elif orientation == "portrait":
        if quality == "SD":
            return (405, 720)
        elif quality == "HD":
            return (1080, 1920)
        elif quality == "UHD":
            return (2160, 3840)
        elif quality == "4K":
            return (2160, 4096)
        else:
            raise Exception("Not Standard Portrait Screen Size")

def getNormalizedPixelPositions(imageSizes):
    xArray = []
    yArray = []
    for x in range(imageSizes[0]):
        xArray.append(x/100.0)
    for y in range(imageSizes[1]):
        yArray.append(y/100.0)
    return {"x": xArray, "y": yArray}

imSize = getStandardScreenDefinitions("landscape","SD")
print(imSize)
print(imSize[0])
im = Image.new(mode="RGB", size=imSize)

im.show()