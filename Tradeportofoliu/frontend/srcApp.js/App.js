import React from "react";
import Dashboard from "./components/Dashboard";
import AIAdvisor from "./components/AIAdvisor";
import "./styles/theme.css";

export default function App() {
  return (
    <div className="container">
      <h1>Tradeportofoliu</h1>
      <Dashboard />
      <AIAdvisor />
    </div>
  );
}
