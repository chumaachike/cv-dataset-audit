from pathlib import Path
from PIL import Image, UnidentifiedImageError
from quality import blur_score, exposure_hint
from exif_tools import has_exif, remove_exif

def scan(rootdir: Path, no_exif=False, no_face=False):
    results = []
    for p in Path(rootdir).rglob("*"):
        if not p.is_file():
            continue

        rec = {"path": str(p), "ok": True}

        try:
            
            with Image.open(p) as im:
                im.verify()  # quick structural check

            # Reopen to access properties after verify()
            with Image.open(p) as im:
                rec["width"], rec["height"] = im.size
                rec["format"] = im.format
                rec["mode"] = im.mode

            rec["filesize"] = p.stat().st_size
            rec["blur_score"] = blur_score(p)
            rec["exposure"] = exposure_hint(p)
            rec["exif"] = has_exif(p)

            if no_exif:
                remove_exif(p)


        except UnidentifiedImageError:
            rec.update({"ok": False, "error": "unreadable_or_not_image"})
        except Exception as e:
            rec.update({"ok": False, "error": f"{type(e).__name__}: {e}"})

        results.append(rec)

    return results
