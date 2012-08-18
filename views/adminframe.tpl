<!DOCTYPE html>
<html>
	<head>
		<title>{{title or "no title"}}</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<link href="/static/blog.css" rel="stylesheet" />
		<link href="/static/prettify/prettify.css" type="text/css" rel="stylesheet" />
		<script type="text/javascript" src="/static/prettify/prettify.js"></script>
	</head>
	<body onload="prettyPrint()">
		<header>
			<p><a href="/">回首页</a></p>
			<h1><a href="/admin">博客管理</a></h1>
		</header>
		<nav>
			<a href="/admin/new-article">写博客</a>
			<a href="/admin/archive">所有博客</a>
			<a href="/admin/draft">草稿箱</a>
			<a href="/admin/recycle">回收站</a>
			<a href="/logout">注销</a>
		</nav>
		%include 
		%include footer
	</body>
</html>
