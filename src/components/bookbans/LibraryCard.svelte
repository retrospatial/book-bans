<script>
  import ChartDetails from "$components/bookbans/ChartDetails.svelte";
  import LibraryCard from "$svg/librarycard.html?raw";
</script>

<!-- <img src="/assets/svgs/librarycard.svg" class="image" alt="Library Card" /> -->
<section class="image">
  {@html LibraryCard.replaceAll("figma2html-box", "figma2html-box-card")}
</section>
<ChartDetails source="Source: PEN America, Facebook" />


<style>
  .image {
    display: block;
    margin: 0 auto 4rem auto !important;
  }

</style>
