<div id="main">
	<div id="content">
		<p>已删除的文章：</p>
		<ul>
			%for blog in blogs:
			<li>
			<p>{{blog.title}}
				<a href="/admin/post-article/{{blog.id}}">[重新发布]</a>
				<a href="/admin/edit/{{blog.id}}">[编辑]</a>
				<a href="/admin/draft-article/{{blog.id}}">[移至草稿箱]</a>
				<a href="/admin/del/{{blog.id}}/clean">[彻底删除]</a>
			</p>
			</li>
			%end
		</ul>
	</div>
</div>

%rebase adminframe title="回收站", select_name="recycle"
