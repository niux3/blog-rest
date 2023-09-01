<script>
    export let url
    export let title


    let posts = (async ()=>{
        let resp = await fetch(url)
        return await resp.json()
    })()
</script>

{#if title !== undefined}
    <h1>{title}</h1>
{/if}
{#await posts}
    <p>chargement...</p>
{:then data}
    {#each data['posts'] as row}
        <article data-id="{row.id}">
            <a href="/#/article/{row.id}-{row.slug}">
                <h2>{row.title}&nbsp;<small>{row.created}</small></h2>
                <img src={row.illustration} alt="" class="thumbnail">
                <p>{row.content.substr(0, 200)}...</p>
            </a>
            <div class="callout">
                <ul class="menu simple">
                    <li><a href="/">Auteur: {row.author}</a></li>
                    <li><a href="/">Commentaire{row.comments.length > 1? 's' : ''}: {row.comments.length}</a></li>
                </ul>
            </div>
        </article>
    {/each}
{/await}

<style>
    article > a p{
        color: #333;
    }
</style>


