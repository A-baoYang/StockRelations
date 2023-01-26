def daterange(start_date: str, end_date: str):
    import arrow

    start_date, end_date = arrow.get(str(start_date)), arrow.get(str(end_date))
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date.shift(days=+n).format("YYYY-MM-DD")


def decode_key(item):
    import urllib.parse

    if type(item) == dict:
        item = {
            urllib.parse.unquote_plus(k.replace("%2E", ".")): v for k, v in item.items()
        }  # firebase 限制: 若 key 值出現 "." 改為 %2E
        return {k: decode_key(v) for k, v in item.items()}
    elif type(item) == list and type(item[0]) == dict:
        return [decode_key(d) for d in item]
    else:
        return item
