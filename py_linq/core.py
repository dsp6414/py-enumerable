import itertools
import io

class Key(object):
    def __init__(self, key, **kwargs):
        """
        Constructor for Key class. Autogenerates key properties in object
        given dict or kwargs
        :param key: dict of name-values
        :param kwargs: optional keyword arguments
        :return: void
        """
        key = key if key is not None else kwargs
        self.__dict__.update(key)

    def __repr__(self):
        return self.__dict__.__repr__()


class OrderingDirection(object):
    def __init__(self, key, reverse):
        """
        A container to hold the lambda key and sorting direction
        :param key: lambda function
        :param reverse: boolean. True for reverse sort
        """
        self.key = key
        self.descending = reverse

class RepeatableIterable(object):
    def __init__(self, data):
        if data is None:
            data = []
        if not hasattr(data, "__iter__"):
            raise TypeError(u"RepeatableIterable must be instantiated with an iterable object")
        self._data = data
        self._len = None
        self.cycle = itertools.cycle(self._data)

    def __len__(self):
        if self._len is None:
            self._len = sum(1 for item in self._data)
        return self._len

    def __iter__(self):
        i = 0
        while i < len(self):
            yield next(self.cycle)
            i += 1

    def __next__(self):
        return self.next()

    def next(self):
        return next(self.cycle)
