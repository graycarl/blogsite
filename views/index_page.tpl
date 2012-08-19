<div id="main">
	<div id="content">
		%for blog in blogs:
		%include article blog=blog
		%end
		<p class="pagebutton">
			<a class="buttoncenter" href="#doctop">回到顶部</a>
			%if page > 1:
			<a class="buttonleft" href="/page/{{page-1}}">上一页</a>
			%end
			%if next:
			<a class="buttonright" href="/page/{{page+1}}">下一页</a>
			%end
		</p>
	</div>
</div>

%rebase mainframe title="Carl's Blog",select_name="index"
