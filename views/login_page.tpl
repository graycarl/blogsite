<div id="main">
<div id="content">
	<script type="text/javascript">
		function submit_login()
		{
			var f = document.getElementById("login_form")
			f.submit()
		}
	</script>
<form id="login_form" action="/login_check" method="POST">
	%if with_err:
	<p>用户名或密码错误，请重新输入：</p>
	%end
	<p>username:<input type="text" name="username" /></p>
	<p>password:<input type="password" name="password" /></p>
</form>
<p class="pagebutton">
	<a class="bottoncenter" href="javascript:submit_login()">登陆后台</a>
</p>
</div>
</div>

%rebase mainframe title="登陆"
