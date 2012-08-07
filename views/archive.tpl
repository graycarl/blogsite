%for mon in mons:
<b>{{mon}}</b>
<ol>
%for art in arts[mon]:
	<li><a href="/article/{{art["id"]}}">{{art["title"]}}</a>({{art["posttime"]}})</li>
%end
</ol>
<br/>
%end

%rebase mainframe title="文章存档"
