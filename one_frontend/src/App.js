import './App.css';
import axios from 'axios'
import React, { useEffect, useState } from 'react'

// import K1_1 from './pages/K1_1';
// import K1_2 from './pages/K1_2';
// import K2_1 from './pages/K2_1';
// import K2_2 from './pages/K2_2';
import Home from './pages/Home';
import Login from 'loginpages/Login';
import Register from 'loginpages/Register';

import Nav from 'components/Nav';

import { BrowserRouter, Route } from 'react-router-dom';



export default function App() {
  // const [token, setToken] = useState();
  
  // if(!token) {
  //   return <Login setToken={setToken} />
  // }
  return(
  
    <div className='App'>
      <BrowserRouter>
        <Nav/>

      <main className="form-signin">
          
            <Route exact path='/' component={Home} />
            <Route path='/login' component={Login} />
            <Route path='/register' component={Register} />
          
      </main>
      </BrowserRouter>
    </div>
  )
}