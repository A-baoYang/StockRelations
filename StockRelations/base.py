import os
import requests
from .utils import daterange, decode_key


class StockRelation:
    def __init__(self) -> None:
        self.db_root = "https://stockrelations-dabe9-default-rtdb.asia-southeast1.firebasedatabase.app/Relations"

    def get_broker_transcations(self, ticker: str, start_date: str, end_date: str):

        self.ticker = ticker

        table_dir = "chip"
        table_name = "12-concords-broker_transcations_2330_2022-3-1_2022-3-31.json"
        db_path = os.path.join(self.db_root, table_dir, table_name)
        data = requests.get(db_path).json()[self.ticker]
        data = {
            k: v for k, v in data.items() if k in list(daterange(start_date, end_date))
        }
        return decode_key(data)
