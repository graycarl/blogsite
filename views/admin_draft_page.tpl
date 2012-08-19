<div id="main">
	<div id="content">
		<article class="artmanage">
		<ul>
			%if not blogs:
			<li>
				<p class="notify">没有内容</p>
			</li>
			%else:
			%for blog in blogs:
			<li>
			<a class="title" href="/admin/edit/{{blog.id}}">{{blog.title}}</a>
			<a class="control" href="/admin/del/{{blog.id}}">[删除]</a>
			</li>
			%end
			%end
		</ul>
		</article>
	</div>
</div>

%rebase adminframe title="草稿箱", select_name="draft"
