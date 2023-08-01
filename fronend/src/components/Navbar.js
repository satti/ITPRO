import React from "react";
import { NavLink } from "react-router-dom";
import './navbar.css';
const Navbar = () => {
    return (
        <div className="nav">
            <div className="nav-item">
                <NavLink to="/" className="nav-link">Home</NavLink>
            </div>
            <div className="nav-item">
                <NavLink to="/subjects" className="nav-link">Subjects</NavLink>
            </div>
            <div className="nav-item">
                <NavLink to="/create" className="nav-link">Subcreate</NavLink>
            </div>
        </div>
    )
}

export default Navbar