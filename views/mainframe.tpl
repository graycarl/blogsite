<!DOCTYPE html>
<html>
	<head>
		<title>{{title or "no title"}}</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<link href="/static/base.css" rel="stylesheet" />
		<link href="/static/main.css" rel="stylesheet" />
		<link href="/static/prettify/prettify.css" type="text/css" rel="stylesheet" />
		<script type="text/javascript" src="/static/prettify/prettify.js"></script>
		<script type="text/javascript" src="/static/my.js"></script>
	</head>
	<body onload="prettyPrint()">
		<header>
			<hgroup>
				<h1><a href="/">CARL GRAY</a></h1>
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
	</body>
</html>
