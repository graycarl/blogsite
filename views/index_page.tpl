<div id="main">
	%if page > 1:
	<p>Page {{page}}</p>
	%end
	<div id="content">
		%for blog in blogs:
		%include article blog=blog
		%end
	</div>
	<ul>
		%if page > 1:
		<a href="/page/{{page-1}}">上一页</a>
		%end
		%if next:
		<a href="/page/{{page+1}}">下一页</a>
		%end
	</ul>
</div>

%rebase mainframe title="Carl's Blog",select_name="index"
