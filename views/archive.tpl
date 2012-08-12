%for mon in mons:
<b>{{mon}}</b>
<ol>
%for art in arts[mon]:
	<li>
		<a href="/article/{{art["id"]}}">{{art["title"]}}</a>&nbsp;&nbsp;&nbsp;
		({{art["posttime"]}})
	%if admin:
		<a href="/del/{{art["id"]}}">[删除]</a>
	%end
	</li>
%end
</ol>
<br/>
%end

%rebase mainframe title="文章存档"
