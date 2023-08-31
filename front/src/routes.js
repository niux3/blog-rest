import Home from './pages/Home.svelte'
import Article from './pages/Article.svelte'
import Categories from './pages/Categories.svelte'


let routes = {
    '#/home': Home,
    '#/article/[0-9]+[a-z0-9_-]+' : Article,
    '#/categorie/[0-9]+[a-z0-9_-]+' : Categories,

}

export default routes
