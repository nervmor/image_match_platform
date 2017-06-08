"""
@api {post} /image/add/ add
@apiGroup image
@apiName add
@apiDescription 导入一张网络图片到样本库中
@apiVersion 0.1.0

@apiParam {String} metadata 自定义标识数据
@apiParam {String} url 图片的地址

@apiParamExample {json} 参数示例:
{
    "metadata": 
    {
        "name" : "Jack's life", 
        "from" : "Jack.mp4",
        "size" : "1024 * 768",
        "format" : "jpg"
    },
    "url" : "http://47.93.244.54/storage/0/5643F2AC451D034“
}

@apiUse api_success
@apiSuccessExample {json} 成功:
      HTTP/1.1 200 OK
      {
        "code": 0,
        "msg": "success"
      }

@apiUse api_failure
@apiErrorExample {json} 失败:
      HTTP/1.1 400 
      {
        "code": -1,
        "msg": "image url is invalid"
      }
"""


"""
@api {post} /image/match/ match
@apiName match
@apiGroup image
@apiDescription 将该图片和库中所有图片进行匹配并返回匹配结果
@apiVersion 0.1.0

@apiParam {String} url 图片的地址
@apiParam {Number} [maxdist] 最大差距度(可选参数)

@apiParamExample {json} 参数示例:
{
    "url" : " http://47.93.244.54/storage/0/5643F2AC451D034",
    "maxdist" : 0.5
}

@apiUse api_success
@apiSuccess {Object[]} results 匹配结果
@apiSuccess {String} results.metadata 自定义信息
@apiSuccess {String} results.url 图片的url
@apiSuccess {Number} results.dist 匹配差距度得分，分数越低表示匹配度越高
@apiSuccessExample {json} 成功:
      HTTP/1.1 200 OK
      {
            "code": 0,
            "msg": "success",
            "results" : 
            [
                {
                    "metadata": 
                    {
                        "name" : "Jack's life", 
                        "from" : "Jack.mp4",
                        "size" : "1024 * 768",
                        "format" : "jpg"
                    },
                    "url" : "http://47.93.244.54/storage/0/5643F2AC451D034",
                    "dist" : 0.0
                },
                {
                    "metadata": 
                    {
                        "name" : "Tom's life", 
                        "from" : "Tom.mp4",
                        "size" : "800 * 600",
                        "format" : "png"
                    },
                    "url" : "http://47.93.244.54/storage/3/B874C76F7E120016",
                    "dist" : 0.5232368
                }
            ]
      }

@apiUse api_failure
@apiErrorExample 失败:
      HTTP/1.1 400 OK
      {
        "code": -1,
        "msg": "image url is invalid"
      }
"""


"""
@apiDefine api_success
@apiSuccess {Number} code 成功时code=0
@apiSuccess {String} msg 返回相关信息
"""

"""
@apiDefine api_failure
@apiError {Number} code 失败时code<0
@apiError {String} msg 失败原因说明
"""