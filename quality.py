import cv2

def blur_score (imagepath):
    image = cv2.imread(imagepath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()

def exposure_hint(imagepath):
    image = cv2.imread(imagepath)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    m = float(gray.mean())
    # crude buckets: tune later
    if m < 60: return "under"
    if m > 190: return "over"
    return "ok"