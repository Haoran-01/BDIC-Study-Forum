function bindCaptchaBtnClick(){
    $("#captcha-btn").on("click",function(event){
        var email=$("input[name='email']").val();
        if(!email){
            alert("请先输入邮箱！");
            return;
        }
        //通过js发送网络请求：ajax
        $.ajax({
            url:"user/captcha",
            method:"POST",
            data:{
                "email":email
            },
            success:function(res){
                var code=res['code'];
                if(code == 200){
                    alert("验证码发送成功！");
                }else{
                    alert(res['message']);
                }
            }
        })
    });
}

//等网页文档所有元素都加载完成后再执行
$(function(){
    bindCaptchaBtnClick()
})