from .defn import RESULT
import simplejson as json
import types
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

def is_type_int(v):
    if not isinstance(v, types.IntType):
        return False
    return True

def is_type_float(v):
    if not isinstance(v, types.FloatType):
        return False
    return True

def is_type_str(v):
    if not isinstance(v, types.StringType):
        return False
    return True

def is_type_list(v):
    if not isinstance(v, types.ListType):
        return False
    return True

def parse_class_param(req):
    ret = True
    category = []
    tags = []

    while (True):
        if not req.has_key('class'):
            break
        if req['class'].has_key('category'):
            if not is_type_list(req['class']['category']):
                ret = False
                break
            valid = True
            for e in req['class']['category']:
                if not is_type_str(e):
                    valid = False
                    break
                category.append(e)
            if not valid:
                break

        if req['class'].has_key('tags'):
            if not is_type_list(req['class']['tags']):
                ret = False
                break
            valid = True
            for e in req['class']['tags']:
                if not is_type_str(e):
                    valid = False
                    break
                tags.append(e)
            if not valid:
                break
        break
    return ret, category, tags


def make_pic_class(category, tags):
    cls = {}
    c = []
    t = []
    for e in category.split(';'):
        if len(e) <> 0:
            c.append(e)
    for e in tags.split(';'):
        if len(e) <> 0:
            t.append(e)
    cls['category'] = c
    cls['tags'] = t
    return cls

def make_pic_class_str(category, tags):
    str_category = ""
    for s in category:
        if len(str_category) <> 0:
            str_category += ";"
        str_category += s
    str_tags = ""
    for s in tags:
        if len(str_tags) <> 0:
            str_tags += ";"
        str_tags += s
    return str_category, str_tags