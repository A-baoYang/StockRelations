import pytest


dir_pairs = [
    ("2330", "20220301", "20220310", 8),
    ("2330", "20220301", "20220331", 23),
    ("2330", "20220315", "20220310", 0),
]


@pytest.mark.parametrize("ticker, start_date, end_date, ans_len", dir_pairs)
def test_fetch_broker(ticker, start_date, end_date, ans_len):
    from ..base import StockRelation

    stockrel = StockRelation()
    output = stockrel.get_broker_transcations(
        ticker=ticker, start_date=start_date, end_date=end_date
    )
    assert len(output) == ans_len
