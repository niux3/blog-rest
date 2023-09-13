import Home from './pages/Home.svelte'
import Article from './pages/Article.svelte'
import Categories from './pages/Categories.svelte'
import Authors from './pages/Authors.svelte'
import Register from './pages/Register.svelte'
import Login from './pages/Login.svelte'


let routes = {
    '#/home': Home,
    '#/article/[0-9]+[a-z0-9_-]+' : Article,
    '#/categorie/[0-9]+[a-z0-9_-]+' : Categories,
    '#/auteurs/[0-9]+[a-z0-9_-]+' : Authors,
    '#/s-inscrire' : Register,
    '#/se-connecter' : Login,

}

export default routes
