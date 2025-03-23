import React, { useState } from "react";
import axios from "axios";
import { Upload, CheckCircle } from "lucide-react";

const HomePage = () => {
  const [file, setFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [downloadUrl, setDownloadUrl] = useState(null);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile && selectedFile.type !== "application/pdf") {
      setError("Only PDF format allowed");
      setFile(null);
    } else {
      setError("");
      setFile(selectedFile);
    }
  };

  const handleEnhanceResume = async () => {
    if (!file || !jobDescription.trim()) {
      alert("Please upload a PDF resume and enter a job description.");
      return;
    }

    const formData = new FormData();
    formData.append("resume_file", file);
    formData.append("job_description", jobDescription);

    setLoading(true);
    setDownloadUrl(null);
    try {
      const response = await axios.post("http://localhost:8000/generate_resume/", formData, {
        responseType: "blob",
      });
    console.log(response)
      const url = window.URL.createObjectURL(new Blob([response.data]));
      setDownloadUrl(url);
    } catch (error) {
      alert("Error generating resume. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-full h-screen flex flex-col bg-gray-50">
      {/* Navbar */}
      <nav className="w-full bg-white shadow-md p-6 text-center text-2xl font-semibold text-gray-800">
        Resume Relevance Checker
      </nav>

      {/* Main Content - Full width & height */}
      <div className="w-full h-full flex items-center justify-center p-8">
        <div className="bg-white shadow-lg rounded-lg p-8 w-full h-full flex flex-col lg:grid lg:grid-cols-2 gap-8">
          {/* Upload Section */}
          <div className="flex flex-col justify-center">
            <h2 className="text-xl font-semibold text-gray-800 text-center mb-6">
              Upload & Analyze Your Resume
            </h2>

            <label className="block text-gray-700 font-medium mb-2">
              Upload Your Resume (PDF only)
            </label>
            <div className="border-2 border-dashed border-gray-300 rounded-lg p-6 flex flex-col items-center justify-center text-center cursor-pointer hover:border-blue-500 transition w-full h-40">
              <input
                type="file"
                onChange={handleFileChange}
                className="hidden"
                id="resume-upload"
              />

              {!file ? (
                <label
                  htmlFor="resume-upload"
                  className="flex flex-col items-center cursor-pointer"
                >
                  <Upload className="text-blue-500 w-14 h-14 mb-2" />
                  <span className="text-gray-500">Click to upload</span>
                </label>
              ) : (
                <a
                  href={URL.createObjectURL(file)}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center justify-center bg-green-500 text-white px-4 py-2 rounded-lg font-medium"
                >
                  <CheckCircle className="w-5 h-5 mr-2" />
                  <span className="underline">{file.name}</span>
                </a>
              )}
            </div>

            {error && <p className="text-red-500 text-sm mt-2">{error}</p>}
          </div>

          {/* Job Description + Button Section */}
          <div className="flex flex-col justify-center">
            <label className="block text-gray-700 font-medium mb-2">
              Job Description
            </label>
            <textarea
              className="w-full px-4 py-3 border border-gray-300 text-gray-900 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 h-40"
              placeholder="Paste the job description here..."
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
            ></textarea>

            <button
              onClick={handleEnhanceResume}
              className="w-full bg-blue-600 text-white mt-6 py-3 rounded-lg font-semibold hover:bg-blue-700 transition"
              disabled={loading}
            >
              {loading ? "Generating..." : "Enhance Resume"}
            </button>

            {downloadUrl && (
              <a
                href={downloadUrl}
                download="tailored_resume.pdf"
                className="block text-blue-600 mt-4 text-center"
              >
                Download Tailored Resume
              </a>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;