<!DOCTYPE html>
<html>
	<head>
		<title>{{title or "no title"}}</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<link href="/static/base.css" rel="stylesheet" />
		<link href="/static/main.css" rel="stylesheet" />
		<link href="/static/code.css" rel="stylesheet" />
		<script type="text/javascript" src="/static/my.js"></script>
	</head>
	<body>
		<header>
			<hgroup>
				<h1><a name="doctop" href="/">CARL GRAY</a></h1>
				<h2>这里是灰狼的个人博客</h2>
			</hgroup>
		</header>
		%setdefault('select_name', 'None')
		<nav onload="set_selected('{{select_name}}')">
			<a id="nav_index" href="/">博客</a>
			<a id="nav_archive"href="/archive">存档</a>
			<a id="nav_about" href="/about">关于我</a>
			<a id="nav_admin" href="/admin">管理</a>
			<script type="text/javascript">
				set_selected("{{select_name}}")
			</script>
		</nav>
		%include 
		%include footer

        <script type="text/javascript">
        /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
        var disqus_shortname = 'carlblog'; // required: replace example with your forum shortname

        /* * * DON'T EDIT BELOW THIS LINE * * */
        (function () {
            var s = document.createElement('script'); s.async = true;
            s.type = 'text/javascript';
            s.src = 'http://' + disqus_shortname + '.disqus.com/count.js';
            (document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(s);
        }());
        </script>


		<!--[if lt IE 9]><div style="position:fixed;top:0;left:0;right:0;bottom:0;background:black;z-index:999999999;text-align:center;"><a href="http://godarkforie.org/upgrade"><img src="http://godarkforie.org/gonedark.jpg" alt="You are using an old version of Internet Explorer. Click here to find out more about the Going Dark For IE movement." /></a></div><![endif]-->		
	</body>
</html>
