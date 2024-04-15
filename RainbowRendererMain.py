import numpy as np
from PIL import Image
import math

print("Start")


def getStandardScreenDefinitions(orientation, quality):
    """

    :param orientation: Must be "landscape" or "portrait"
    :param quality: Can be "SD", "HD", "UHD" and "4K"
    :return: Tuple with Screen Size
    """
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
    """

    :param imageSizes: (xSize, ySize)
    :return: dict with "x" and "y" arrays each between 0 and 1 on length
    """
    xArray = []
    yArray = []
    for x in range(imageSizes[0]):
        xArray.append(x / (imageSizes[0] - 1))
    for y in range(imageSizes[1]):
        yArray.append(y / (imageSizes[1] - 1))
    return {"x": xArray, "y": yArray}


def normalizeTo8Bit(value):
    """

    :param value: Float between 0 and 1
    :return: Int between 0 and 255
    """
    # rounded = int(round((value+1.0) * 128, 0))
    rounded = int(round(value * 255, 0))
    if rounded > 255:
        rounded = 255
    elif rounded < 0:
        rounded = 255
    return rounded


def redValueCalculation(posX, posY):
    """
    Here you can change your Calculation for the red Color
    :param posX: normalized X position (0 to 1)
    :param posY: normalized Y position (0 to 1)
    :return: 0-255
    """
    return normalizeTo8Bit(math.sin(3 * posX * posY * math.pi))


def greenValueCalculation(posX, posY):
    """
    Here you can change your Calculation for the green Color
    :param posX: normalized X position (0 to 1)
    :param posY: normalized Y position (0 to 1)
    :return: 0-255
    """
    return normalizeTo8Bit(math.sin(5 * posX * posY * math.pi))


def blueValueCalculation(posX, posY):
    """
    Here you can change your Calculation for the blue Color
    :param posX: normalized X position (0 to 1)
    :param posY: normalized Y position (0 to 1)
    :return: 0-255
    """
    return normalizeTo8Bit(math.sin(8 * posX * posY * math.pi))


imSize = getStandardScreenDefinitions("landscape", "HD")
print(imSize)

normedPixels = getNormalizedPixelPositions(imSize)
print(normedPixels["x"])
print(normedPixels["y"])
im = Image.new(mode="RGB", size=imSize)
np_data = np.zeros(shape=(imSize[1], imSize[0], 3), dtype=np.uint8)

for x in range(0, imSize[0]):
    for y in range(0, imSize[1]):
        np_data[y, x, 0] = redValueCalculation(normedPixels["x"][x], normedPixels["y"][y])
        np_data[y, x, 1] = greenValueCalculation(normedPixels["x"][x], normedPixels["y"][y])
        np_data[y, x, 2] = blueValueCalculation(normedPixels["x"][x], normedPixels["y"][y])  # print(np_data[y][x])

img = Image.fromarray(np_data)
img.save("RainbowRendererOutput.png")
#img.show()

##TODO
##ADD Anti Aliasing Filter
