<script>
	import { getContext } from "svelte";
	import Scrolly from "$components/helpers/Scrolly.svelte";
	import Books from "$components/bookbans/Books.svelte";

	const copy = [
		{ value: "More than 4,000 unique books were restricted or removed from school libraries this past school year.<br><br>The majority of them were authored by women—like <span style='background-color: #D3F3EE; padding: 4px 4px; border-radius: 5px;'><b>The Handmaid’s Tale</b></span> by Margaret Atwood, which has been repeatedly challenged for decades due to its depiction of ‘inappropriate’ themes, such as sex, profanity, and violence." },
		{ value: "More recently, the center of the political storm has shifted to target books that discuss race, gender, sex, diversity, and LGBTQ+ issues.<br><br>According to the American Library Association, Maia Kobabe’s graphic memoir <span style='background-color: #f3d3ee; padding: 4px 4px; border-radius: 5px;'><b>Gender Queer</b></span> was the most challenged book in the United States for three consecutive years from 2021 to 2023." },
		{ value: "Sure, many of these books can be found on the internet, easily accessible for today’s internet-savvy generation."},
		{ value: "But banning them from schools signals a dangerous opposition to letting kids and teens explore different worldviews in this increasingly polarized nation. More crucially, it limits them from accessing resources that may be critical for their own self-discovery." },
		{ value: "Recognize any of these books?" },
	]; 

	let scrollIndex;
	let steps = [0, 1, 2, 3, 4];
</script>

<section id="scrolly">
	<div class="sticky">
		<Books scrollIndex={scrollIndex} />
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
		z-index: 1000;
	}
	.sticky {
		position: sticky;
		top: 0;
		transition: all 1s;
		height: auto;
		max-width: 70rem;
		width: 100%;
		margin: 0 auto;  
		z-index: 1;
		overflow-x: hidden;
		pointer-events: none;
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.spacer {
		height: 75vh;
	}
	.step {
		height: 100vh;
		text-align: center;
		z-index: 1000;
		max-width: 30rem;
		margin: 0 auto;
		pointer-events: none;
		position: relative;
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
		font-weight: normal !important;
		padding: 0.25rem;
	}

	@media (max-width: 800px) { 
        
    }
	
</style>