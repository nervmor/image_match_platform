pic_srv_url = "http://www.nervmor.com:4869/";
cur_upload_files = [];
result_str = [
  { "-1": "请求的json数据不正确" },
  { "-2": "请求参数不正确" },
  { "-3": "请求的HTTP方法不支持" },
  { "-4": "图片地址无法访问" },
  { "-5": "参数maxdist不正确" },
];

function reset_state() {
  $("#pic_op_cont").hide();
  $("#res_sec").hide();
  cur_upload_files = [];
  $("#match_btn").attr("disabled", false);
  $("#remove_btn").attr("disabled", false);
}
function show_loading(text) {
  $("#loading_icon").addClass("fa fa-spinner fa-spin");
  $("#loading_modal").modal('toggle');
}
function complete_loading() {
  $("#loading_icon").removeClass("fa fa-spinner fa-spin");
  $("#loading_modal").modal('hide');
}
function create_match_result_item(url, dist, metadata) {
  $list = $("<div class=\"list\"></div>");
  $img = $("<img class=\"list-icon\"></img>");
  $img.attr("src", url);
  $list.append($img);

  $title = $("<div class=\"list-title\"></div>");
  $title.text("[自定义信息]---> " + metadata);
  $list.append($title);

  $dist = $("<div class=\"list-subtitle\"></div>");
  $dist.text("[差异度数值]---> " + String(dist));
  $list.append($dist);

  return $list;
}

/******************************** loading ui  *******************************/


toastr.options = {
  "closeButton": false,
  "debug": false,
  "newestOnTop": false,
  "progressBar": false,
  "positionClass": "toast-bottom-center",
  "preventDuplicates": false,
  "onclick": null,
  "showDuration": "300",
  "hideDuration": "1000",
  "timeOut": "5000",
  "extendedTimeOut": "1000",
  "showEasing": "swing",
  "hideEasing": "linear",
  "showMethod": "fadeIn",
  "hideMethod": "fadeOut"
}
/******************************** file-upload  *******************************/
$("#file-upload").fileinput(
  {
    "uploadUrl": pic_srv_url,
    "language": "zh",
    "maxFileCount": 10
  });

$("#file-upload").on("fileuploaded", function (event, data, previewId, index) {
  res = data.response;
  if (!res["ret"]) {
    toastr.error("图片服务器处理失败");
    return;
  }
  md5 = res["info"]["md5"];
  pic_url = pic_srv_url + md5;
  cur_upload_files.push(pic_url);
  if (cur_upload_files.length == 1) {
    $("#pic_op_cont").show();
  } else {
    $("#match_btn").attr("disabled", true);
    $("#remove_btn").attr("disabled", true);
  }
})
$('#file-upload').on('filebatchuploaderror', function (event, data, msg) {
  toastr.error("上传图片失败");
  reset_state();
});
$("#file-upload").on("filebatchselected", function (event, files) {
  reset_state();
});

$("#file-upload").on("filecleared", function (event, data, msg) {
  reset_state();
});

/******************************** btn event  *******************************/
$("#metadata_yes_btn").on("click", function () {
  $.each(cur_upload_files, function (i, pic_url) {
    metadata = $("#metadata_edit").val();
    if (metadata.length == 0) {
      cur_date = new Date();
      metadata = "浏览器于" + cur_date.toLocaleString() + "录入";
    }
    req_data = {
      "url": pic_url,
      "metadata": metadata
    };
    $("#metadata_modal").modal('hide');
    $.ajax({
      type: "post",
      url: "http://www.nervmor.com/api/image/add/",
      data: JSON.stringify(req_data),
      dataType: "json",
      beforeSend: function () {
        show_loading("正在入库");
      },
      success: function (data, textStatus) {
        if (data["code"] != 0) {
          toastr.error(result_str[String(data["code"])]);
        } else {
          toastr.success("图片入库成功");
        }
        complete_loading();
      },
      error: function (XMLHttpRequest, textStatus, errorThrown) {
        toastr.error("图片入库失败");
        complete_loading();
      }
    });
  });
});

$("#match_btn").on("click", function () {
  req_data = {
    "url": cur_upload_files[0]
  };
  $.ajax({
    type: "post",
    url: "http://www.nervmor.com/api/image/match/",
    data: JSON.stringify(req_data),
    dataType: "json",
    beforeSend: function () {
      $("#res_lst").empty();
      show_loading("正在匹配");
    },
    success: function (data, textStatus) {
      do {
        if (data["code"] != 0) {
          toastr.error(result_str[String(data["code"])]);
          break;
        }
        if (!data["result"]) {
          toastr.error("[result] not found");
          break;
        }
        result = data["result"];
        if (result.length == 0) {
          toastr.warning("没有匹配到相似的图片");
          break;
        }
        $("#res_sec").show();
        $.each(result, function (i, r) {
          $li = create_match_result_item(r["url"], r["dist"], r["metadata"]);
          $("#res_lst").append($li);
        });
        toastr.success("图片匹配成功");
      } while (false);
      complete_loading();
    },
    error: function (XMLHttpRequest, textStatus, errorThrown) {
      complete_loading();
    }
  });
});

$("#remove_btn").on("click", function () {
  req_data = {
    "url": cur_upload_files[0]
  };
  $.ajax({
    type: "post",
    url: "http://www.nervmor.com/api/image/remove/",
    data: JSON.stringify(req_data),
    dataType: "json",
    beforeSend: function () {
      show_loading("正在移除");
    },
    success: function (data, textStatus) {
      if (data["code"] != 0) {
        toastr.error(result_str[String(data["code"])]);
      } else {
        result = data["result"];
        del_cnt = result["delcnt"];
        if (del_cnt != 0) {
          toastr.success("成功移除了[" + String(del_cnt) + "个]图片");
        } else {
          toastr.warning("图片库中没有找到该图片");
        }
      }
      complete_loading();
    },
    error: function (XMLHttpRequest, textStatus, errorThrown) {
      toastr.error("图片移除失败");
      complete_loading();
    }
  });
});
