
from PIL import Image
import piexif, io

def has_exif(path):
    try:
        exif = piexif.load(str(path))
        return any(exif[k] for k in exif)
    except Exception:
        return False

def remove_exif(path):
    im = Image.open(path)
    data = list(im.getdata())
    clean = Image.new(im.mode, im.size)
    clean.putdata(data)
    clean.save(path)  