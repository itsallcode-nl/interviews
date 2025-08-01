from etl.extractors import FileExtractor


def main():
    extractor = FileExtractor()
    ds = extractor.extract('./apps/simple.json')
    prices = ds['price']
    quantities = ds['quantity']
    ds['total'] = prices * quantities
    print(ds)


if __name__ == '__main__':
    main()