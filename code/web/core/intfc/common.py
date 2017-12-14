import requests
import simplejson as json


def request(url, data):
    code = -1
    error = ""
    result = {}
    headers = {'Content-Type': 'application/json'}
    try:
        r = requests.post(url = url, headers = headers, data = json.dumps(data))
        code = r.status_code
    except (requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
            requests.exceptions.Timeout,
            requests.exceptions.TooManyRedirects):
        pass
    while (True):
        if code <> 200 and code <> 400:
            break
        try:
            rdata = r.json()
        except (ValueError):
            break
        if (code == 400):
            error = rdata['error']
            break
        result = rdata['results']
        break
    return code, error, result
