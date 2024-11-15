<script>
	import Scrolly from "$components/helpers/Scrolly.svelte";
	import Maps from "$components/bookbans/Maps.svelte";
  
	const copy = [
	  { value: "Between 2021 and 2024, PEN America tracked <b>15,940 counts</b> of book banning incidents across <b>395 counties</b> in the United States. Florida, Iowa, and Texas accounted for nearly 80% of these bans." },
	  { value: "During the same period, <b>302 counties</b> became home to a local Moms for Liberty chapter. These are primarily concentrated in Florida, North Carolina, and Pennsylvania, but are spread out all across the map." },
	  { value: "These maps don’t perfectly overlap: only 127 counties have both a Moms for Liberty chapter and a book ban incident.<br><br>This is because the group isn’t solely drawn to red counties, where they have a better chance at advancing politically conservative policies. In fact, much of their campaign focuses on “flipping” school boards by appealing to those who feel <a href=https://www.momsforliberty.org/chapters/''>alone and unheard in their concerns</a>” in <a href='https://www.brookings.edu/articles/moms-for-liberty-where-are-they-and-are-they-winning/'>blue and purple</a>> counties, where opposition is likely to be greater." },
	];
  
	let scrollIndex;
	let steps = [0, 1, 2];  


$: console.log("Parent scrollIndex:", scrollIndex);

	</script>
  
<section id="scrolly" class="scrolly-container">
	<div class="sticky">
		<Maps scrollIndex={scrollIndex} />
	</div>

	<Scrolly bind:value={scrollIndex}>
		{#if copy.length > 0}
			{#each copy as text, i}
				<div class="step">
					<div class="step-inner">
						<p>{@html text.value}</p>
					</div>
				</div>
			{/each}
		{/if}
	</Scrolly>
	<div class="spacer" />
</section>

<style>
	#scrolly {
		position: relative;
		display: flex;
		align-items: flex-start;
		justify-content: space-between;
		width: 100%;
	}
	.scrolly-container {
		width: 100%;
		display: flex;
		justify-content: space-between;
		gap: 4rem; 
	}
	.sticky {
		position: sticky;
		top: 0;
		transition: all 1s;
		min-height: 100vh;
		max-width: 80rem;
		width: 100%; 
		margin: 0;
		z-index: 1;
		overflow-x: hidden;
		pointer-events: none;
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.step {
		height: 100vh;
		text-align: center;
		z-index: 1000;
		max-width: 30rem;
		margin: 0 auto;
		pointer-events: none;
		position: relative;
		display: flex;
		align-items: center; 
		justify-content: center; 
	}
	.step-inner {
		padding: 1rem;
		background-color: #FFFFFF;
		border: 1px solid black;
		box-shadow: 4px 6px 6px #00000046; 
	}
	:global(.step .strong) {
		color: black;
	}
	:global(.step) {
		color: black;
		font-family: var(--sans);
		padding: 0.25rem;
	}
	.spacer {
		height: 75vh;
	}

	@media (max-width: 1200px) {
		#scrolly {
			display: block; 
		}
		.scrolly-container {
			display: block; 
			gap: 0; 
		}
	}

	@media (max-width: 800px) {
		.step {
			max-width: 20rem;
		}
		.step-inner {
			font-size: 12px; /* Set font size to 12px for smaller screens */
		}
	}


</style>
