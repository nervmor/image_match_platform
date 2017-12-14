define({ "api": [
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./html/main.js",
    "group": "T__local_image_match_platform_code_web_apidoc_html_main_js",
    "groupTitle": "T__local_image_match_platform_code_web_apidoc_html_main_js",
    "name": ""
  },
  {
    "type": "result",
    "url": "/engine/result",
    "title": "*code值说明*",
    "group": "_result",
    "name": "code___",
    "description": "<p>返回码code以及对应描述</p>",
    "version": "0.1.0",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "0",
            "description": "<p>成功</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "-1",
            "description": "<p>请求的json格式不正确</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "-2",
            "description": "<p>请求的参数不正确</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "-3",
            "description": "<p>请求的HTTP Method不支持</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "-4",
            "description": "<p>请求的图片地址无法访问</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "-5",
            "description": "<p>请求参数maxdist不正确</p>"
          }
        ]
      }
    },
    "filename": "./apidoc.py",
    "groupTitle": "_result"
  },
  {
    "type": "post",
    "url": "/engine/match/",
    "title": "match",
    "group": "engine",
    "name": "match",
    "description": "<p>对两组图片进行匹配并输出差距值</p>",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String[]",
            "optional": false,
            "field": "url_src",
            "description": "<p>对比图片数组</p>"
          },
          {
            "group": "Parameter",
            "type": "String[]",
            "optional": false,
            "field": "url_dst",
            "description": "<p>被对比图片数组</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例:",
          "content": "{\n    \"url_src\" :\n    [\n        \"http://www.nervmor.com/api/img/8c186f92ec604040962b2490a0d2ecfa\",\n        \"http://www.nervmor.com/api/img/a87ff679a2f3e71d9181a67b7542122c\"\n    ],\n    \"url_dst\" : \n    [\n        \"http://www.nervmor.com/api/img/622162fa514365fa3867ddce401378a7\",\n        \"http://www.nervmor.com/api/img/67f1bf7400e3834476865298d3c3b179\",\n        \"http://www.nervmor.com/api/img/89b689f47afb5779ecfe8b7e41477e02\"\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Object[]",
            "optional": false,
            "field": "results",
            "description": "<p>匹配结果</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "results.url_src_value",
            "description": "<p>src图片对dst图片组的匹配结果</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "results.url_src_value.url_dst_value",
            "description": "<p>src图片对dst图片组匹配的差距值</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>成功时code=0</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "成功:",
          "content": "HTTP/1.1 200 OK\n{\n    \"code\": 0,\n    \"results\":\n    {\n        \"http://www.nervmor.com/api/img/8c186f92ec604040962b2490a0d2ecfa\" : \n        {\n            \"http://www.nervmor.com/api/img/622162fa514365fa3867ddce401378a7\" : 0.332423432,\n            \"http://www.nervmor.com/api/img/67f1bf7400e3834476865298d3c3b179\" : 0.25277,\n            \"http://www.nervmor.com/api/img/89b689f47afb5779ecfe8b7e41477e02\" : 0.68254\n        },\n\n        \"http://www.nervmor.com/api/img/a87ff679a2f3e71d9181a67b7542122c\" : \n        {\n            \"http://www.nervmor.com/api/img/622162fa514365fa3867ddce401378a7\" : 0.51848,\n            \"http://www.nervmor.com/api/img/67f1bf7400e3834476865298d3c3b179\" : 0.025954,\n            \"http://www.nervmor.com/api/img/89b689f47afb5779ecfe8b7e41477e02\" : 0.12179\n        }\n    }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "失败:",
          "content": "HTTP/1.1 400 \n{\n    \"code\": -1,\n    \"error\": \"image url is invalid\"\n}",
          "type": "json"
        }
      ],
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>失败时code&lt;0</p>"
          },
          {
            "group": "Error 4xx",
            "type": "String",
            "optional": false,
            "field": "error",
            "description": "<p>失败原因说明</p>"
          }
        ]
      }
    },
    "filename": "./apidoc.py",
    "groupTitle": "engine"
  },
  {
    "type": "post",
    "url": "/feature/phash/add/",
    "title": "add",
    "group": "feature",
    "name": "add",
    "description": "<p>录入特征</p>",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "pic_url",
            "description": "<p>图片的地址</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "feat_x",
            "description": "<p>特征区域的X坐标</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "feat_y",
            "description": "<p>特征区域的Y坐标</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "feat_w",
            "description": "<p>特征区域的宽度</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "feat_h",
            "description": "<p>特征区域的高度</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "feat_x_range",
            "description": "<p>特征区域的X坐标的浮动范围</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "feat_y_range",
            "description": "<p>特征区域的Y坐标的浮动范围</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "feat_w_range",
            "description": "<p>特征区域的宽度的浮动范围</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "feat_h_range",
            "description": "<p>特征区域的高度的浮动范围</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "metadata",
            "description": "<p>自定义标识数据(可选参数)</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例:",
          "content": "{\n    \"url\" : \"http://www.nervmor.com/api/img/8c186f92ec604040962b2490a0d2ecfa\",\n    \"feat_x\" : 100,\n    \"feat_y\" : 80,\n    \"feat_x_range\" : 5,\n    \"feat_y_range\" : 5,\n    \"feat_w\" : 50,\n    \"feat_h\" : 50,\n    \"feat_w_range\" : 3,\n    \"feat_h_range\" : 3,\n        \"metadata\": \n    {\n        \"name\" : \"Jack's life\", \n        \"from\" : \"Jack.mp4\",\n        \"size\" : \"1024 * 768\",\n        \"format\" : \"jpg\"\n    }\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "成功:",
          "content": "HTTP/1.1 200 OK\n{\n    \"code\": 0,\n}",
          "type": "json"
        }
      ],
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>成功时code=0</p>"
          }
        ]
      }
    },
    "error": {
      "examples": [
        {
          "title": "失败:",
          "content": "HTTP/1.1 400 \n{\n    \"code\": -1,\n    \"error\": \"image url is invalid\"\n}",
          "type": "json"
        }
      ],
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>失败时code&lt;0</p>"
          },
          {
            "group": "Error 4xx",
            "type": "String",
            "optional": false,
            "field": "error",
            "description": "<p>失败原因说明</p>"
          }
        ]
      }
    },
    "filename": "./apidoc.py",
    "groupTitle": "feature"
  },
  {
    "type": "get",
    "url": "/img/[md5]?t=1",
    "title": "del",
    "name": "del",
    "group": "img",
    "description": "<p>删除图片</p>",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "t",
            "description": "<p>t=1时删除图片</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例:",
          "content": "http://www.nervmor.com/api/img/f5307fa900eb682e57d22a29c78a4ff5?t=1 删除图片",
          "type": "json"
        }
      ]
    },
    "filename": "./apidoc.py",
    "groupTitle": "img"
  },
  {
    "type": "get",
    "url": "/img/[md5]",
    "title": "get",
    "name": "get",
    "group": "img",
    "description": "<p>根据参数得到相应的图片</p>",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "x",
            "description": "<p>截取局部图片时的x坐标</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "y",
            "description": "<p>截取局部图片时的y坐标</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "l",
            "description": "<p>截取局部图片时的长度</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "w",
            "description": "<p>截取局部图片时的宽度</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例:",
          "content": "http://www.nervmor.com/api/img/f5307fa900eb682e57d22a29c78a4ff5?x=100&y=80&l=40&w=40 截取坐标为[100,80]尺寸为40*40的局部图片\nhttp://www.nervmor.com/api/img/f5307fa900eb682e57d22a29c78a4ff5?x=0&y=0&l=60&w=60 截取坐标为[0,0](左上角)尺寸为60*60的局部图片\nhttp://www.nervmor.com/api/img/f5307fa900eb682e57d22a29c78a4ff5 返回原图",
          "type": "json"
        }
      ]
    },
    "filename": "./apidoc.py",
    "groupTitle": "img"
  },
  {
    "type": "post",
    "url": "/img/",
    "title": "upload",
    "name": "upload",
    "group": "img",
    "description": "<p>上传图片到图片服务器</p>",
    "version": "0.1.0",
    "parameter": {
      "examples": [
        {
          "title": "参数示例:",
          "content": "1. 使用标准的HTTP multitype/form 形式上传\n2. 使用二进制流的形式上传:HTTP头部需要加入Content-Type:jpg/png/[..]，body部分为文件的二进制流",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "ret",
            "description": "<p>是否成功</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "info",
            "description": "<p>图片信息</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "info.md5",
            "description": "<p>图片的MD5</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "info.size",
            "description": "<p>图片的大小</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "成功:",
          "content": "HTTP/1.1 200 OK\n{\n      \"ret\": true,\n      \"info\" : \n      {\n          \"md5\": \"f5307fa900eb682e57d22a29c78a4ff5\",\n          \"size\": 281356\n      }\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "Boolean",
            "optional": false,
            "field": "ret",
            "description": "<p>是否成功</p>"
          },
          {
            "group": "Error 4xx",
            "type": "Object",
            "optional": false,
            "field": "error",
            "description": "<p>错误信息</p>"
          },
          {
            "group": "Error 4xx",
            "type": "Number",
            "optional": false,
            "field": "error.code",
            "description": "<p>错误代码</p>"
          },
          {
            "group": "Error 4xx",
            "type": "String",
            "optional": false,
            "field": "error.message",
            "description": "<p>错误说明</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "成功:",
          "content": "HTTP/1.1 200 OK\n{\"ret\":false,\"error\":{\"code\":0,\"message\":\"Internal error.\"}}\n{\"ret\":false,\"error\":{\"code\":1,\"message\":\"File type not support.\"}}\n{\"ret\":false,\"error\":{\"code\":2,\"message\":\"Request method error.\"}}\n{\"ret\":false,\"error\":{\"code\":3,\"message\":\"Access error.\"}}\n{\"ret\":false,\"error\":{\"code\":4,\"message\":\"Request body parse error.\"}}\n{\"ret\":false,\"error\":{\"code\":5,\"message\":\"Content-Length error.\"}}\n{\"ret\":false,\"error\":{\"code\":6,\"message\":\"Content-Type error.\"}}\n{\"ret\":false,\"error\":{\"code\":7,\"message\":\"File too large.\"}}",
          "type": "json"
        }
      ]
    },
    "filename": "./apidoc.py",
    "groupTitle": "img"
  }
] });
