<ol start="0">
	<li>
		<a href="/new">&lt;new article&gt;</a>
	</li>
%for t in titles:
	<li>
		<a href="/article/{{t["id"]}}">{{t["title"]}}</a>&nbsp;&nbsp;&nbsp;
		({{t["posttime"]}})
	%if admin:
		<a class="control_button" href="/del/{{t["id"]}}">[删除]</a>		
	%end
	</li>
%end
</ol>

%rebase mainframe title="文章列表",admin=admin
