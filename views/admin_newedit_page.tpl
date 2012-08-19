<div id="main">
	<script type="text/javascript">
		function post_article()
		{
			var f = document.getElementById("edit_form")
			f.action = "/admin/post-article"
			f.submit()
		}
		function draft_article()
		{
			var f = document.getElementById("edit_form")
			f.action = "/admin/draft-article"
			f.submit()
		}
	</script>
	<form id="edit_form" class="add" method="POST">
		<input type="hidden" name="artid" value="{{blog.id}}" />
		<input name="artauthor" type="hidden" value="{{blog.author}}" />
		<p>title:
			<input name="arttitle" type="text" value="{{blog.title}}" />
		</p>
		<p>content:<br/>
			<textarea name="artcontent">{{blog.content}}</textarea>	
		</p>
	</form>
	<p>
		<ul>
		<li><input type="button" value="发布文章" onclick="post_article()" /></li>
		<li><input type="button" value="保存草稿" onclick="draft_article()" /></li>
		</ul>
	</p>
</div>

%rebase adminframe title="编辑文章", select_name="new"
