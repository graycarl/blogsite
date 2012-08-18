<div id="main">
	<div id="content">
	<p>最近的文章：</p>
	<ul>
		%for blog in blogs:
		<li>
		<p>
			<a href="/article/{{blog.id}}">{{blog.title}}</a>
			<a href="/admin/edit/{{blog.id}}">[编辑]</a>
		</p>
		</li>
		%end
	</ul>
	</div>
</div>

%rebase adminframe title="博客管理"
