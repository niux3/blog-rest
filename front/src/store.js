import {writable} from 'svelte/store'


export let authenticated = writable({
    logged : false,
    username : '',
    id: 0
})

