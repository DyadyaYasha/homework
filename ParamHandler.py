from abc import ABCMeta, abstractmethod
from os import path

class ParamHandler(metaclass=ABCMeta):
    def __init__(self, source):
        self.source = source

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    # @abstractmethod
    # def finish_writing(self):
    #     pass
    types = {}

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')
        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException (
                'Class {} is not ParamHandler'.format(klass)
            )
        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        _, ext = path.splitext(str(source).lower())
        ext = source.split('.')[-1]
        klass = cls.types.get(ext)
        if klass is None:
            raise ParamHandlerException(
                'Type {} is not found'.format(ext)
            )
        return klass(source, *args, **kwargs)


class TxtParamHandler(ParamHandler):

    def read(self):
        with open(self.source, 'r') as f:
            return f.read()

    def write(self, data):
        with open(self.source, 'w') as f:
            f.write(data)

    # def finish_writing(self, data2):
    #     with open(self.source, 'a') as f:
    #         f.write(data2)

if __name__ == '__main__':

    ParamHandler.add_type('txt', TxtParamHandler)
    r = ParamHandler.get_instance('./data.txt')
    r.write('Это запишется в файл')

    print(r.read())
