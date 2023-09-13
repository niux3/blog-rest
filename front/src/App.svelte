<script>
    import {onMount} from 'svelte'
    import Categories from './components/Categories.svelte'
    import Authors from './components/Authors.svelte'
    import User from './components/User.svelte'
    import Header from './components/commons/Header.svelte'
    import routes from './routes'

    onMount(()=>{
        if(window.location.hash === ''){
            let [first_route, ...others] = Object.keys(routes)
            window.location.hash = first_route.substring(1)
        }else{
            component = getComponent()
        }
    })

    let component,
        getComponent = () =>{
            for(let k in routes){
                if(new RegExp(k).test(window.location.hash)){
                    return routes[k]
                }
            }
        },
        hashChange = () => component = getComponent()

</script>
<svelte:window on:hashchange={hashChange} />
<main>
    <Header />
    <div class="grid-container">
        <div class="grid-x grid-margin-x">
            <div class="medium-9 cell">
                <svelte:component this={component} />
            </div>
            <div class="medium-3 cell">
                <div class="sticky">
                    <Categories />
                    <Authors />
                    <User />
                </div>
            </div>
        </div>
    </div>
</main>


<style>
    .sticky{
        position: sticky;
        top: 10px;
    }
</style>
