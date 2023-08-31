<script>
    import Articles from "../components/Articles.svelte"

    let getParams = () =>{
        let full_url = window.location.hash,
            end_url = full_url.substring(full_url.lastIndexOf('/') + 1),
            [all, id, category] = [...end_url.matchAll(/^(\d+)-([a-z0-9-]+)/g)][0]
        return {
            id,
            category
        }
    }
    $: url = '//localhost:8000/search-categories/' + getParams().id
    let hashChange = ()=> {
        url = '//localhost:8000/search-categories/' + getParams().id
    }

</script>

<svelte:window on:hashchange={hashChange} />
{#key url}
    <Articles url={url} title={`catégorie : ${getParams().category}`}/>
{/key}
