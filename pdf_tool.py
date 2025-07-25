
from PyPDF2 import PdfMerger, PdfReader
import os

def merge_pdfs(files, output):
    merger = PdfMerger()
    for f in files:
        if os.path.exists(f) and f.endswith(".pdf"):
            merger.append(f)
        else:
            print(f"Warning: {f} not found or not a PDF.")
    merger.write(output)
    merger.close()
    print(f"Created merged file: {output}")

def split_pdf(file):
    if not os.path.exists(file) or not file.endswith(".pdf"):
        print(f"Error: {file} not found or is not a PDF.")
        return
    reader = PdfReader(file)
    for i, page in enumerate(reader.pages):
        writer = PdfMerger()
        writer.append(file, pages=(i, i+1))
        out_name = f"page_{i+1}.pdf"
        writer.write(out_name)
        writer.close()
        print(f"Create: {out_name}")

if __name__ == "__main__":
    # Example usage - replace with your own PDF files
    merge_pdfs(["file1.pdf", "file2.pdf"], "merged.pdf")
    split_pdf("merged.pdf")
