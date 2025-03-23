import React from "react";

const ResumeAnalysis = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 px-4 sm:px-6 lg:px-8">
      <div className="w-full max-w-lg bg-white p-6 sm:p-8 rounded-xl shadow-xl text-center">
        <h1 className="text-3xl font-bold text-gray-900 mb-6">Resume Analysis</h1>

        {/* Data Visualization */}
        <div className="bg-gray-200 p-4 sm:p-6 rounded-lg">
          <p className="text-lg font-semibold text-gray-800">
            Enhancement Score: <span className="font-bold">85%</span>
          </p>
          <ul className="mt-3 text-gray-700 text-sm space-y-1 text-left">
            <li>✅ Added keywords from job description.</li>
            <li>✅ Improved bullet points.</li>
            <li>✅ Removed unnecessary content.</li>
          </ul>
        </div>

        {/* Go Back Button */}
        <button
          onClick={() => window.history.back()}
          className="w-full mt-6 bg-black text-white py-2 rounded-lg hover:bg-gray-800 transition"
        >
          Go Back
        </button>
      </div>
    </div>
  );
};

export default ResumeAnalysis;
