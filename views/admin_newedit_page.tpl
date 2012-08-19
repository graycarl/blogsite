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
	<div id="content">
	<form id="edit_form" class="edit_form" method="POST">
		<input type="hidden" name="artid" value="{{blog.id}}" />
		<input name="artauthor" type="hidden" value="{{blog.author}}" />
		<div>
		<input class="titlebox" name="arttitle" type="text" value="{{blog.title}}" />
		</div>
		<div>
		<textarea rows="20" class="contentbox" name="artcontent">{{blog.content}}</textarea>	
		</div>
	</form>
	<p class="pagebutton">
	<a class="buttonleft" href="javascript:post_article()" >发布文章</a>
	<a href="javascript:draft_article()" class="buttonright">保存草稿</a>
	</p>
	</div>
</div>

%rebase adminframe title="编辑文章", select_name="new"
