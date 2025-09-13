
**Code (pdf_tool.py)**  
```python
from PyPDF2 import PdfMerger, PdfReader

def merge_pdfs(files, output):
    merger = PdfMerger()
    for f in files:
        merger.append(f)
    merger.write(output)
    merger.close()

def split_pdf(file):
    reader = PdfReader(file)
    for i, page in enumerate(reader.pages):
        writer = PdfMerger()
        writer.append(file, pages=(i, i+1))
        writer.write(f"page_{i+1}.pdf")
        writer.close()

# Example
merge_pdfs(["file1.pdf", "file2.pdf"], "merged.pdf")
split_pdf("merged.pdf")
