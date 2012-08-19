<div id="main">
	<div id="content">
		<article class="archive">
			<header>
				<h1>所有文章列表</h1>
			</header>
			%for mon in mons:
			<section>
				<h2>{{mon}}</h2>
				<ul>
				%for art in arts[mon]:
					<li>
						<a href="/article/{{art.id}}">{{art.title}}</a>
						%dt = art.posttime.split()[0]
						<span class="posttag"><time datetime="{{dt}}">{{dt}}</time></span>
					</li>
				%end
				</ul>
			</section>
			%end
		</article>
		<p class="pagebutton">
			<a class="buttoncenter" href="#doctop">回到顶部</a>
		</p>
	</div>
</div>

%rebase mainframe title="文章存档",select_name="archive"
