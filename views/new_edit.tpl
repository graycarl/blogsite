<form action="/save_article" method="POST">
<input type="hidden" name="artid" value="{{dic['artid']}}" />
<p>title:<input type="text" name="arttitle" value="{{dic['title']}}" /></p>
<input type="hidden" name="artauthor" value="{{dic['author']}}" />
<p>content:<br/><textarea name="artcontent" rows="10" cols="80" >{{dic['content']}}</textarea></p>
<p><input type="submit" name="commit" value="保存" /></p>
</form>

%rebase mainframe title="编写文章"
