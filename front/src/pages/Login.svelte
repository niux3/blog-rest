<script>
    import {authenticated} from '../store.js'

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
        fetch('//localhost:8000/users', params).then(resp =>{
            return resp.json()
        }).then(data =>{
            console.log('>>', data)
            if(data['errors'] !== undefined || data['errors'] !== null){
                document.querySelectorAll('form input + span').forEach($el => $el.remove())
                for(let k in data['errors']){
                    let $el = document.querySelector(`form *[name='${k}']`),
                        tplError = `<span style="color:orangered">${data['errors'][k][0]}</span>`
                    $el.insertAdjacentHTML('afterend', tplError)
                }
            }
            if(data['message'] !== undefined && data['message'] === 'ok'){
                authenticated.set({
                    username: data['username'],
                    logged: data['logged'],
                    id: data['id']
                })
                $form.reset()

            }
        })
    }
</script>

<h1>se connecter</h1>
<form method="post" on:submit|preventDefault={onSubmit}>
    <input type="hidden" name="type" value="login">
    <div class="grid-container">
        <div class="grid-x grid-padding-x">
            <div class="medium-6 cell">
                <label>
                    <span>Email</span>
                    <input type="text" name="email" value="dom@dom.com">
                </label>
            </div>
            <div class="medium-6 cell">
                <label>
                    <span>Mot de passe</span>
                    <input type="password" name="password" value="admin">
                </label>
            </div>
            <button class="button medium-12 cell" type="submit">envoyer</button>
        </div>
    </div>
</form>
