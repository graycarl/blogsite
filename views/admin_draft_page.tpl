<div id="main">
	<div id="content">
		<p>草稿箱</p>
		<ul>
			%if not blogs:
			<li>
				<p>没有内容</p>
			</li>
			%else:
			%for blog in blogs:
			<li><p>
			<a href="/admin/edit/{{blog.id}}">{{blog.title}}</a>
			<a href="/admin/del/{{blog.id}}">[删除]</a>
			</p></li>
			%end
			%end
		</ul>
	</div>
</div>

%rebase adminframe title="草稿箱", select_name="draft"
