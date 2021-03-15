import React from 'react';
import { BrowserRouter, Switch, Route, Link } from "react-router-dom"

const Nav =()=>{
    return(
        <nav className='navbar navbar-expand-md navbar-dark bg-dark mb-4'>
            <div className='container-fluid'>
                <Link to='/' className='navbar-brand'>HOME</Link>
            <div>
                <ul className="navbar-nav me-auto mb-2 mb-md-0">
                <li className="nav-item active">
                    <Link to='/login' className="nav-link" href='#'>LOGIN</Link>
                </li>
                <li>
                    <Link to='/register' className="nav-link" href="#">REGISTER</Link>
                </li>
                </ul>
            </div>
            </div>
        </nav>
    )
}

export default Nav