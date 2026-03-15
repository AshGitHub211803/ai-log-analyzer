import React, { useState } from "react";

function App() {

  const [file, setFile] = useState(null);
  const [result, setResult] = useState("");

  const handleUpload = async () => {

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://localhost:8000/analyze", {
      method: "POST",
      body: formData
    });

    const data = await response.json();

    setResult(data.analysis);
  };

  return (
    <div style={{padding: "40px"}}>

      <h2>AI Log Analyzer</h2>

      <input 
        type="file" 
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={handleUpload}>
        Analyze Logs
      </button>

      <h3>Result</h3>

      <pre>{result}</pre>

    </div>
  );
}

export default App;