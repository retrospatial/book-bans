<!-- 
npm run build
git add .
git commit -m "clean"
git push origin main

vercel --prod
 -->

<script>
	import Title from "$components/bookbans/Title.svelte";
	import UniqueTitles from "$components/bookbans/UniqueTitles.svelte";
	import M4LGroups from "$components/bookbans/M4LGroups.svelte";
	import TimeDifferences from "$components/bookbans/TimeDifferences.svelte";
	import IntroScrolly from "$components/bookbans/IntroScrolly.svelte";
	import M4LMap from "$components/bookbans/M4LMap.svelte";
	import BookBanMap from "$components/bookbans/BookBanMap.svelte";
	import Maps from "$components/bookbans/Maps.svelte";
	import MapsScrolly from "$components/bookbans/MapsScrolly.svelte";
	import RevenueGraphic from "$components/bookbans/RevenueGraphic.svelte";
	import LibraryCard from "$components/bookbans/LibraryCard.svelte";
	import AboutData from "$components/bookbans/AboutData.svelte";
</script>

<div id="page">
	
	<p class="copy">
		PEN America <a href="https://pen.org/report/beyond-the-shelves/">defines a book ban</a> as “any action taken against a book based on its content” that leads to a previously accessible book being restricted or removed either temporarily or permanently. According to the American Library Association, a challenge is an attempt to remove a book whereas a ban is the actual act of removal.
	</p>
	
	<p class="copy">
		Book bans aren’t new. Removing books from public circulation has long been used as a tool to suppress free speech and restrict access to ideas deemed dissenting, inappropriate, or dangerous. These conditions have been applied, often arbitrarily, to any book from <i>The Diary of a Young Girl</i> to <i>Harry Potter</i>.
	</p>

	<p class="copy">
		But the recent surge in bans across the United States <i>is</i> new. Against the backdrop of the early 2020s—marked by deep cultural divisions over issues like the COVID-19 pandemic, racial justice, abortion access, transgender rights, climate policy, and contentious elections—the rate of book bans reached unprecedented levels. Stories written by or about LGBTQ+ and people of color were particularly targeted, and the numbers since then have only increased.
	</p>

	<UniqueTitles />

	<h2 class="section-header">Who is driving these book bans?</h2>

	<p class="copy">
		Much of these bans have been attributed to individuals or committees linked to ‘parental rights’ groups. On paper, the parental rights movement is described as a push to broaden a parent’s right to determine what their child is being taught at school. In reality, the term has been invoked to restrict educators from teaching about race, gender, and sexuality in classrooms. It shares a name with Florida’s Parental Rights in Education Act (colloquially known as the ‘Don’t Say Gay’ law), which restricts education on sexual orientation and gender identity to what the state considers to be “age-appropriate.” 
	</p>

	<p class="copy">
		Book bans in particular have emerged as a key tactic to control educational content in schools. They’ve also become the basis of many conservative platforms, including Moms for Liberty. Formed in January 2021 to oppose Covid-19 masking and vaccine mandates, the group has since pivoted to target national education policies. 
	</p>
	
	<p class="copy">
		In just three years, Moms for Liberty has expanded from Florida to 48 states and increased its revenue sixfold—from $370,000 in 2021 to over $2 million in 2022. This growth has been backed by institutions like the Heritage Foundation, a conservative think tank that published the controversial Project 2025 plan, and the George Jenkins Foundation, whose president <a href="https://www.forbes.com/sites/tylerroush/2022/12/22/publix-heiress-julie-fancelli-offered-3-million-to-fund-jan-6-rally-house-documents-show/?sh=510e424852bd">bankrolled the January 6 rally</a> at the Capitol. 
	</p>

	<p class="copy">
		Last year, the group hosted prominent Republican figures such as Donald Trump, Ron DeSantis, Nikki Haley, and Vivek Ramaswamy as speakers at its National Summit, citing the “woke ideology” in public education as a <a href="https://www.edweek.org/policy-politics/moms-for-libertys-national-summit-5-takeaways-for-educators/2023/06">central battle</a> for the party. 
	</p>

	<p class="copy">
		Moms for Liberty’s star reputation among Republicans has also propelled its members to a seat at the <a href="https://apnews.com/article/moms-for-liberty-trump-2024-election-harris-7c252c611b5bc73c333a24392b979372">advisory board</a> of Project 2025 and has enabled the group to allocate <a href="https://apnews.com/article/moms-for-liberty-election-2024-battleground-states-ba85cdfe315df5adf75304c433b2581e">$3 million</a> for electoral advertising in key presidential swing states in the 2024 election. 
	</p>

	<p class="copy">
		It’s not alone. Across the three largest parental rights groups in the United States—Moms for Liberty, No Left Turn in Education, and Parents Defending Education—we found that their collective revenue nearly doubled after just a year of operation, increasing from $4 million in 2021 to $6.9 million in 2022. 
	</p>

	<RevenueGraphic />

	<p class="copy">
		Where is this money going? Much of it is funding lawsuits against school districts with progressive policies. Cases include one in <a href="https://www.wbur.org/news/2022/02/08/wellesley-parents-defending-education-lawsuit-settlement-boston">Massachusetts</a> over the creation of student affinity groups and another in <a href="https://www.axios.com/2022/08/08/iowa-school-transgender-rights-parents">Iowa</a> challenging policies that allowed students to use their preferred names and pronouns.
	</p>

	<p class="copy">
		For Moms for Liberty, whose modus operandi revolves around influencing school board elections and <a href="https://www.the74million.org/article/moms-for-liberty-has-lost-ground-at-the-polls-but-it-still-wields-influence/">mobilizing voters</a> for Republican candidates, these funds have been instrumental in gaining political influence. This money has enabled the group to advance its agenda at local levels and align with key conservative power brokers. 
	</p>

	<h2 class="section-header">How Moms for Liberty is gaining ground</h2>

	<p class="copy">
		To assess Moms for Liberty’s presence across the country, we compiled a list of local chapters from its national <a href="https://www.facebook.com/Moms4Liberty/groups">Facebook</a> group and compared it with data from PEN America’s <a href="https://pen.org/book-bans/pen-america-index-of-school-book-bans-2023-2024/">Index of School Book Bans</a> from 2021 to 2024.  
	</p>

	<p class="copy">
		<b>Here’s what that data looks like geographically.</b>
	</p>

</div>

<div id="maps">
	<MapsScrolly />
</div>

<div id="page">
	<p class="copy">
		Even so, eight of the ten counties with the most book bans have an associated Moms for Liberty group. The two that don’t still have ties to the organization. Iowa’s Johnson County hosted Moms for Liberty speakers from the neighboring Linn County chapter at their <a href='https://www.instagram.com/moms4libertylinn/p/Cux5hjcNKle/'>Freedom Rally</a> last year. And a teacher from Escambia was accused of <a href='https://www.advocate.com/news/teacher-moms-for-liberty-scheme'>scheming with the group</a> to trick a student into checking out an ‘inappropriate’ book, which Moms for Liberty then used as grounds to accuse public school librarians of distributing pornography to students. 
	</p>

	<LibraryCard />

	<p class="copy">
		All four states on this list have enacted versions of Florida’s ‘Don’t Say Gay’ law, which Moms for Liberty has <a href='https://www.pbs.org/newshour/politics/moms-for-liberty-rises-as-power-player-in-gop-politics-after-attacking-schools-over-gender-race'>publicly endorsed</a>. As a result of this legislation, thousands of books depicting sexual topics, LGBTQ+ characters, and people of color have been removed from school and library shelves at an unprecedented rate. 
	</p>

	<p class="copy">
		Timing is another important factor. For counties with both a Moms for Liberty chapter and a book ban, our analysis finds that the first book ban typically occurred shortly after a chapter was established in that county. This indicates that the group’s presence may play a crucial role in mobilizing local efforts to challenge and remove books from schools. The graph below shows that the highest rate of first-time book bans tends to occur within a year of a chapter's creation in the same county. 
	</p>

	<TimeDifferences />

	<p class="copy">
		While the chaotic and fragmented nature of state-based education policies makes it difficult to establish a direct link of causation between Moms for Liberty and each book ban, the data suggests that in areas where it’s active, the group has contributed to the frequency and scope of book bans. This is particularly true in regions vulnerable to policies that allow book banning. 
	</p>

	<h2 class="section-header">What’s next for book bans?</h2>

	<p class="copy">
		Some experts believe that the influence of parental rights groups like Moms for Liberty has <a href='https://www.axios.com/local/miami/2024/03/13/dont-say-gay-parental-rights-florida-moms-for-liberty'>finally hit its peak</a> after three years of unchecked growth. But recent legislative changes in states like Utah and <a href='https://www.iowapublicradio.org/education/2024-08-09/federal-appeals-court-rules-iowas-book-ban-law-can-take-effect'>Iowa</a> continue to pressure schools, libraries, and educators to conform to increasingly restrictive content guidelines, further threatening intellectual freedom and access to diverse educational materials.  
	</p>

	<p class="copy">
		Readers, however, are fighting back. Little Free Library stewards are <a href='https://www.tennessean.com/story/news/2024/09/25/little-free-libraries-works-banned-books-week-interactive-map/75297244007/'>stocking their bookcases</a> with banned books to promote reading in their neighborhoods. York County, PA, which ranked first for book bans between the 2021 and 2022 school years, has seen no new bans since, thanks to advocacy work done by <a href='https://www.facebook.com/CitizensForCYSD/posts/panther-proud-central-york-is-the-first-school-district-in-york-county-to-prohib/869040768657125/'>school board members</a> in the Central York School District. 
	</p>

	<p class="copy">
		Across the nation, students are <a href='https://wach.com/news/local/kids-march-at-south-carolina-state-to-protest-book-bans-and-honor-history-book-bans-banned-children-reading-history-orange-burg-massacre-scsu-claflin-university-peaceful-protest-protesting'>marching</a> to defend their right to read. They’re coordinating <a href='https://19thnews.org/2024/07/book-bans-students-parents-advocates/'>grassroots</a> efforts to combat these bans. And community members of all ages have their backs.
	</p>

	<p class="copy">
		“Banning books and burning books are the same. Both are done for the same reason: fear of knowledge,” said 101-year-old Florida resident <a href='https://pen.org/grace-linn-book-ban-martin-county/'>Grace Linn</a>, whose activism inspired the documentary The ABCs of Book Banning, which won a nomination for this year’s Oscars. “Fear is not freedom. Fear is not liberty. Fear is control.”
	</p>

	<p class="copy">
		Still, when it comes to book banning, other forces beyond Moms for Liberty are at play. Trump’s new presidency may spell even greater trouble for public education, as he has pledged to <a href='https://www.cnn.com/2024/09/20/politics/department-of-education-shut-down-trump/index.html'>dismantle</a> the U.S. Department of Education This would potentially drain even more resources from the system and further narrow the boundaries of what is considered appropriate education.  
	</p>

	<p class="copy">
		More than ever, books are getting caught in the political crossfire sweeping this country. You can <a href='https://bookriot.com/how-to-fight-book-bans-and-challenges/'>get involved</a> in the fight by organizing reading programs, voting in local elections, or simply checking out a book at your public library. 
	</p>

	<AboutData />
</div>

	


<style>
	#page {
		max-width: 45rem;   
		padding: 0;      
		margin: 0 auto;    
	}

	#maps {
		max-width: 80rem;   
		margin: 0 auto; 
		   
	}

	:global(#page section) {
		margin: 32px auto;  
		padding-top: 32px;  
	}

	:global(#page section > section) {
		margin: 0 auto;      
		padding-top: 0;     
	}

	:global(#page h2 span) {
		background: var(--color-mark); 
		padding: 0 8px;             
	}

	.copy {
		max-width: 45rem;  
		margin: 32px auto;    
		text-align: left;   
	}

	.section-header{
		max-width: 45rem; 
		margin: 64px auto;      
		text-align: left;
	}

	@media (max-width: 800px) { 
        #page {
			padding: 0 2rem;
		}
    }
</style>

