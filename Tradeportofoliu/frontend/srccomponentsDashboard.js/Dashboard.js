import React, { useEffect, useState } from "react";

export default function Dashboard() {
  const [portfolio, setPortfolio] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/portfolio")
      .then((r) => r.json())
      .then(setPortfolio);
  }, []);

  return (
    <div className="card">
      <h2>Portofoliul tău</h2>
      <ul>
        {portfolio.map((p) => (
          <li key={p.id}>
            {p.symbol}: {p.value} €
          </li>
        ))}
      </ul>
    </div>
  );
}
