import React from "react";
import { Pie } from "react-chartjs-2";

function PieChart({ chartData }) {
  return (
    <div className="chart-container">
      <Pie
        options={{
          plugins: {
            legend: {
              labels: {
                color: "white",
              },
            },
          },
        }}
        data={chartData}
      />
    </div>
  );
}
export default PieChart;
