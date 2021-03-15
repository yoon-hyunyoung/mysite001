import axios from 'axios';
import React, { useState, useContext } from 'react';
import LoginContext from './Util';
import { Redirect } from 'react-router';


const Login =() => {
    
    const login = React.useContext(LoginContext);
    const [email,setEmail] = useState('');
    const [password,setPassword] = useState('');
    const [redirect,setRedirect] = useState(false)

    
    const submit = (e) => {
        // e.preventDefault();
    // http://localhost:8000/api/register     
            axios({
                method: 'get',
                url: 'http://localhost:8000/api/register',
    
                data: {
                    email,
                    password
                }
            })

        console.log({email,password})
        setRedirect(true);
        console.log('sdsdsdsd')
    }
    if (redirect) {
        return <Redirect to='/'/>
    };
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