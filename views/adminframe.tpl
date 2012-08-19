<!DOCTYPE html>
%setdefault('select_name', 'None')
<html>
	<head>
		<title>{{title or "no title"}}</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<link href="/static/base.css" rel="stylesheet" />
		<link href="/static/admin.css" rel="stylesheet" />
		<link href="/static/prettify/prettify.css" type="text/css" rel="stylesheet" />
		<script type="text/javascript" src="/static/prettify/prettify.js"></script>
		<script type="text/javascript" src="/static/my.js"></script>
	</head>
	<body onload="prettyPrint()">
		<header>
			<p><a href="/">回首页</a></p>
			<h1><a href="/admin">博客管理</a></h1>
		</header>
		<nav >
			<a id="nav_new" href="/admin/new-article">写博客</a>
			<a id="nav_archive" href="/admin/archive">所有博客</a>
			<a id="nav_draft" href="/admin/draft">草稿箱</a>
			<a id="nav_recycle" href="/admin/recycle">回收站</a>
			<a id="nav_logout" href="/logout">注销</a>
			<script type="text/javascript">
				set_selected("{{select_name}}")
			</script>
		</nav>
		%include 
		%include footer
	</body>
</html>
