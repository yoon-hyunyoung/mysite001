import React from 'react';

const Login =() => {

    const [email,setEmail] = useState('');
    const [password,setPassword] = useState('');

    const submit = (e) => {
        e.preventDefault();
        const a=axios({
            method: 'post',
            url: 'http://localhost:8000/api/register',
            data: {
                username,
                email,
                password
            }
        })
        console.log(a,'swdenfhufhnjweifjefhfrjweof9')
     console.log({username,email,password})
     setRedirect(true);
     console.log('sdsdsdsd')
    }

    return(
        <form onSubmit={submit}>
            <h1 className="h3 mb-3 fw-normal">Please sign in</h1>
            <input type="email" className="form-control" placeholder="Email address" required
                   onChange={e => setEmail(e.target.value)}
            />

            <input type="password" className="form-control" placeholder="Password" required
                   onChange={e => setPassword(e.target.value)}
            />

            <button className="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
        </form>
    )
}

export default Login