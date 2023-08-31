<script>
    let categories = (async ()=>{
        let response = await fetch('//localhost:8000/categories')
        return await response.json()
    })()
</script>

<h3>Catégories</h3>
<ul>
    {#await categories}
        <li>chargement...</li>
    {:then data}
        {#each data['categories'] as row}
            <li><a href="/#/categorie/{row.id}-{row.name.replace(' ', '-')}">#{row.name}</a></li>
        {/each}
    {/await}
</ul>
