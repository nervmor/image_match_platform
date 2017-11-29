from define import RESULT
import simplejson as json

def common_api_check(request):
    res = False
    ret = {}
    req = object
    while (True):
        if request.method != 'POST':
            ret['code'] = RESULT.HTTP_METHOD_NOT_SUPPORT['code']
            ret['error'] = RESULT.HTTP_METHOD_NOT_SUPPORT['error']
            break
        try:
            if not request.body:
                req = {}
            else:
                req = json.loads(request.body, encoding='utf-8')
            res = True
            break
        except (TypeError, ValueError, AttributeError), e:
            ret['code'] = RESULT.JSON_PARSE_ERROR['code']
            ret['error'] = RESULT.JSON_PARSE_ERROR['error']
            break
    return res, ret, req