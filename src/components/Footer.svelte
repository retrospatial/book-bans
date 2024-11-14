<script>
	import sticker from "$svg/cclogo_white.svg";

	const links = [
		{ name: "about", url: "https://pudding.cool/about" },
		{ name: "facebook", url: "https://facebook.com/pudding.viz/" },
		{ name: "twitter", url: "https://twitter.com/puddingviz/" },
		{
			name: "instagram",
			url: "https://www.instagram.com/the.pudding"
		},
		{ name: "patreon", url: "https://patreon.com/thepudding/" },
		{ name: "privacy", url: "https://pudding.cool/privacy/" },
		{ name: "newsletter", url: "https://pudding.cool/subscribe" },
		{ name: "rss", url: "https://pudding.cool/feed/index.xml" }
	];

</script>

<footer>
	<section class="about">
		<div class="sticker">
			<a href="https://citizencodex.com" target="_self">
				{@html sticker}
			</a>	
		</div>
		<p>
			<a href="https://citizencodex.com" target="_self">Citizen Codex</a> is a data design studio sharing insights and data more clearly to the world.
		</p>
		<p>
			Reach out: email@email.com
		</p>
	</section>

	<section class="links">
		<ul>
			{#each links as link}
				<li>
					<a href={link.url} target="_self">
						<span>{link.name.toUpperCase()}</span>
					</a>
				</li>
			{/each}
		</ul>
	</section>
</footer>

<style>
	footer {
		background-color: #303334;
		color: white;
		font-family: var(--sans);
		padding: 2em;
		margin-top: 4em;
	}

	a,
	a:visited {
		color: var(--color-bg);
		text-decoration: underline;
		text-decoration-color: #F4E48A; /* Underline color */
	}

	a:hover {
		background-color: #F4E48A; /* Change background color on hover */
		color: var(--color-fg); /* Optional: Adjust the text color when hovered */
	}

	.sticker {
		max-width: 15em;
		margin: 4em auto;
	}

	.about {
		margin: 3rem auto;
		margin-top: 0;
		text-align: center;
	}

	.links ul {
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
	}

	.links li {
		display: flex;
		padding: 0.5em 1em;
	}

	.links a {
		display: flex;
		border: none;
		align-items: center;
		text-decoration: none;
	}

	.links span {
		margin-left: 0.5em;
	}

</style>
