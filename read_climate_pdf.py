import traceback
import PyPDF2

try:
    path = r"E:\Tech\My-Projects\_posts\Mạng lưới mạng khí hậu trong.pdf"
    doc = PyPDF2.PdfReader(path)
    text = []
    for page in doc.pages:
        text.append(page.extract_text())
    with open("temp2.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(text))
    print("Done")
except Exception as e:
    print(traceback.format_exc())
