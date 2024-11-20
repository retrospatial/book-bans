<script>
	export let title = "Book Bans";
	export let description = "";
	export let url = "https://citizencodex.com";
	export let preloadFont = [];
</script>

<svelte:head>
	<title>{title}</title>
	<meta name="description" content={description} />
	<meta name="author" content="Citizen Codex" />
	<meta property="og:title" content={title} />
	<meta property="og:site_name" content="Citizen Codex" />
	<meta property="og:url" content={url} />

	<link rel="canonical" href="{url}/" />

	{#each preloadFont as href}
		<link rel="preload" {href} as="font" type="font/woff2" crossorigin />
	{/each}
</svelte:head>
