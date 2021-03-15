import './K1_1.css';
import axios from 'axios'
import React, { useEffect, useState } from 'react'
// import a from './images/ulsan.PNG'
// import b from './images/pohang.png'
// import c from './images/suwon.png'
// import d from './images/jeonbuk.png'
// import e from './images/seoul.png'
// import f from './images/incheon.png'
// import g from './images/jeju.png'
// import h from './images/daegu.png'
// import i from './images/sungnam.png'
// import j from './images/suwonFC.png'
// import k from './images/gwangju.png'
// import l from './images/gangwon.png'
import a from './../images/aa.jpg' // ../이 폴더 속이란 뜻인 것 같다..



export default function K1_1() {
  const [test, setTest] = useState([]);

  React.useEffect(() => {
  axios.get("http://localhost:8000/api/k1/2")
  
    .then(response => {
      console.log(response);
      const {data} = response;
      setTest(data);
         // response  
    }).catch(error => {
        // 오류발생시 실행
        console.log(error)
    });
  },[])
  return(
  
  <div style={{height:'1200px',width:'1200px',position:'absolute',backgroundImage:`url(${a})`,zIndex:9999}}>
  <div style={{margin:'70px',marginLeft:'100px'}}>
  <thead id='table' style={{textAlign:'center', fontSize:'13px'}}>
      <tr id='tr'>
        <td>순위</td>
        <td colSpan={2}>구단</td>
        
        <td>경기</td>
        <td>승점</td>
        <td>승</td>
        <td>무</td>
        <td>패</td>
        <td>득점</td>
        <td>실점</td>
        <td>골득실</td>

      </tr>
      </thead>
    
  { test.map(( v ) => {

    return (
      
        <tbody id='table'>
      <tr key={v.id} style={{color: 'white', fontWeight: 700, textAlign: 'center'}}>
        <td style={{width:'40px', backgroundColor: '#082150', margin: '10px'}}>{v.ranking}위</td>
        <td><img id='img1' src={v.logos}/></td>
        <td style={{width:'55px',backgroundColor: '#082150', margin: '10px'}}>{v.name}</td>
        <td style={{opacity: 0.7,backgroundColor: '#082150', margin: '10px'}}>{v.matches}</td>
        <td style={{backgroundColor: '#C51E1E', margin: '10px'}}>{v.points}</td>
        <td style={{opacity: 0.7,backgroundColor: '#082150', margin: '10px'}}>{v.wons}</td>
        <td style={{opacity: 0.7,backgroundColor: '#082150', margin: '10px'}}>{v.draws}</td>
        <td style={{opacity: 0.7,backgroundColor: '#082150', margin: '10px'}}>{v.losses}</td>
        <td style={{opacity: 0.8,backgroundColor: '#082150', margin: '10px'}}>{v.getgoals}</td>
        <td style={{opacity: 0.7,backgroundColor: '#082150', margin: '10px'}}>{v.lostgoals}</td>
        <td style={{opacity: 0.7,backgroundColor: '#082150', margin: '10px'}}>{v.get_losts}</td>
        

      </tr>
      </tbody>
    );
}
)
}</div></div>)
}