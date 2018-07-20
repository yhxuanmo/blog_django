/*

@Name：不落阁整站模板源码 
@Author：Absolutely 
@Site：http://www.lyblogs.cn

*/

prettyPrint();
layui.use(['form', 'layedit'], function () {
    var form = layui.form();
    var $ = layui.jquery;
    var layedit = layui.layedit;

    //评论和留言的编辑器
    var editIndex = layedit.build('remarkEditor', {
        height: 150,
        tool: ['face', '|', 'left', 'center', 'right', '|', 'link'],
    });
    //评论和留言的编辑器的验证
    layui.form().verify({
        content: function (value) {
            value = $.trim(layedit.getText(editIndex));
            if (value == "") return "自少得有一个字吧";
            layedit.sync(editIndex);
        }
    });

    //监听评论提交
    form.on('submit(formRemark)', function (data) {
        var index = layer.load(1);
        //模拟评论提交
        var csrf = $('input[name="csrfmiddlewaretoken"]').val()
        var comment = data.field.editorContent;
        var comment_data = {
            'comment':comment,
            'reader_name':'游客',
            'head_img':'/static/images/Absolutely.jpg'
        };

        $.ajax({
            url:'comment/',
            type:'post',
            datatype:'json',
            data:comment_data,
            headers:{'X-CSRFToken':csrf},
            success:function (msg) {
                if (msg.code == 200){
                    layer.close(index);
                    var content = data.field.editorContent;
                    var html = '<li><div class="comment-parent"><img src="/static/images/Absolutely.jpg"alt="absolutely"/><div class="info"><span class="username">'+ comment_data.reader_name +'</span><span class="time">'+ msg.comment_time + '</span></div><div class="content">' + content + '</div></div></li>';
                    $('.blog-comment').append(html);
                    $('#remarkEditor').val('');
                    editIndex = layui.layedit.build('remarkEditor', {
                        height: 150,
                        tool: ['face', '|', 'left', 'center', 'right', '|', 'link'],
                    });
                    layer.msg("评论成功", { icon: 1 });
                }

            },
            error:function () {
                alert('提交失败')
            }
        });

        return false;
    });
});