import pandas as pd


class CreateCSV:
    def generate_csv(self, csv_path, data, columns: []):
        df = pd.DataFrame.from_records(data=data)
        df.columns = columns
        df.set_index(columns[0], inplace=True)

        df.to_csv(path_or_buf=csv_path)
