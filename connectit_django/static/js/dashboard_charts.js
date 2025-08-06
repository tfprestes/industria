// static/js/dashboard_charts.js

Chart.register(ChartjsPluginDatalabels);

document.addEventListener('DOMContentLoaded', function() {
    function getChartData(chartDataId) {
        const dataScript = document.getElementById(chartDataId);
        if (!dataScript) return null;
        return JSON.parse(dataScript.textContent);
    }

    function initializeHorizontalBarChart(chartId, labelText) {
        const ctx = document.getElementById(chartId);
        const chartData = getChartData(chartId); // ID do canvas e do script são os mesmos
        if (!ctx || !chartData) return;
        
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: chartData.labels,
                datasets: [{
                    label: labelText,
                    data: chartData.data,
                    backgroundColor: chartData.backgroundColor,
                    borderColor: chartData.backgroundColor,
                    borderWidth: 1
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false },
                    datalabels: {
                        anchor: 'end',
                        align: 'start',
                        formatter: v => `R$ ${v.toFixed(2)}`,
                        color: '#fff',
                        font: { weight: 'bold' }
                    }
                },
                scales: {
                    x: { beginAtZero: true, grid: { color: 'rgba(255, 255, 255, 0.1)' }, ticks: { color: '#bbb' } },
                    y: { grid: { color: 'rgba(255, 255, 255, 0.1)' }, ticks: { color: '#bbb' } }
                }
            }
        });
    }

    function initializeStackedBarChart(chartId) {
        const ctx = document.getElementById(chartId);
        const chartData = getChartData(chartId);
        if (!ctx || !chartData) return;

        const datasets = chartData.datasets.map(ds => ({
            label: ds.label,
            data: ds.data,
            backgroundColor: ds.backgroundColor || 'rgba(54, 162, 235, 0.8)',
            borderColor: 'rgba(255, 255, 255, 0.1)',
            borderWidth: 1
        }));
        
        new Chart(ctx, {
            type: 'bar',
            data: { labels: chartData.labels, datasets },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                indexAxis: 'y',
                plugins: { legend: { labels: { color: '#bbb' } }, datalabels: { display: false } },
                scales: {
                    x: { stacked: true, beginAtZero: true, grid: { color: 'rgba(255, 255, 255, 0.1)' }, ticks: { color: '#bbb' } },
                    y: { stacked: true, grid: { color: 'rgba(255, 255, 255, 0.1)' }, ticks: { color: '#bbb' } }
                }
            }
        });
    }

    function initializeLineChart(chartId, labelText) {
        const ctx = document.getElementById(chartId);
        const chartData = getChartData(chartId);
        if (!ctx || !chartData) return;

        new Chart(ctx, {
            type: 'line',
            data: {
                labels: chartData.labels,
                datasets: [{
                    label: labelText,
                    data: chartData.data,
                    borderColor: chartData.borderColor,
                    backgroundColor: 'rgba(255, 255, 255, 0.1)',
                    tension: 0.4,
                    fill: true,
                    pointBackgroundColor: chartData.borderColor,
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: chartData.borderColor
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false }, datalabels: { display: false } },
                scales: {
                    x: { grid: { color: 'rgba(255, 255, 255, 0.1)' }, ticks: { color: '#bbb' } },
                    y: { beginAtZero: true, grid: { color: 'rgba(255, 255, 255, 0.1)' }, ticks: { color: '#bbb' } }
                }
            }
        });
    }

    // Inicialização dos Gráficos
    initializeHorizontalBarChart('costsByComputerSectorChart', 'Custo (R$)');
    initializeHorizontalBarChart('costsByCellphoneSectorChart', 'Custo (R$)');
    initializeHorizontalBarChart('costsByPrinterSectorChart', 'Custo (R$)');
    initializeStackedBarChart('softwareDistributionChart');
    initializeLineChart('costEvolutionChart', 'Custo Total (R$)');
});