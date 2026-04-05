import fitz
import os

pdf_path = r"E:\Tech\My-Projects\_posts\Mạng lưới mạng khí hậu trong.pdf"
out_dir = r"E:\Tech\My-Projects\assets\img\projects\microclimate"
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)
image_count = 0
for page_index in range(len(doc)):
    page = doc[page_index]
    image_list = page.get_images()
    for image_index, img in enumerate(image_list, start=1):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image_name = f"page{page_index+1}_img{image_index}.{image_ext}"
        image_path = os.path.join(out_dir, image_name)
        with open(image_path, "wb") as f:
            f.write(image_bytes)
        print("Saved:", image_path)
        image_count += 1
print(f"Total {image_count} images extracted.")
