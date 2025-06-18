from etl.extractors import FileExtractor


def main():
    extractor = FileExtractor()
    ds = extractor.extract('./apps/simple.json')

    print(ds)


if __name__ == '__main__':
    main()