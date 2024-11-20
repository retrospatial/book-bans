<script>
	import Title from "$components/bookbans/Title.svelte";
	import IntroScrolly from "$components/bookbans/IntroScrolly.svelte";
	import sticker from "$svg/cclogo_black.svg";
</script>


<section id="section1">

	<header>
		<div class="sticker">
			<a href="https://citizencodex.com" target="_self">
				{@html sticker}
			</a>	
		</div>
	</header>

	<div class="title">
		<Title /> 
	</div>

	<p class="copy">
		This past July, the Donnelly Public Library in Idaho was forced to do the unthinkable: <a href="https://donnelly.lili.org/new-rules-at-the-library/">ban minors from entering</a> without an accompanying guardian or written parental consent. The library effectively turned adults-only. This drastic measure came in response to a new state law requiring libraries to sequester all books deemed inappropriate for minors within 60 days of receiving a complaint—an impossible task given the library's limited space. 
	</p>

	<p class="copy">
		A month later, all public schools in Utah were ordered to remove 13 books from their library shelves due to a state law requiring the blanket removal of any books containing “<a href="https://abcnews.go.com/US/utah-bans-13-books-public-schools-statewide-including/story?id=112680897">pornographic or indecent</a>” material. The no-read list includes titles such as <i>Forever</i> by Judy Blume, <i>Milk and Honey</i> by Rupi Kaur, and <i>A Court of Thorns and Roses</i> by Sarah J. Maas. 
	</p>

	<p class="copy">
		And in September, the Charlotte-Mecklenburg school district in North Carolina <a href="https://www.theguardian.com/us-news/2023/sep/30/north-carolina-bans-banned-books-week-but-retracts-after-media-backlash">barred educators</a> from planning programming around Banned Books Week, a literacy campaign run annually by the American Library Association since 1982. Only after a huge backlash did the district reverse its decision. 
	</p>

	<p class="copy">
		That’s just this past summer. According to literacy advocacy group PEN America, which tracks book bans across the nation, efforts to remove literature from schools and libraries have taken a severe turn in recent years. There were over 10,000 reported bans during the 2023-2024 school year, a sharp increase from 3,362 reports in the previous year.
 	</p>

	 <p class="copy">
		You may be asking yourself
 	</p>
	
	<div class="scrolly">
		<IntroScrolly />
	</div>
</section>

<style>
	#section1 {
		background-image: url('/assets/images/paper3.png');
		background-size: 100%; 
		background-repeat: repeat; 
		background-position: center; 
		padding: 0;      
		margin: 0 auto; 
	}

	.copy {
		max-width: 42rem;  
		margin: 32px auto;    
		text-align: left;   
	}

	header {
		display: flex;
		justify-content: center; 
		padding-top: 2rem;
	}

	.sticker {
		max-width: 16em;
	}

	@media (max-width: 800px) { 
        #section1 {
			padding: 0 1rem;
		}
    }


</style>
