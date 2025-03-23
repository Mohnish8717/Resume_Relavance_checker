import React, { useState } from 'react';
import axios from 'axios';

const ResumeUploader = () => {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleResumeUpload = async () => {
    if (!file) return alert("Please select a file first");

    const formData = new FormData();
    formData.append('file', file);

    try {
      setLoading(true);
      const response = await axios.post('/generate_resume/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
        responseType: 'blob', // PDF response
      });

      // Create a link to download the PDF
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'tailored_resume.pdf');
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (error) {
      console.error('Upload failed', error);
      alert('Resume generation failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6 border rounded-md shadow-sm max-w-lg mx-auto">
      <h2 className="text-xl font-bold mb-4">Upload Your Resume</h2>
      <input
        type="file"
        accept=".pdf,.doc,.docx"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-4"
      />
      <button
        onClick={handleResumeUpload}
        disabled={loading}
        className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        {loading ? 'Generating...' : 'Generate Tailored Resume'}
      </button>
    </div>
  );
};

export default ResumeUploader;