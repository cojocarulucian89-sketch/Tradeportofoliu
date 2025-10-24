import React, { useState } from "react";

export default function AIAdvisor() {
  const [assets, setAssets] = useState(["OMV", "ENGIE", "Edenred"]);
  const [result, setResult] = useState(null);

  const optimize = async () => {
    const res = await fetch("http://localhost:5000/api/optimize", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ assets }),
    });
    const data = await res.json();
    setResult(data);
  };

  return (
    <div className="ai-card">
      <h2>Asistent AI - Optimizare Portofoliu</h2>
      <button onClick={optimize}>Optimizează</button>
      {result && (
        <div className="output">
          <pre>{JSON.stringify(result.optimized_weights, null, 2)}</pre>
          <p>{result.comment}</p>
        </div>
      )}
    </div>
  );
}
