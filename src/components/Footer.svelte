<script>
	import sticker from "$svg/cclogo_white.svg";

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
		text-decoration-color: #F4E48A; 
	}

	a:hover {
		background-color: #F4E48A; 
		color: var(--color-fg); 
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

</style>
