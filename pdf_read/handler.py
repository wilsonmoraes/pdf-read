import glob

import PyPDF2

from config import settings


def pdf_to_str():
    content = ""

    pdfs = glob.glob(f"{settings.READ_PDFS_FROM_FOLDER}/*.pdf")
    for pdf in pdfs:
        pdf_file = open(pdf, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        num_pages = read_pdf.getNumPages()
        for i in range(0, num_pages):
            content += read_pdf.getPage(i).extractText() + "\n"
            content = " ".join(content.replace(u"\xa0", " ").strip().split())

        print(f"file={pdf[:-4]},text={content}")
        break


pdf_to_str()
