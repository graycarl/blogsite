%def headcontent():
<title>{{title or "no title"}}</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="/static/blog.css" rel="stylesheet" />
<link href="/static/prettify/prettify.css" type="text/css" rel="stylesheet" />
<script type="text/javascript" src="/static/prettify/prettify.js"></script>
%end

%def bodycontent():
%setdefault("admin", False)
%include navititle admin=admin
%include
%end

%rebase baseframe headcontent=headcontent, bodycontent=bodycontent
