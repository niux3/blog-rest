<script>
    import {authenticated} from '../store.js'


    let data = (async ()=>{
        let full_url = window.location.hash,
            end_url = full_url.substring(full_url.lastIndexOf('/') + 1),
            [all, id, ...others] = [...end_url.matchAll(/^(\d+)-/g)].pop()
        let resp = await fetch(`//localhost:8000/post/${id}`)
        return await resp.json()
    })()

    let users = (async ()=>{
        let resp = await fetch('//localhost:8000/users')
        return await resp.json()
    })()

    let auth = {}
    authenticated.subscribe(o => auth = o)

    let onSubmit = e =>{
        let headers = new Headers({
                "X-Requested-With": "XMLHttpRequest",
                "Accept": "application/json",
                "Content-Type": 'application/json'
            }),
            $form = e.target,
            object = {},
            formData = new FormData($form)
        formData.forEach((value, key) => object[key] = value)
        object['authors'] = auth.id

        let params = {
            method: $form.method,
            headers,
            cache: 'no-cache',
            redirect: 'follow',
            referrerPolicy: 'no-referrer',
            mode: "cors",
            body: JSON.stringify(object)
        }
        e.preventDefault()
        fetch('//localhost:8000/comments', params).then(resp =>{
            if(resp.ok === true)
                return resp.json()
        }).then(d =>{
            $form.reset()
            data = (async ()=>{
                let full_url = window.location.hash,
                    end_url = full_url.substring(full_url.lastIndexOf('/') + 1),
                    [all, id, ...others] = [...end_url.matchAll(/^(\d+)-/g)].pop()
                let resp = await fetch(`//localhost:8000/post/${id}`)
                return await resp.json()
            })()
        })
    }

</script>

{#await data}
    <p>Chargement...</p>
{:then row}
    <article>
        <img src={row.illustration} alt="" class="thumbnail">
        <h2>{row.title}</h2>
        <p><small> <a href={"/#/categorie/1-" + row.categorie}>#{row.categorie}</a></small> - <small>créé le <i>{row.created}</i></small> par <small><strong>{row.author}</strong></small></p>
        <div>{@html row.content}</div>
    </article>
    {#if row.comments.length > 0}
        <aside>
            <h3>les commentaires de l'article : {row.title}</h3>
            <ul>
                {#each row.comments as comment}
                    <li>
                        {#if comment.title !== ''}<h4>{comment.title}</h4>{/if}
                        <p>créé le <small>{comment.created}</small> par <strong><small>{comment.author}</small></strong></p>
                        <div>{@html comment.content}</div>
                    </li>
                {/each}
            </ul>
        </aside>
    {/if}
    {#if auth.logged === true}
    <form on:submit|preventDefault={onSubmit} method="post">
        <input type="hidden" name="posts" value={row.id}>
        <fieldset class="fieldset">
            <legend>Laisser un commentaire</legend>
            <div class="input text">
                <label>
                    <span>title</span>
                    <input type="text" name="title" placeholder="laisser un titre">
                </label>
            </div>
            <div class="input textarea">
                <label>
                    <span>commentaire</span>
                    <textarea name="content" placeholder="laisser un commentaire" required></textarea>
                </label>
            </div>
            <div class="input submit">
                <button class="button expanded">envoyer</button>
            </div>
        </fieldset>
    </form>
    {/if}
{/await}

<style>
    textarea{
        resize: vertical;
    }
</style>
