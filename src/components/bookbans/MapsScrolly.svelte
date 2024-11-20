<script>
	import Scrolly from "$components/helpers/Scrolly.svelte";
	import Maps from "$components/bookbans/Maps.svelte";
  
	const copy = [
	  { value: "Between 2021 and 2024, PEN America tracked <span style='background-color: #FFECE9; padding: 4px 4px; border-radius: 5px;'><b>15,940 counts</b></span> of <span style='background-color: #FFECE9; padding: 4px 4px; border-radius: 5px;'><b>book banning incidents</b></span> across <span style='background-color: #FFECE9; padding: 4px 4px; border-radius: 5px;'><b>395 counties</b></span> in the United States. Florida, Iowa, and Texas accounted for nearly 80% of these bans." },
	  { value: "During the same period, <span style='background-color: #DFEBF9; padding: 4px 4px; border-radius: 5px;'><b>302 counties</b></span> became home to a local <span style='background-color: #DFEBF9; padding: 4px 4px; border-radius: 5px;'><b>Moms for Liberty chapter</b></span>. These are primarily concentrated in Florida, North Carolina, and Pennsylvania, but are spread out all across the map." },
	  { value: [
		"These maps don’t perfectly overlap: only <span style='background-color: #EFFCFA; padding: 4px 4px; border-radius: 5px;'><b>127 counties have both</b></span> a Moms for Liberty chapter and a book ban incident.",
		"This is because the group isn’t solely drawn to red counties, where they have a better chance at advancing politically conservative policies. In fact, much of their campaign focuses on <span style='background-color: #EFFCFA; padding: 4px 4px; border-radius: 5px;'><b>“flipping” school boards</b></span> by appealing to those who feel <a href=https://www.momsforliberty.org/chapters/''>alone and unheard in their concerns</a>” in <a href='https://www.brookings.edu/articles/moms-for-liberty-where-are-they-and-are-they-winning/'>blue and purple</a> counties, where opposition is likely to be greater." 
		]},
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
			{#if Array.isArray(text.value)}
			  <div class="step">
				{#each text.value as subText}
				  <div class="step-inner">
					<p>{@html subText}</p>
				  </div>
				{/each}
			  </div>
			{:else}
			  <div class="step">
				<div class="step-inner">
				  <p>{@html text.value}</p>
				</div>
			  </div>
			{/if}
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
		z-index: 0;
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
		max-width: 40rem;
		margin: 0 auto;
		position: relative;
		display: flex;
		align-items: center; 
		justify-content: center; 
		flex-direction: column;
		gap: 1rem;
	}
	.step-inner {
		padding: 1rem;
		background-color: #FFFFFF;
		border: 1px solid black;
		box-shadow: 4px 6px 6px #00000046; 
		z-index: 1000;
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
			max-width: 30rem;
		}
		.step-inner {
			font-size: 12px; /* Set font size to 12px for smaller screens */
		}
	}


</style>
