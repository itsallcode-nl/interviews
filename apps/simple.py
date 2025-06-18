from etl.extractors import FileExtractor


def feature():
    extractor = FileExtractor()
    ds = extractor.extract('./apps/simple.json')

    ds['total'] = ds['price'] * ds['quantity']
    return ds


def extra():
    ds = feature()
    print(sum(ds['total']))


def main():
    extractor = FileExtractor()
    ds = extractor.extract('./apps/simple.json')

    print(ds)


if __name__ == '__main__':
    main()