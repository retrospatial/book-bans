<script>
    import ChartDetails from "$components/bookbans/ChartDetails.svelte";
    import TimeDiff from "$svg/timediff.html?raw";
  </script>
  
  <!-- <img src="/assets/svgs/librarycard.svg" class="image" alt="Library Card" /> -->
  <div class="image">
    {@html TimeDiff.replaceAll("figma2html-box", "figma2html-box-time")}
  </div>
  <ChartDetails source="Source: PEN America, Facebook" />
  
  
  <style>
    .image {
        display: block;
        margin: 2rem auto !important;
    }

    @media (max-width: 800px) { 
        .image {
			margin: 4rem auto 2rem auto !important;
		}
    }
  </style>
  
  
<!-- <script>
    import { onMount } from "svelte";
    import * as d3 from "d3";
    import { LayerCake, Svg } from 'layercake';
    import Column from "$components/layercake/Column.svelte"; 
    import AxisX from "$components/layercake/AxisX.svg.svelte";
    import AxisY from "$components/layercake/AxisY.svg.svelte";
    import ChartDetails from "$components/bookbans/ChartDetails.svelte";
    import inView from "$actions/inView.js";

    // Defaults
    let data = [];
    const xKey = "time_diff"; 
    const yKey = "count";  
    let inViewTrigger = false;
    let innerWidth = 0;
    let innerHeight = 0;

    // Load the data when the component is mounted
    onMount(async () => {
        try {
            const dataPath = "/assets/data/3_timedifferences.csv"; 
            data = await d3.csv(dataPath);

            // Ensure the values are numbers
            data.forEach(d => {
                d[xKey] = +d[xKey];
                d[yKey] = +d[yKey];
            });

            // Create histogram bins
            const histogram = d3.histogram()
                .value(d => d[xKey])
                .domain(d3.extent(data, d => d[xKey]))
                .thresholds(25);

            // Group data into bins
            const bins = histogram(data);

            // Prepare data for LayerCake
            data = bins.map(b => ({
                x0: b.x0,
                x1: b.x1,
                count: b.length,
                color: b.x0 < 0 ? "#ccc": "steelblue"
            }));

            // Log prepared data for debugging
            console.log("Data:", data);
            
        } catch (error) {
            console.error("Error loading data:", error);
        }
    });

    // Function to trigger drawing when in view
    function inViewDraw() { inViewTrigger = true; }
    function exitViewDraw() { inViewTrigger = false; }
</script>

<svelte:window bind:innerWidth bind:innerHeight />

<!-- Chart Title 
<ChartDetails title="Days Between M4L Chapter Creation and First Book Ban" />

<div class="chart-container"
    use:inView
    on:enter={inViewDraw}
    on:exit={exitViewDraw}
>
    {#if data.length > 0}  
        <LayerCake
            padding={{ top: 16, right: 16, bottom: 32, left: 16 }}
            x={d => [d.x0, d.x1]} 
            y={d => d.count} 
            xDomain={d3.extent(data, d => d.x0)}
            yDomain={[0, d3.max(data, d => d.count)]}
            data={data}
        >
            <Svg>
                <AxisX gridlines={false} />
                <AxisY snapBaselineLabel gridlines={true} />
                <Column 
                    inViewTrigger={inViewTrigger} 
                    stroke="black"
                    strokeWidth="1"
                    fill={d => d.color}
                />

                <div class="annotation" style="left: 0; top: 0;">
                    <p>Book bans increased</p>
                    <p>the change</p>
                </div>
                
            </Svg>
        </LayerCake>
    {/if}
</div>

<!-- Charop Source 
<ChartDetails source="Source: Facebook, PEN America" />

<style>
    .chart-container {
        width: calc(100% - 2rem);
        height: 400px;
        margin: 1rem auto;
        background: #f2f2f2;
        padding: 1rem;
        border: 2px solid;
        border-color: var(--window-inset-stroke);
    }

    @media (max-width: 600px) { 
        .chart-container {
            padding: 1rem;
            height: 300px;
        }
    }

    .annotation {
        position: absolute;
        color: black;
        font-size: 1em;
    }

    .annotation p {
        margin: 0;
        line-height: 1.2;
    }
</style> -->
