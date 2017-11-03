import json

def http_headers_to_json(head, result):
    with open(head, 'r') as f:
        st = f.readline().strip().split()
        sp = st[0][0:3]
        dict1 = {
        'protocol':st[0],
        'status_code':st[1],
        'status_message':st[2]
        }

        dict2 = {
        'method':st[0],
        'uri':st[1],
        'protocol':st[2]
        }

        if sp == 'HTT':
            dict0 = dict1

        elif sp == 'GET':
            dict0 = dict2

        for st in f:
            if len(st) > 1:
                st = st.strip('\n')
                st = f.readline().strip().split(':', 1)
                dict0[st[0]] = st[1]


    with open(result, 'w') as f:
        f.write(json.dumps(dict0, indent=4))

    return dict0

if __name__ == '__main__':
    http_headers_to_json('headers-1.txt', 'results-1.json')
    http_headers_to_json('headers-2.txt', 'results-2.json')
    http_headers_to_json('headers-3.txt', 'results-3.json')
