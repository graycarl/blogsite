<div id="main">
	<div id="content">
		%for mon in mons:
		<b>{{mon}}</b>
		<ol>
		%for art in arts[mon]:
			<li>
				<a href="/article/{{art.id}}">{{art.title}}</a>&nbsp;&nbsp;&nbsp;
				({{art.posttime}})
			</li>
		%end
		</ol>
		<br/>
		%end
	</div>
</div>

%rebase mainframe title="文章存档",select_name="archive"
