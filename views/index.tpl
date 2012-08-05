<ol>
%for t in titles:
	<li><a href="/article/{{t["id"]}}">{{t["title"]}}</a>({{t["posttime"]}})</li>
%end
</ol>

%rebase mainframe title="文章列表"
