<div class="article">
<h1>{{dic["title"]}}
%if admin:
<a class="control_button" href="/edit/{{dic["artid"]}}">[编辑]</a>
%end
</h1>
<div class="authortime">
	<p>{{dic["author"]}} {{dic["posttime"]}}</p>
</div>
{{!dic["content"]}}
</div>

%rebase mainframe title=dic["title"]
