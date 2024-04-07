from PIL import Image

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

    im = Image.new(mode="RGB", size=getStandardScreenDefinitions("landscape","SD"))