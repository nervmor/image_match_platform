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
    "type": "post",
    "url": "/image/add/",
    "title": "add",
    "group": "image",
    "name": "add",
    "description": "<p>导入一张网络图片到样本库中</p>",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "metadata",
            "description": "<p>自定义标识数据</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "url",
            "description": "<p>图片的地址</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例:",
          "content": "{\n    \"metadata\": \n    {\n        \"name\" : \"Jack's life\", \n        \"from\" : \"Jack.mp4\",\n        \"size\" : \"1024 * 768\",\n        \"format\" : \"jpg\"\n    },\n    \"url\" : \"http://47.93.244.54/storage/0/5643F2AC451D034“\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "成功:",
          "content": "HTTP/1.1 200 OK\n{\n  \"code\": 0,\n  \"msg\": \"success\"\n}",
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
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "msg",
            "description": "<p>返回相关信息</p>"
          }
        ]
      }
    },
    "error": {
      "examples": [
        {
          "title": "失败:",
          "content": "HTTP/1.1 400 \n{\n  \"code\": -1,\n  \"msg\": \"image url is invalid\"\n}",
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
            "field": "msg",
            "description": "<p>失败原因说明</p>"
          }
        ]
      }
    },
    "filename": "./apidoc.py",
    "groupTitle": "image"
  },
  {
    "type": "post",
    "url": "/image/match/",
    "title": "match",
    "name": "match",
    "group": "image",
    "description": "<p>将该图片和库中所有图片进行匹配并返回匹配结果</p>",
    "version": "0.1.0",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "url",
            "description": "<p>图片的地址</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "maxdist",
            "description": "<p>最大差距度</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "参数示例:",
          "content": "{\n    \"url\" : \" http://47.93.244.54/storage/0/5643F2AC451D034\",\n    \"maxdist\" : 0.5\n}",
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
            "type": "String",
            "optional": false,
            "field": "results.metadata",
            "description": "<p>自定义信息</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "results.url",
            "description": "<p>图片的url</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "results.dist",
            "description": "<p>匹配差距度得分，分数越低表示匹配度越高</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>成功时code=0</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "msg",
            "description": "<p>返回相关信息</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "成功:",
          "content": "HTTP/1.1 200 OK\n{\n      \"code\": 0,\n      \"msg\": \"success\",\n      \"results\" : \n      [\n          {\n              \"metadata\": \n              {\n                  \"name\" : \"Jack's life\", \n                  \"from\" : \"Jack.mp4\",\n                  \"size\" : \"1024 * 768\",\n                  \"format\" : \"jpg\"\n              },\n              \"url\" : \"http://47.93.244.54/storage/0/5643F2AC451D034\",\n              \"dist\" : 0.0\n          },\n          {\n              \"metadata\": \n              {\n                  \"name\" : \"Tom's life\", \n                  \"from\" : \"Tom.mp4\",\n                  \"size\" : \"800 * 600\",\n                  \"format\" : \"png\"\n              },\n              \"url\" : \"http://47.93.244.54/storage/3/B874C76F7E120016\",\n              \"dist\" : 0.5232368\n          }\n      ]\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "失败:",
          "content": "HTTP/1.1 400 OK\n{\n  \"code\": -1,\n  \"msg\": \"image url is invalid\"\n}",
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
            "field": "msg",
            "description": "<p>失败原因说明</p>"
          }
        ]
      }
    },
    "filename": "./apidoc.py",
    "groupTitle": "image"
  }
] });