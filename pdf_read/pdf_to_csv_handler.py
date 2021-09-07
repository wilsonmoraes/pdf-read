import glob
import logging
from datetime import datetime

import pandas as pd

from .config import settings
from .contract_info import ContractInfo
from .utils import find_following_working_day, pdf_content_to_str

logger = logging.getLogger()
logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S"
)
for v in ["pdfminer.pdfinterp", "pdfminer.pdfdocument", "pdfminer.pdfpage"]:
    logging.getLogger(v).setLevel(logging.WARNING)


class PdfToCsvHandler:
    def _get_all_pdf_contents(self, folder):
        pdfs = glob.glob(f"{folder}/*.pdf")
        logger.info(f"found {len(pdfs)} PDF's")
        return [pdf_content_to_str(pdf_path=pdf) for pdf in pdfs]

    def _transform_contract_info_to_csv_row(self, pdf_content):
        contract_date = ContractInfo.get_date(pdf_content)
        deed_in_days = ContractInfo.get_count_deed_in_days(pdf_content)
        deed_date = ""
        if deed_in_days:
            deed_date = find_following_working_day(
                datetime.strptime(contract_date, "%d/%m/%Y").date(),
                deed_in_days,
            ).strftime("%d/%m/%Y")

        csv_row = {
            "Unit_id": ContractInfo.get_identifier(pdf_content),
            "Valor_Total": ContractInfo.get_amount(pdf_content),
            "Data_Contrato": contract_date,
            "Data_escritura": deed_date,
        }
        return csv_row

    def _generate_csv(self, export_to, data, index_col: str = None):
        df = pd.DataFrame.from_records(data=data)
        if index_col:
            df.set_index(index_col, inplace=True)
        df.to_csv(path_or_buf=export_to)

    def run(self, pdf_folder=settings.INPUT_DIR):
        logger.info("started")
        now = datetime.utcnow()
        now_str = now.strftime("%d_%m_%Y_%H_%M_%S")
        out_file_name = f"{settings.OUT_DIR}/{now_str}.csv"

        values = self._get_all_pdf_contents(pdf_folder)
        values = [self._transform_contract_info_to_csv_row(value) for value in values]
        self._generate_csv(data=values, export_to=out_file_name, index_col="Unit_id")
        logger.info("ended")
