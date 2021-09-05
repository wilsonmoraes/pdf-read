import glob
import logging
from datetime import datetime

import pandas as pd

from .config import settings
from .pdf_detail_handler import PdfDetailHandler
from .utils import find_following_working_day

logger = logging.getLogger()
logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S"
)
for v in ["pdfminer.pdfinterp", "pdfminer.pdfdocument", "pdfminer.pdfpage"]:
    logging.getLogger(v).setLevel(logging.WARNING)


class PdfToCsvHandler:
    def extract_contract_details_from_folder(self, folder):
        pdf_detail_handler = PdfDetailHandler()
        pdfs = glob.glob(f"{folder}/*.pdf")
        logger.info(f"found {len(pdfs)} PDF's")
        return [pdf_detail_handler.get_detail(pdf) for pdf in pdfs]

    def transform_pdf_details_to_csv_details(self, contract_detail):
        details_to_csv = {
            "Unit_id": contract_detail["contract_number"],
            "Valor_Total": contract_detail["amount"],
            "Data_Contrato": contract_detail["date"],
            "Data_escritura": find_following_working_day(
                datetime.strptime(contract_detail["date"], "%d/%m/%Y").date(),
                contract_detail["write_in_days"],
            ),
        }
        details_to_csv["Data_escritura"] = details_to_csv["Data_escritura"].strftime("%d/%m/%Y")
        return details_to_csv

    def generate_csv(self, csv_path, data):
        df = pd.DataFrame.from_records(data=data)
        df.to_csv(path_or_buf=csv_path)

    def run(self, pdf_folder=settings.INPUT_DIR):
        logger.info("started")
        now = datetime.utcnow()
        now_str = now.strftime("%d_%m_%Y_%H_%M_%S")
        csv_path = f"{settings.OUT_DIR}/{now_str}.csv"

        values = self.extract_contract_details_from_folder(pdf_folder)
        values = [self.transform_pdf_details_to_csv_details(value) for value in values]
        self.generate_csv(
            data=values,
            csv_path=csv_path,
        )
        logger.info("ended")
