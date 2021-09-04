from datetime import datetime

import pandas as pd
from config import settings


class CreateCSVHandler:
    def generate_csv(self, csv_path, data, columns: []):
        df = pd.DataFrame.from_records(data=data)
        df.columns = columns
        df.set_index(columns[0], inplace=True)

        df.to_csv(path_or_buf=csv_path, header=True)


def run_example():
    values = [
        {"contract_number": "736122", "amount": "1.400.000,00 ", "write_in_days": 76, "date": "15/02/2021"},
        {"contract_number": "942739", "amount": "590.000,00 ", "write_in_days": 100, "date": "13/04/2021"},
        {"contract_number": "592837", "amount": "800.000,00 ", "write_in_days": 100, "date": "17/03/2021"},
        {"contract_number": "285799", "amount": "1.200.000,00 ", "write_in_days": 25, "date": "29/05/2021"},
        {"contract_number": "584112", "amount": "770.000,00 ", "write_in_days": 100, "date": "31/03/2021"},
        {"contract_number": "133555", "amount": "871.000,00 ", "write_in_days": 100, "date": "31/03/2021"},
    ]
    now = datetime.utcnow()
    now_str = now.strftime("%d_%m_%Y_%H_%M_%S")

    csv = CreateCSVHandler()
    csv.generate_csv(
        data=values,
        columns=["Unit_id", "Valor_Total", "Data_Contrato", "Data_escritura"],
        csv_path=f"{settings.EXPORT_CSV_TO_FOLDER}/{now_str}.csv",
    )
