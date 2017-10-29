import pickle
import json


def read_params(source):
    ext = source.split('.')[-1]
    if ext == 'json':
        with open(source, 'r') as f:
            return json_r(f)
    elif ext == 'pickle':
        with open(source, 'rb') as f:
            return pickle_r(f)
    else:
        'error'




def write_params(source, params):
    ext = source.split('.')[-1]
    if ext == 'json':
        with open(source, 'w') as f:
            return json_w(f, params)
    elif ext == 'pickle':
        with open(source, 'wb') as f:
            return pickle_w(f, params)
    else:
        'error'


def json_r(f):
    return json.load(f)

def json_w(f, data):
    json.dump(data, f)


def pickle_r(f):
    return pickle.load(f)

def pickle_w(f, data):
    pickle.dump(data, f)



if __name__ == '__main__':
    params = {
        'key1': 'val1',
        'key2': 'val2',
        'key3': 'val3'
    }

    f = './params.json'
    write_params(f, params)

    print(read_params(f))
    f = './params.pickle'
    write_params(f, params)

    print(read_params(f))
