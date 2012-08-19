<div id="main">
	<div id="content">
		<article class="artmanage">
		<section>
		<ul>
			%if not blogs:
			<li>
				<p class="notify">没有内容</p>
			</li>
			%else:
			%for blog in blogs:
			<li>
				<a class="title">{{blog.title}}</a>
				<a class="control" href="/admin/post-article/{{blog.id}}">[重新发布]</a>
				<a class="control" href="/admin/edit/{{blog.id}}">[编辑]</a>
				<a class="control" href="/admin/draft-article/{{blog.id}}">[移至草稿箱]</a>
				<a class="control" href="/admin/del/{{blog.id}}/clean">[彻底删除]</a>
			</li>
			%end
			%end
		</ul>
		</section>
		</article>
	</div>
</div>

%rebase adminframe title="回收站", select_name="recycle"
