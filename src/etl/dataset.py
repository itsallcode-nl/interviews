class DataSet[T=dict]:
    _data: list[T]

    def __init__(self, data: list[T]):
        self._data = data
