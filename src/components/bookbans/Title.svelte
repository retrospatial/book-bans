<script>
	import Intro from "$svg/intro.html?raw";
</script>

<section id="intro">
	<div class="intro-row"> 
		<section class="title">
			{@html Intro.replaceAll("figma2html-box", "figma2html-box-intro")}
		</section>

		<div id="subtitle">
			<p class="subtitle-text">Book bans are a national issue. See what’s happening in your county.</p>

			<div id="byline">
				<p class="byline-text">By Florina Sutanto</p>
				<p class="byline-date">November 2024</p>
			</div>
		</div>
	</div>
</section>


<style>
	#intro {
		display: table;
		justify-content: center;     
		align-items: center;         
		min-height: 100vh;           
		text-align: center;          
		margin: 0;  
		width: 100%;
	}

	.intro-row{
		display: table-cell;
		vertical-align: middle;
	}

	#subtitle {
		margin: 4rem auto;
	}

	.subtitle-text
	{
		font-size: 18px;
		padding: 0 12px;
		margin-bottom: 50px;
	}

    #byline {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        max-width: 40rem;
        margin-top: 16px;
        border-top: 1px dashed #000;
        border-bottom: 1px dashed #000;
        padding: 18px 0;
		margin-left: auto;
    	margin-right: auto;
    }

    .byline-text,
    .byline-date {
		font-size: 14px;
		font-weight: 500;
        margin: 0;
        text-transform: uppercase;
		font-family: 'Roboto Mono', monospace;
    }
</style>
