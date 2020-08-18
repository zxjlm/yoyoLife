var ENTER_KEY = 13;
var edit_id = -1;

// item相关

function new_item() {
    var $input = $('#item-input');
    var value = $input.val().trim();

    $input.focus().val('');
    $.ajax({
        type: 'POST',
        url: new_item_url,
        data: JSON.stringify({'body': value}),
        contentType: 'application/json;charset=UTF-8',
        success: function (data) {
            $('#flag-hidden').remove()

            toastr.success(data.message)
            $('#item_list').append(data.html);
        },
        error: function () {
            toastr.error('fail to add')
        }
    });
}

function del_item(_id) {
    $.ajax({
        type: 'DELETE',
        url: delete_item_url + _id,
        success: function (data) {
            if ($('#item').length === 0) {
                $('#item_list').append("<div class=\"ui info message\" id=\"flag-hidden\">\n" +
                    "            <i class=\"close icon\"></i>\n" +
                    "            <div>暂时还没有安排哦~</div>\n" +
                    "        </div>");
            }

            toastr.success(data.message)
            $('#body' + _id).parent().remove()
        },
        error: function () {
            toastr.error('fail to change toggle')
        }
    })
}

function edit_modal(_id) {
    document.getElementById("edit_todo_body").value = document.getElementById('body' + _id).innerText;
    edit_id = _id
    $('.ui.modal.todo').modal('show');
}

function edit_item() {
    var value = document.getElementById("edit_todo_body").value.trim();
    if (value === document.getElementById('body' + edit_id).innerText.trim()) {
        toastr.info('todo content unchanged')
        return
    }

    $.ajax({
        type: 'POST',
        url: edit_item_url,
        data: JSON.stringify({'body': value, 'id': edit_id}),
        contentType: 'application/json;charset=UTF-8',
        success: function (data) {
            document.getElementById('body' + edit_id).innerText = document.getElementById("edit_todo_body").value.trim()
            toastr.success(data.message)
            // activeM();
            // refresh_count();
        },
        error: function () {
            toastr.error('fail to edit')
        }
    })
}

function toggle_item(_id) {
    $.ajax({
        type: 'GET',
        url: toggle_item_url + _id,
        success: function (data) {
            toastr.success(data.message)
            let tmp = $('#status_' + _id)
            if (data.status) {
                tmp.addClass('check')
            } else {
                tmp.removeClass('check')
            }
        },
        error: function () {
            toastr.error('fail to change toggle')
        }
    })
}


//------------------------------------------分割线---------------------------------------------
//Bills相关

function del_bill(_id) {
    $.ajax({
        type: 'DELETE',
        url: delete_bill_url + _id,
        success: function (data) {
            if ($('#bill').length === 0) {
                $('#bill_list').append("<div class=\"ui info message\" id=\"flag-hidden\">\n" +
                    "            <i class=\"close icon\"></i>\n" +
                    "            <div>暂时还没有安排哦~</div>\n" +
                    "        </div>");
            }

            toastr.success(data.message)
            $('#bill-main-1').remove()
        },
        error: function () {
            toastr.error('fail to change toggle')
        }
    })
}

function edit_bill_modal(_id) {
    if (_id === -1) {
        edit_id = _id
        document.getElementById("edit_bill_body").value = "";
        document.getElementById("edit_bill_money").value = "";
        $('#edit_bill_type')[0].innerText = "类型选择";
        $('#date1').calendar('set date', Date().toLocaleString());
    } else {
        document.getElementById("edit_bill_body").value = document.getElementById('bill-payfor-' + _id).innerText;
        document.getElementById("edit_bill_money").value = document.getElementById('bill-money-' + _id).innerText;
        $('#edit_bill_type')[0].innerText = document.getElementById('bill-type-' + _id).innerText;
        $('#date1').calendar('set date', document.getElementById('bill-date-' + _id).innerText);
        edit_id = _id
    }
    $('.ui.mini.modal.bill').modal('show');
    $('#date1').calendar({
        on: 'hover'
    });
    $('.ui.floating').dropdown();
}

function edit_bill() {
    let type = $('#edit_bill_type')[0].textContent;
    let money = $('#edit_bill_money')[0].valueAsNumber;
    let payfor = $('#edit_bill_body')[0].value.trim();
    let date = $('#date1').calendar('get date');

    if (edit_id === -1) {
        $.ajax({
            type: 'POST',
            url: new_bill_url,
            data: JSON.stringify({'body': payfor, 'id': edit_id, 'type': type, 'money': money, 'date': date}),
            contentType: 'application/json;charset=UTF-8',
            success: function (data) {
                // $('#bills-t-body').append(data.html)
                bill_onload()
                toastr.success(data.message)
            },
            error: function () {
                toastr.error('fail to edit')
            }
        })
    } else {
        $.ajax({
            type: 'POST',
            url: edit_bill_url,
            data: JSON.stringify({'body': payfor, 'id': edit_id, 'type': type, 'money': money, 'date': date}),
            contentType: 'application/json;charset=UTF-8',
            success: function (data) {
                bill_onload()
                toastr.success(data.message)
            },
            error: function () {
                toastr.error('fail to edit')
            }
        })
    }

}
