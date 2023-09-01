import Home from './pages/Home.svelte'
import Article from './pages/Article.svelte'
import Categories from './pages/Categories.svelte'
import Authors from './pages/Authors.svelte'


let routes = {
    '#/home': Home,
    '#/article/[0-9]+[a-z0-9_-]+' : Article,
    '#/categorie/[0-9]+[a-z0-9_-]+' : Categories,
    '#/auteurs/[0-9]+[a-z0-9_-]+' : Authors,

}

export default routes
