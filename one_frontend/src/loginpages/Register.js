import React, { useState } from 'react';
import axios from 'axios'
import { Redirect } from 'react-router';
const Register =() => {
    const [username, setUsername] = useState('');
    const [email,setEmail] = useState('');
    const [password,setPassword] = useState('');
    const [redirect,setRedirect] = useState(false)


    const submit = (e) => {
        // e.preventDefault();
// http://localhost:8000/api/register     
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
    if(redirect) {
        return <Redirect to='/login'/>;
    }



    return(            
        <form onSubmit={submit}>
            <h1 className="h3 mb-3 fw-normal">Please register</h1>

            <input className="form-control" placeholder="Name" required
                   onChange={e => setUsername(e.target.value)}
            />
            
            <input type="email" className="form-control" placeholder="Email address" required
                   onChange={e => setEmail(e.target.value)}/>            
            
            <input type="password" className="form-control" placeholder="Password" required
                   onChange={e => setPassword(e.target.value)}/>            
            
            <button className="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>        
        </form>
    )
}

export default Register