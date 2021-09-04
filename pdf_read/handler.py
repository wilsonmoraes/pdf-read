import glob
import re

import PyPDF2
from pdfminer.high_level import extract_text

from config import settings
from price_parser import Price

regex_currency = re.compile(
    r'\$?(?:(?:[1-9][0-9]{0,2})(?:,[0-9]{3})+|[1-9][0-9]*|0)(?:[\.,][0-9][0-9]?)?(?![0-9]+)'
)


def pdf_to_str_PyPDF2():
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


def pdf_to_str_pdfminer():
    content = ""

    pdfs = glob.glob(f"{settings.READ_PDFS_FROM_FOLDER}/*.pdf")
    for pdf in pdfs:
        content += extract_text(pdf)
        filtered = [s for s in content.splitlines() if s]
        contract_number = filtered[3].strip()
        amount = list(filter(lambda x: x.startswith("3.1."), filtered))[0]
        amount = Price.fromstring(amount)
        write_in_days = list(filter(lambda x: x.startswith("A Escritura deverá ser lavrada"), filtered))[0]
        write_in_days = int(re.search(r'\d+', write_in_days).group())
        date = re.search(r"([0-9]{2}\/[0-9]{2}\/[0-9]{4})", filtered[-1]).group()
        print(f"file={pdf[:-4]},text={content}")
        break


pdf_to_str_pdfminer()
