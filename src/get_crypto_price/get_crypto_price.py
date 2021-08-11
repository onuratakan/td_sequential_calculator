import requests
import json
import argparse


sources = [
    "bitstamp"
]

def get(source = "bitstamp", pair = "btcusdt"):

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', type=str, help='Source')
    parser.add_argument('-p', '--pair', type=str, help='Pair')

    args = parser.parse_args()

    if not args.source is None:
        source = args.source
    if not args.pair is None:
        pair = args.pair
    


    if source in sources:
        URL = None

        if source == "bitstamp":
            URL = f"https://www.bitstamp.net/api/v2/ticker/{pair}"


        if not URL is None:

            try:
                r = requests.get(URL)
                priceFloat = float(json.loads(r.text)["last"])
                return priceFloat

            except requests.ConnectionError:
                print("Error querying API")
            except json.decoder.JSONDecodeError:
                print("Error querying pair")

    else:
        print("Availale sources: ")
        for each_source in sources:
            print(each_source)
        raise "Source is unavailable"

