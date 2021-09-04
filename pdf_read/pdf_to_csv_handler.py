from datetime import datetime

from config import settings
from create_csv import CreateCSV

from utils import find_following_working_day


class PdfToCsvHandler:
    def extract_transform_export(self):
        now = datetime.utcnow()
        now_str = now.strftime("%d_%m_%Y_%H_%M_%S")
        csv_path = f"{settings.EXPORT_CSV_TO_FOLDER}/{now_str}.csv"
        values = [
            {
                "contract_number": "736122",
                "amount": "1.400.000,00 ",
                "date": "15/02/2021",
                "write_in_days": 76,
            },
            {
                "contract_number": "942739",
                "amount": "590.000,00 ",
                "date": "13/04/2021",
                "write_in_days": 100,
            },
            {
                "contract_number": "592837",
                "amount": "800.000,00 ",
                "date": "17/03/2021",
                "write_in_days": 100,
            },
            {
                "contract_number": "285799",
                "amount": "1.200.000,00 ",
                "date": "29/05/2021",
                "write_in_days": 25,
            },
            {
                "contract_number": "584112",
                "amount": "770.000,00 ",
                "date": "31/03/2021",
                "write_in_days": 100,
            },
            {
                "contract_number": "133555",
                "amount": "871.000,00 ",
                "date": "31/03/2021",
                "write_in_days": 100,
            },
        ]
        for x in values:
            x["write_in_days"] = find_following_working_day(
                datetime.strptime(x["date"], "%d/%m/%Y").date(), x["write_in_days"]
            )
            x["write_in_days"] = x["write_in_days"].strftime("%d/%m/%Y")
        csv = CreateCSV()
        csv.generate_csv(
            data=values,
            columns=["Unit_id", "Valor_Total", "Data_Contrato", "Data_escritura"],
            csv_path=csv_path,
        )


p = PdfToCsvHandler()
p.extract_transform_export()
