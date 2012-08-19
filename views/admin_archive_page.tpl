<div id="main">
	<div id="content">
	<article class="archive">
	<section>
	%for mon in mons:
		<h2>{{mon}}</h2>
		<ul>
		%for blog in titles[mon]:
			<li>
				<a class="title" href="/article/{{blog.id}}" target="_blank">{{blog.title}}</a>
				<a class="control" href="/admin/edit/{{blog.id}}">[编辑]</a>
				<a class="control" href="/admin/del/{{blog.id}}">[删除]</a>
			</li>
		%end
		</ul>
	%end
	</section>
	</article>
	</div>
</div>

%rebase adminframe title="所有博客", select_name="archive"
