<form action="/save_article" method="POST">
<input type="hidden" name="artid" />
<p>title:<input type="text" name="arttitle" /></p>
<input type="hidden" name="artauthor" />
<p>content:<br/><textarea name="artcontent" rows="10" cols="80" ></textarea></p>
<p><input type="submit" name="commit" value="保存" /></p>
</form>

%rebase mainframe title="编写文章"
