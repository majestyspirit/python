from requests import get, utils
from datetime import datetime

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


def currency_rates(count):
    for i in content.split("Valute ID="):
        if count.upper() in i:
            print(datetime.strptime(content.split("Valute ID=")[0].split('"')[-4], '%d.%m.%Y')
                  .date(), ", ", sep="", end="")
            return float(i.replace("/", "").split("Value")[-2].replace("<", "").replace(">", "").replace(",", "."))


if __name__ == '__main__':
    print('as file')
else:
    print('as module')
