<script>
	import sticker from "$svg/cclogo_white.svg";

	const links = [
		{ name: "about", url: "https://www.citizencodex.com/about-us" },
		{ name: "our stories", url: "https://www.citizencodex.com/our-stories" },
		{ name: "linkedin", url: "https://www.linkedin.com/company/citizen-codex/" },
	];

</script>

<footer>

	<section class="about">
		<div class="sticker">
			<a href="https://citizencodex.com" target="_self">
				{@html sticker}
			</a>	
		</div>

		<p class="text">
			<a href="https://citizencodex.com" target="_self">Citizen Codex</a> is a data design studio sharing insights and data more clearly to the world.
		</p>
		<p class="text">
			Reach out: <a href="mailto:hello@citizencodex.com">hello@citizencodex.com</a>

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
		color: white;
		text-decoration: underline;
		text-decoration-color: #F4E48A; 
	}

	a:hover {
		background-color: #F4E48A; 
		color: black; 
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

	.text {
		color: white;
	}

	.links ul {
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
		align-items: center;
		padding: 0;
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
		margin: auto 0.5em;
	}

</style>
