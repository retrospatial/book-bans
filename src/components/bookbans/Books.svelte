<script>
    import { onMount } from 'svelte';

    export let scrollIndex;

    // Generate all 50 book images
    const bookImages = Array.from({ length: 50 }, (_, i) => `covers/book_${i + 1}.jpg`);

    // Group the images into rows of 10
    const bookRows = [];
    for (let i = 0; i < bookImages.length; i += 10) {
        bookRows.push(bookImages.slice(i, i + 10));
    }

    let imagesLoaded = false;

    // Function to preload images
    function preloadImages(imageArray) {
        return Promise.all(
            imageArray.map(image => {
                return new Promise((resolve) => {
                    const img = new Image();
                    img.src = `/assets/images/${image}`;
                    img.onload = () => resolve();
                    img.onerror = () => resolve(); // Resolve even on error to avoid blocking
                });
            })
        );
    }

    onMount(async () => {
        await preloadImages(bookImages);
        imagesLoaded = true;
    });
</script>

<section id="books-array" class:imagesLoaded={imagesLoaded}>
    {#each bookRows as row, rowIndex}
        <div
            class="row-container {scrollIndex >= rowIndex ? 'fade-in' : ''}"
        >
            {#each row as image, index}
                <div class="book-image-container">
                    <img 
                        src={`/assets/images/${image}`} 
                        alt={`Book ${rowIndex * 10 + index + 1}`} 
                        class="book-image"
                    />
                </div>
            {/each}
        </div>
    {/each}
</section>

<style>
    #books-array {
        display: flex;
        flex-direction: column;
        width: 100%;
        position: relative;
        align-items: center;
        max-height: 100vh;
        margin: 32px auto;
        padding-top: 32px;
    }

    .imagesLoaded #books-array {
        visibility: visible;
    }

    .row-container {
        display: grid;
        grid-template-columns: repeat(10, 1fr);
        gap: 1rem;
        width: 100%;
        padding-bottom: 1rem;
        justify-items: center;
        align-items: center;
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    }

    .fade-in {
        opacity: 1;
        transform: translateY(0);
    }

    .book-image-container {
        position: relative;
        width: auto;
        height: 15vh;
        overflow: hidden;
    }

    .book-image {
        width: 100%;
        height: 100%;
        object-fit: contain;
        filter: brightness(1); /* Mute colors and add grayscale */
    }

    /* Noise overlay */
    /* .book-image-container::after {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><rect width="100" height="100" fill="white" fill-opacity="0.2"/><rect width="100" height="100" fill="black" fill-opacity="0.1"/><rect width="100" height="100" fill="white" fill-opacity="0.2"/><rect width="100" height="100" fill="black" fill-opacity="0.1"/></svg>');
        opacity: 0.3;
        pointer-events: none;
    } */
</style>
