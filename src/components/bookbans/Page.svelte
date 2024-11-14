<!-- 
npm run build
git add .
git commit -m "can u not crash"
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
		PEN America defines a book ban as “any action taken against a book based on its content” that leads to a previously accessible book being restricted or removed, regardless of whether it is temporary or permanent. The American Library Association distinguishes a challenge, which signals an attempt at removing a book, from a ban, which is the act of removal. 
	</p>
	
	<p class="copy">
		Book bans aren’t new. The act of removing books from public circulation has long been used as a tool to suppress free speech and restrict access to ideas and information that have been determined by some party to be dissenting, inappropriate, or dangerous—conditions that have been applied, often arbitrarily, to any book from <i>The Diary of a Young Girl</i> to <i>Harry Potter</i>.
	</p>

	<p class="copy">
		But the recent surge in bans across the United States <i>is</i> new. Amidst the increasingly heightened cultural divide of the 2020s—marked by deep divisions over the Covid-19 pandemic, racial injustice, abortion access, transgender rights, climate policies, and charged elections—book bans have accelerated at an unprecedented rate since 2021, with a particular target on stories written by or about LGBTQ+ and people of color. And the numbers have only increased since then. 
	</p>

	<UniqueTitles />

	<h2 class="section-header">Who is driving these book bans?</h2>

	<p class="copy">
		Much of these bans have been attributed to individuals or committees linked to ‘parental rights’ groups. On paper, the parental rights movement is described as a push to broaden a parent’s right to determine what their child is being taught at school. In reality, the term has been invoked to restrict educators from teaching and discussing race, gender, and sexuality in classrooms, sharing a name with Florida’s Parental Rights in Education Act (colloquially known as Don’t Say Gay), which restricts education on sexual orientation and gender identity to what the state considers to be “age-appropriate”. 
	</p>

	<p class="copy">
		Much of these bans have been attributed to individuals or committees linked to ‘parental rights’ groups. On paper, the parental rights movement is described as a push to broaden a parent’s right to determine what their child is being taught at school. In reality, the term has been invoked to restrict educators from teaching and discussing race, gender, and sexuality in classrooms, sharing a name with Florida’s Parental Rights in Education Act (colloquially known as the ‘Don’t Say Gay’ law), which restricts education on sexual orientation and gender identity to what the state considers to be “age-appropriate”. 
	</p>

	<p class="copy">
		Book bans in particular have emerged as a key tactic in efforts to control educational content in schools and become the basis of many conservative platforms. One such group is Moms for Liberty, which formed in January 2021 to oppose Covid-19 masking and vaccine mandates and has since pivoted to target national education policies. 
	</p>
	
	<p class="copy">
		In just three years, the group has expanded from Florida to 48 states and increased their revenue sixfold—from $370,000 in 2021 to over $2 million in 2022. This growth has been backed by institutions like the Heritage Foundation, a conservative think tank that published the controversial Project 2025 plan, and the George Jenkins Foundation, whose president bankrolled the January 6 rally at the Capitol. 
	</p>

	<p class="copy">
		Moms for Liberty’s star reputation among Republicans has also propelled them to a seat at the advisory board of Project 2025 and enabled them to allocate $3 million for electoral advertising in key presidential swing states in the 2024 election. Last year, the group hosted prominent Republican figures such as Donald Trump, Ron DeSantis, Nikki Haley, and Vivek Ramaswamy as speakers at their National Summit, citing the “woke ideology” in public education as a central battle for the party. 
	</p>

	<p class="copy">
		They’re not alone. Across the three largest parental rights groups in the United States—Moms for Liberty, No Left Turn in Education, and Parents Defending Education, all of which were founded in 2020 or 2021—we found that their collective revenue nearly doubled after just a year of operation, increasing from $4 million in 2021 to $6.9 million in 2022. 
	</p>

	<RevenueGraphic />

	<p class="copy">
		Where is this money going? Much of it has been directed toward funding lawsuits against school districts with progressive policies, including a case in Massachusetts over the creation of student affinity groups and another in Iowa challenging policies that allowed students to use their preferred names and pronouns.
	</p>

	<p class="copy">
		For Moms for Liberty, whose modus operandi revolves around influencing school board elections and mobilizing voters for Republican candidates, these funds have been instrumental in gaining political influence, enabling them to advance their agenda at local levels and align with key conservative power brokers. 
	</p>

	<h2 class="section-header">How Moms for Liberty is gaining ground</h2>

	<p class="copy">
		To assess Moms for Liberty’s presence across the country, we compiled a list of local chapters from their national Facebook group and compared it with data from PEN America’s Index of School Book Bans from 2021 to 2024.  
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
		Even so, eight of the ten counties with the most book bans have an associated Moms for Liberty group. The two that don’t still have ties to the organization: Iowa’s Johnson County hosted Moms for Liberty speakers from the neighboring Linn County chapter at their Freedom Rally last year, and a teacher from Escambia was accused of scheming with the group to trick a student into checking out an ‘inappropriate’ book, which Moms for Liberty then used as grounds to accuse public school librarians of distributing pornography to students. 
	</p>

	<LibraryCard />

	<p class="copy">
		All four states on this list have enacted versions of Florida’s ‘Don’t Say Gay’ law, which Moms for Liberty has publicly endorsed. As a result of this legislation, thousands of books depicting sexual topics, LGBTQ+ characters, and people of color have been removed from school and library shelves at an unprecedented rate since 2021. 
	</p>

	<p class="copy">
		Timing is another important factor. For counties with both a Moms for Liberty chapter and a book ban, our analysis finds that the first book ban typically occurred shortly after a chapter was established in that county, indicating that the group’s presence may play a crucial role in mobilizing local efforts to challenge and remove books from schools. The graph below shows that the highest rate of first-time book bans tends to occur within a year of a chapter's creation in the same county. 
	</p>

	<TimeDifferences />

	<p class="copy">
		While the chaotic and fragmented nature of state-based education policies makes it difficult to establish a direct link of causation between Moms for Liberty and each book ban, the data suggests that the group’s presence and expansion has contributed to the frequency and scope of book bans in areas where they are active, particularly in regions vulnerable to policies that allow book banning. 
	</p>

	<h2 class="section-header">What’s next for book bans?</h2>

	<p class="copy">
		While some experts believe that the influence of parental rights groups like Moms for Liberty has finally hit its peak after three years of unchecked growth, recent changes to legislation in states like Utah and Iowa continue to pressure schools, libraries, and educators to conform to increasingly restrictive content guidelines, further threatening intellectual freedom and access to diverse educational materials.  
	</p>

	<p class="copy">
		Much of these bans have been attributed to individuals or committees linked to ‘parental rights’ groups. On paper, the parental rights movement is described as a push to broaden a parent’s right to determine what their child is being taught at school. In reality, the term has been invoked to restrict educators from teaching and discussing race, gender, and sexuality in classrooms, sharing a name with Florida’s Parental Rights in Education Act (colloquially known as Don’t Say Gay), which restricts education on sexual orientation and gender identity to what the state considers to be “age-appropriate”. 
	</p>

	<p class="copy">
		Across the nation, students are marching to defend their right to read and coordinating grassroots efforts to combat these bans. Community members of all ages have their backs.
	</p>

	<p class="copy">
		“Banning books and burning books are the same. Both are done for the same reason: fear of knowledge,” said 101-year-old Florida resident Grace Linn, whose activism inspired the documentary The ABCs of Book Banning, which won a nomination for this year’s Oscars. “Fear is not freedom. Fear is not liberty. Fear is control.”
	</p>

	<p class="copy">
		Still, when it comes to book banning, other forces beyond Moms for Liberty are at play. Trump's new presidency may spell even greater trouble for public education, as he has pledged to dismantle the U.S. Department of Education, potentially draining even more resources from the system and further narrowing the boundaries of what is considered appropriate education.  
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
</style>

