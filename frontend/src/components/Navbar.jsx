import React from "react";
import { Link } from "react-router-dom";
import logo from "../assets/logo.jpeg"; // Import your logo
import "../App.css"

const Navbar = () => {
  return (
    <nav className="bg-white mt-25 shadow-md p-4 w-full flex items-center justify-between">
      {/* Logo on the left */}
      <div className="flex items-center space-x-4">
        <img src={logo} alt="Logo" className="w-14 h-14 sm:w-16 sm:h-16" />
      </div>

      {/* Navigation Links */}
      <div className="flex space-x-8 text-lg font-medium">
        <Link to="/" className="text-gray-600 hover:underline">Home</Link>
        <Link to="/optimized-resume" className="text-gray-600 hover:underline">Optimized Resume</Link>
        <Link to="/resume-analysis" className="text-gray-600 hover:underline">Resume Analysis</Link>
      </div>
    </nav>
  );
};

export default Navbar;
