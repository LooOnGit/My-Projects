import zipfile
import os
import shutil

docx_path = r"E:\Tech\My-Projects\_posts\Team6_Report2nd.docx"
out_dir = r"E:\Tech\My-Projects\assets\img\projects\arm_robot"
os.makedirs(out_dir, exist_ok=True)

image_count = 0
with zipfile.ZipFile(docx_path, 'r') as z:
    for item in z.namelist():
        if item.startswith('word/media/'):
            z.extract(item, path=out_dir)
            image_count += 1
            original_path = os.path.join(out_dir, item)
            base_name = os.path.basename(item)
            new_path = os.path.join(out_dir, base_name)
            if os.path.exists(new_path):
                os.remove(new_path)
            os.rename(original_path, new_path)

# cleanup
try:
    shutil.rmtree(os.path.join(out_dir, 'word'))
except:
    pass

print(f"Extracted {image_count} images.")
