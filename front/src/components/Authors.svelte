<script>
    let authors = (async ()=>{
        let response = await fetch('//localhost:8000/users')
        return await response.json()
    })()
</script>

<h3>Auteurs</h3>
<ul>
    {#await authors}
        <li>chargement...</li>
    {:then data}
        {#each data as row}
            {#if row.username !== 'visiteur'}
                <li><a href="/#/auteurs/{row.id}-{row.slug}">{row.firstname} {row.lastname}</a></li>
            {/if}
        {/each}
    {/await}
</ul>
