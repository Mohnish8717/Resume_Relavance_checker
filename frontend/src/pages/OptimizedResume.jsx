import React, { useEffect, useState } from "react";
import { jsPDF } from "jspdf";
import { Download, BarChart } from "lucide-react";
import "../App.css";

const OptimizedResume = () => {
  const [resumeContent, setResumeContent] = useState("Loading optimized resume...");

  useEffect(() => {
    fetch("http://localhost:5000/api/optimized-resume") // Update with actual API endpoint
      .then((response) => response.json())
      .then((data) => setResumeContent(data.optimizedResume))
      .catch((error) => {
        console.error("Error fetching optimized resume:", error);
        setResumeContent("Failed to load optimized resume...");
      });
  }, []);

  const handleDownload = () => {
    if (!resumeContent) {
      alert("No resume content available to download.");
      return;
    }

    const doc = new jsPDF();
    doc.setFont("helvetica", "bold");
    doc.setFontSize(16);
    doc.text("Optimized Resume", 20, 20);

    doc.setFont("helvetica", "normal");
    doc.setFontSize(12);

    const pageWidth = doc.internal.pageSize.getWidth();
    const textWidth = pageWidth - 40;
    doc.text(resumeContent, 20, 40, { maxWidth: textWidth });

    doc.save("Optimized_Resume.pdf");
  };

  return (
    <div className="w-full m-auto min-h-screen flex flex-col bg-gray-100">
      {/* Navbar */}
      <nav className="w-full bg-white shadow-md p-4 text-center text-lg sm:text-2xl font-semibold text-gray-800">
        Optimized Resume
      </nav>

      {/* Main Content */}
      <div className="w-full flex justify-center p-4 sm:p-8">
        <div className="bg-white shadow-lg rounded-lg p-6 sm:p-8 w-full max-w-3xl flex flex-col">
          <h1 className="text-xl sm:text-2xl font-bold text-center text-gray-900 mb-4 sm:mb-6">
            Optimized Resume
          </h1>

          {/* Resume Content */}
          <div className="bg-gray-100 p-4 sm:p-5 rounded-lg text-sm font-mono min-h-[150px] sm:min-h-[250px] max-h-96 overflow-y-auto border border-gray-300 shadow-inner">
            <pre className="whitespace-pre-wrap text-black">{resumeContent}</pre>
          </div>

          {/* Buttons */}
          <div className="flex flex-col sm:flex-row justify-center items-center gap-3 sm:gap-6 mt-6 sm:mt-8 w-full">
            {/* Download Resume Button */}
            <button
              onClick={handleDownload}
              className="flex items-center justify-center gap-2 bg-blue-600 text-white px-5 py-2 sm:px-6 sm:py-3 rounded-lg shadow-md hover:bg-blue-700 transition w-full sm:w-auto"
            >
              <Download size={20} />
              Download PDF
            </button>

            {/* View Analysis Button */}
            <a
              href="/resume-analysis"
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center justify-center gap-2 bg-green-500 text-white px-5 py-2 sm:px-6 sm:py-3 rounded-lg shadow-md hover:bg-green-600 transition w-full sm:w-auto"
            >
              <BarChart size={20} />
              View Analysis
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default OptimizedResume;
