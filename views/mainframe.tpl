%def headcontent():
<title>{{title or "no title"}}</title>
<meta charset="utf-8" />
<link href="/static/blog.css" rel="stylesheet" />
%end

%def bodycontent():
%include navititle
%include
%end

%rebase baseframe headcontent=headcontent, bodycontent=bodycontent
