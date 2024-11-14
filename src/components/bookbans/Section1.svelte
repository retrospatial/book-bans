<script>
	import Title from "$components/bookbans/Title.svelte";
	import IntroScrolly from "$components/bookbans/IntroScrolly.svelte";
</script>

<div id="section1">
	<Title />

	<p class="copy">
		This past July, the Donnelly Public Library in Idaho was forced to do the unthinkable: ban minors from entering without an accompanying guardian or written parental consent, effectively turning adults-only. This drastic measure came in response to a new state law requiring libraries to sequester all books deemed inappropriate for minors within 60 days of receiving a complaint—an impossible task given the library's limited space. 
	</p>

	<p class="copy">
		A month later, all public schools in Utah were ordered to remove 13 books from their library shelves under a state law requiring the blanket removal of any books containing “pornographic or indecent” material. The no-read list includes titles such as Forever by Judy Blume, Milk and Honey by Rupi Kaur, and A Court of Thorns and Roses by Sarah J. Maas. 
	</p>

	<p class="copy">
		And in September, the Charlotte-Mecklenburg school district in North Carolina barred educators from planning programming around Banned Books Week, a literacy campaign run annually by the American Library Association since 1982, before reversing the decision after much backlash. 
	</p>

	<p class="copy">
		That’s just this past summer. According to literacy advocacy group PEN America, which tracks and records book bans across the nation, efforts to remove literature from schools and libraries have taken a severe turn in recent years, coming to a head with over 10,000 reported bans during the 2023-2024 school year, a sharp increase from 3,362 reports in the previous year.
 	</p>
	
	<div class="scrolly">
		<IntroScrolly />
	</div>
</div>

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

	@media (max-width: 800px) { 
        #section1 {
			padding: 0 2rem;
		}
    }


</style>
