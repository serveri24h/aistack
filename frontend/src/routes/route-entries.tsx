import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import ImgGen from './pages/ImageGenerator';
import TextGen from './pages/TextGenerator';

const PageHeader: React.FC = () => {
    return (
        <div style={{
            backgroundColor:'#110022',
            width:"100%",
            color:"#ffffff"
        }}> 
            <h1> THIS IS HEADER </h1>
        </div>
    )
}

const PageSideBar: React.FC = () => {
    return (
        <div style={{
            backgroundColor:'#110022',
            color:"#ffffff"
        }}> 
            <h1> THIS </h1>
            <h1> IS </h1>
            <h1> SideBar </h1>
        </div>
    )
}

const RouteEntries: React.FC = () => {
  return (
    <>
        <PageHeader/>
        <div className= 'sibar-split' style={{
            display:'flex',
            flexDirection:'row',
            height:'100%',
            width: '100%'
        }}>
            <PageSideBar/>
            <Router>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/img" element={<ImgGen />} />
                    <Route path="/txt" element={<TextGen />} />
                </Routes>
            </Router>
        </div>
    </>
  );
};

export default RouteEntries;