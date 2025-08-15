from pathlib import Path
from PIL import Image, UnidentifiedImageError

def scan(rootdir: Path):
    results = []
    for p in Path(rootdir).rglob("*"):
        if not p.is_file():
            continue

        rec = {"path": str(p), "ok": True}

        try:
            # First, ensure it's a readable, non-truncated image
            with Image.open(p) as im:
                im.verify()  # quick structural check

            # Reopen to access properties after verify()
            with Image.open(p) as im:
                rec["width"], rec["height"] = im.size
                rec["format"] = im.format
                rec["mode"] = im.mode

            rec["filesize"] = p.stat().st_size

        except UnidentifiedImageError:
            rec.update({"ok": False, "error": "unreadable_or_not_image"})
        except Exception as e:
            rec.update({"ok": False, "error": f"{type(e).__name__}: {e}"})

        results.append(rec)

    return results
