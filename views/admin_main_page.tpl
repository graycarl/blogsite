<div id="main">
	<div id="content">
	<article class="artmanage">
		<section>
		<ul>
			%for blog in blogs:
			<li>
				<a class="title" href="/article/{{blog.id}}">{{blog.title}}</a>
				<a class="control" href="/admin/edit/{{blog.id}}">[编辑]</a>
			</li>
			%end
		</ul>
		</section>
	</article>
	</div>
</div>

%rebase adminframe title="博客管理"
