<script>
    import ChartDetails from "$components/bookbans/ChartDetails.svelte";
</script>

<!-- Chart Title -->
<h2 class="chart-title">Across the three largest book-banning organizations, collective revenue nearly <span style="background-color: #FEC872">doubled</span> after just a year of operation.</h2>

<div id="stacks">
    <div class="stack-container">
        <p class="label">$4 million</p>
        <img id="stack1" src="assets/svgs/stack1.svg" alt="stack1" />
        <p class="year">2021</p>
    </div>
    <div class="stack-container">
        <p class="label">$6.8 million</p>
        <img id="stack2" src="assets/svgs/stack2.svg" alt="stack2" />
        <p class="year">2022</p>
    </div>
</div>

<!-- Chart Source -->
<ChartDetails source="Source: ProPublica Nonprofit Explorer" />

<style>
    #stacks {
        display: flex;
        justify-content: center;
        align-items: flex-end;
        gap: 20px; 
    }

    .stack-container {
        display: flex;
        flex-direction: column;
        align-items: center; 
    }

    #stacks img {
        width: 85%;
    }

    .chart-title {
        margin-top: 4rem;
        margin-bottom: 0.25rem;
        font-size: 24px;
        width: 30rem;
        margin: 0 auto;
        padding: 2rem 0;
        font-family: 'American Typewriter', serif;
    }

    .label {
        font-family: 'American Typewriter', serif;
        text-align: center; 
        margin-bottom: 1rem;
    }
    
    .year {
        text-align: center; 
        font-family: 'Roboto Mono', monospace;
        margin-top: 1rem;
    }

    @media (max-width: 800px) { 
        .chart-title {
            font-size: 18px;
            width: 20rem;
        }
    }
</style>
