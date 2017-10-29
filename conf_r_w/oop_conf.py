import json

class Config(object):
    def __init__(self, source=None):
        self.source = source
        self.metod_r = self.json_r
        self.metod_w = self.json_w
        if source:
            self.load(source)

    def set_s(self, data):
        self.data = data

    def get_s(self):
        return self.data

    def load(self, filename):
        with open(filename, 'r') as f:
            self.data = self.metod_r(f)

    def dump(self, filename):
        with open(filename, 'w') as f:
            self.metod_w(f, self.data)


    def json_r(self, f):
        return json.load(f)

    def json_w(self, f, data):
        json.dump(data, f)



if __name__ == '__main__':
    data = Config()

    params = {
        'key1': 'val1',
        'key2': 'val2',
        'key3': 'val3'
    }

    data.set_s(params)

    data.dump('./params.json')

    data = Config('./params.json')

    print(data.get_s())
