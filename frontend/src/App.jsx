import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home"; // Changed from HomePage to Home
import OptimizedResume from "./pages/OptimizedResume";
import ResumeAnalysis from "./pages/ResumeAnalysis";
import NotFound from "./components/NotFound";
import ResumeUploader from "./components/ResumeUploader"; // New import added

const App = () => {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <Navbar /> {/* Navbar added here */}
        <div className="max-w-7xl mx-auto px-4"> {/* Added container for alignment */}
          <Routes>
            <Route path="/" element={<Home />} /> {/* Updated Home */}
            <Route path="/optimized-resume" element={<OptimizedResume />} />
            <Route path="/resume-analysis" element={<ResumeAnalysis />} />
            <Route path="/upload-resume" element={<ResumeUploader />} /> {/* New route added */}
            <Route path="*" element={<NotFound />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default App;
