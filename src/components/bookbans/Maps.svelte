<script>
	// https://github.com/topojson/us-atlas
	// https://github.com/d3/d3-geo
	// https://observablehq.com/@mbostock/u-s-state-map
	// TODO: https://observablehq.com/@d3/u-s-map
	// TODO: https://observablehq.com/@jeantimex/us-state-county-map
	
	import { onMount } from 'svelte';
	import * as topojson from 'topojson-client';
	import { geoPath, geoAlbersUsa } from 'd3-geo';
	import { draw } from 'svelte/transition';
	import { csv } from 'd3-fetch';
	import { scaleSequential } from 'd3-scale';
	import { interpolateReds } from 'd3-scale-chromatic';
	
	// https://github.com/topojson/us-atlas#us-atlas-topojson
	const projection = geoAlbersUsa().scale(1300).translate([487.5, 305])
	
	const path = geoPath().projection(null);
	
	let states = [];
	let counties = [];
	let selected;
	let data = [];

	export let scrollIndex = 0;  
	
	// Color scale only for ban_count
	const colorScale = scaleSequential(interpolateReds).domain([0, 50]);
	
	onMount(async () => {
	  const us = await fetch('https://cdn.jsdelivr.net/npm/us-atlas@3/counties-albers-10m.json')
		.then(d => d.json());
	
	  data = await csv("/assets/data/map_dataset.csv", d => {
		return {
		  ...d,
		  county_fips: d.county_fips,
		  ban_count: d.ban_count === 'NA' ? null : +d.ban_count,  // Handle NA as null
		  facebook_yes: d.facebook === 'yes' ? 1 : 0,  // "yes" becomes 1, others become 0
		  overlap_yes: d.overlap === 'yes' ? 1 : 0  // "yes" becomes 1, others become 0
		};
	  });
	
	  states = topojson.feature(us, us.objects.states).features;
	  counties = topojson.feature(us, us.objects.counties).features;
	});

	// Reactive color array for counties based on selected scrollIndex
	$: countyColors = counties.map(feature => {
	  let entry;
	  if (scrollIndex === 0) {
		entry = data.find(d => d.county_fips === feature.id.toString());
		if (entry && entry.ban_count !== null) {  // Only color if ban_count is not null
		  return { id: feature.id, color: colorScale(entry.ban_count) }; 
		}
	  } else if (scrollIndex === 1) {
		entry = data.find(d => d.county_fips === feature.id.toString());
		if (entry) {
		  return { id: feature.id, color: entry.facebook_yes === 1 ? '#5a74b8' : '#fff' };  // Color for facebook "yes"
		}
	  } else if (scrollIndex === 2) {
		entry = data.find(d => d.county_fips === feature.id.toString());
		if (entry) {
		  return { id: feature.id, color: entry.overlap_yes === 1 ? '#346E75' : '#fff' };  // Color for overlap "yes"
		}
	  }
	  return { id: feature.id, color: '#fff' };  // Default to white for counties without data
	});
</script>

<figure class="folded">
	<!-- SVG Map -->
	<svg viewBox="0 0 975 610" class="fold-me-please">
		<!-- Counties -->
		{#each counties as feature}
			<path 
				d={path(feature)} 
				on:click={() => selected = feature} 
				on:keydown={(e) => (e.key === 'Enter' || e.key === ' ') && (selected = feature)}
				tabindex="0"
				role="button"
				aria-label="Select county"
				class="county"  
				stroke="rgb(0 0 0 / 10%)" 
				fill={countyColors.find(c => c.id === feature.id)?.color} />
		{/each}
  
		<!-- State borders -->
		<g fill="none" stroke="black">
			{#each states as feature, i}
				<path 
					d={path(feature)} 
					on:click={() => selected = feature} 
					on:keydown={(e) => (e.key === 'Enter' || e.key === ' ') && (selected = feature)}
					tabindex="0"
					role="button"
					aria-label="Select state"
					class="state" 
					in:draw={{ delay: i * 50, duration: 1000 }} 
				/>
			{/each}
		</g>
  
		<!-- Highlight selected county -->
		{#if selected}
			<path d={path(selected)} fill="hsl(0 0% 50% / 20%)" stroke="black" stroke-width={2} />
		{/if}
	</svg>
  
	<!-- Fold overlay elements -->
	<span class="folds main">
		<span class="cell main-1"></span>
		<span class="cell main-2"></span>
		<span class="cell main-1"></span>
		<span class="cell main-2"></span>
		<span class="cell main-1"></span>
	</span>
	<span class="folds vertical">
		<span class="cell vertical-1"></span>
		<span class="cell vertical-2"></span>
		<span class="cell vertical-3"></span>
		<span class="cell vertical-4"></span>
		<span class="cell vertical-5"></span>
	</span> 
	<span class="folds horizontal">
		<span class="cell horizontal-1"></span>
		<span class="cell horizontal-2"></span>
		<span class="cell horizontal-1"></span>
		<span class="cell horizontal-2"></span>
		<span class="cell horizontal-1"></span>
		<span class="cell horizontal-3"></span>
		<span class="cell horizontal-4"></span>
		<span class="cell horizontal-3"></span>
		<span class="cell horizontal-4"></span>
		<span class="cell horizontal-3"></span>
	</span>
</figure>

<!-- <div class="selectedName">
	{#if selected}
		{getCountyName(selected)}
	{/if}
</div> -->

<style>
	/* Original styles for county and selectedName */
	.county {
		transition: fill 0.5s ease; 
	}
  
	.county:hover {
		stroke: black;
		stroke-width: 2;
	}
  
	.selectedName {
		text-align: center;
		margin-top: 8px;
		font-size: 1.5rem;
	}
	
	/* Additional styles for fold effect */
body {
  padding: 2em;
  background-color: #dadada;
  background-color: #333;
  font-family: sans-serif;
  margin: 0;
  height: 100vh;
}

figure.folded {
  margin-inline: auto;
  width: min(100%, 60em);
  height: 80vh;
  position:relative;
  display:flex;
  justify-content:center;
  align-items:center;
  overflow:hidden;
  background:#F5F5F4;
  box-shadow:
    0.2em 0.2em 0.8em 0.2em
    rgba(76, 53, 73, 0.4);
	position: relative;
}

svg.fold-me-please {
  width:100%;
  height:100%;
  object-fit:cover;
  filter:
    hue-rotate(0deg)
    saturate(1)
    brightness(1)
    contrast(1)
    opacity(1);
  mix-blend-mode:normal;
  image-rendering:high-quality;
  transform:scale(1);
  visibility:visible;
}

/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */
/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */

span.folds {
  position:absolute;
  top:0;
  right:0;
  bottom:0;
  left:0;
  display:grid;
  grid-template-columns:auto auto auto auto auto;
}

span.cell {
  border:0px solid rgba(30, 10, 60, 0.4);
  font-size:1em;
  display:flex;
  flex-direction:row;
  justify-content:center;
  align-items:center;
}

/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */
/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */

/* MAIN */
span.main {
  visibility:visible;
  filter:opacity(0.2);
}

span.main-1 {
  background-image: 
    linear-gradient(
      to right,
      rgba(76, 53, 73, 0.20) 0%,
      rgba(76, 53, 73, 0.10) 20%
    );
}

span.main-2 {
  background-image: 
    linear-gradient(
      to right,
      rgba(76, 53, 73, 0.04) 0%,
      rgba(76, 53, 73, 0.00) 20%
    );
}

/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */
/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */

/* VERTICAL */
span.vertical {
  visibility:visible;
  filter:opacity(0.1);
}

span.vertical-1 {
  background-image: 
    linear-gradient(
      to right,
      rgba(76, 53, 73, 0.08) 0%,
      rgba(76, 53, 73, 0.02) 20%,
      rgba(76, 53, 73, 0.00) 60%,
      rgba(76, 53, 73, 0.16) 94%,
      rgba(76, 53, 73, 0.10) 98%,
      rgba(76, 53, 73, 0.06) 100%
    );
}

span.vertical-2 {
  background-image: 
    linear-gradient(
      to right,
      rgba(76, 53, 73, 0.06) 0%,
      rgba(76, 53, 73, 0.10) 2%,
      rgba(76, 53, 73, 0.16) 6%,
      rgba(76, 53, 73, 0.00) 40%,
      rgba(76, 53, 73, 0.02) 100%
    );
}

span.vertical-3 {
  background-image: 
    linear-gradient(
      to right,
      rgba(76, 53, 73, 0.15) 0%,
      rgba(76, 53, 73, 0.12) 2%,
      rgba(76, 53, 73, 0.07) 5%,
      rgba(76, 53, 73, 0.00) 28%,
      rgba(76, 53, 73, 0.00) 60%,
      rgba(76, 53, 73, 0.08) 94%,
      rgba(76, 53, 73, 0.05) 98%,
      rgba(76, 53, 73, 0.03) 100%
    );
}

span.vertical-4 {
  background-image: 
    linear-gradient(
      to right,
      rgba(76, 53, 73, 0.06) 0%,
      rgba(76, 53, 73, 0.10) 2%,
      rgba(76, 53, 73, 0.16) 6%,
      rgba(76, 53, 73, 0.00) 40%,
      rgba(76, 53, 73, 0.02) 100%
    );
}

span.vertical-5 {
  background-image: 
    linear-gradient(
      to right,    
      rgba(76, 53, 73, 0.15) 0%,
      rgba(76, 53, 73, 0.12) 2%,
      rgba(76, 53, 73, 0.07) 5%,
      rgba(76, 53, 73, 0.00) 28%,
      rgba(76, 53, 73, 0.01) 100%      
    );
}

/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */
/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */

/* HORIZONTAL */
span.horizontal {
  visibility:visible;
  filter:opacity(0.3);
}

span.horizontal-1 {
  background-image: 
    linear-gradient(
      to bottom,
      rgba(76, 53, 73, 0.02) 0%,
      rgba(76, 53, 73, 0.00) 7%,
      rgba(76, 53, 73, 0.15) 95%,
      rgba(76, 53, 73, 0.24) 100%
    );
}

span.horizontal-2 {
  background-image: 
    linear-gradient(
      to bottom,
      rgba(76, 53, 73, 0.02) 0%,
      rgba(76, 53, 73, 0.00) 60%,
      rgba(76, 53, 73, 0.22) 96%,
      rgba(76, 53, 73, 0.08) 100%
    );
}

span.horizontal-3 {
  background-image: 
    linear-gradient(
      to top,
      rgba(76, 53, 73, 0.08) 0%,
      rgba(76, 53, 73, 0.00) 40%,
      rgba(76, 53, 73, 0.14) 100%
    );
}

span.horizontal-4 {
  background-image: 
    linear-gradient(
      to top,
      rgba(76, 53, 73, 0.02) 0%,
      rgba(76, 53, 73, 0.00) 60%,
      rgba(76, 53, 73, 0.18) 94%,
      rgba(76, 53, 73, 0.02) 100%
    );
}

/* ---------------------------------------------------
Written by STARIDAS GEOGRAPHY Making Maps Pretty 
info@staridasgeography.gr | www.staridasgeography.gr
Copyright 2021 | All Rights Reserved | CC BY-NC-SA 4.0
---------------------------------------------------- */
</style>