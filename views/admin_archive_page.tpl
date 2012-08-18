<div id="main">
	<div id="content">
	%for mon in mons:
		<b>{{mon}}</b>
		<ol>
		%for blog in titles[mon]:
			<li><p>
				<a href="/article/{{blog.id}}" target="_blank">{{blog.title}}</a>
				<a href="/admin/edit/{{blog.id}}">[编辑]</a>
				<a href="/admin/del/{{blog.id}}">[删除]</a>
			</p></li>
		%end
		</ol>
	%end
	</div>
</div>

%rebase adminframe title="所有博客"
