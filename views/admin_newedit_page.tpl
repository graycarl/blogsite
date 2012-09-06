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
		<select class="contypesel" name="artcontype">
			%if blog.contype == blog.contype_markdown:
			<option value="markdown" selected="selected">markdown</option>
			<option value="html">html</option>
			%elif blog.contype == blog.contype_html:
			<option value="markdown">markdown</option>
			<option value="html" selected="selected">html</option>
			%end
		</select>
		</div>
		
		<div>
		<textarea class="contentbox" name="artcontent" onkeydown="return catchTab(this, event)">{{blog.content}}</textarea>	
		</div>
	</form>
	<form id="picture_form" class="picture_form" action="/admin/up-picture" method="POST" target="upiframe" enctype="multipart/form-data">
		<iframe name="upiframe" style="display:none;"></iframe>
		<div>
		<ul id="pic_list">
		</ul>
		<p>
		<input type="file" name="imagedata" />
		<input type="submit" value="AddPicture" />
		</p>
		</div>
	</form>
	<p class="pagebutton">
	<a class="buttonleft" href="javascript:post_article()" >发布文章</a>
	<a href="javascript:draft_article()" class="buttonright">保存草稿</a>
	</p>
	</div>
</div>

%rebase adminframe title="编辑文章", select_name="new"
