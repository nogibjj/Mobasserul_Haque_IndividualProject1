from myLib.lib import (
    read_csv_file, summary_statistics, plot_histograms, 
    plot_scatter_with_hue, plot_box_by_category, plot_correlation_heatmap, 
    plot_scatter_with_trend, plot_bar_by_category
)

file_path = "Customer Purchasing Behaviors.csv"
output_report = "summary_report.md" 

# Reading the data
df = read_csv_file(file_path)

# Writing summary statistics to the summary report file
summary_statistics(df, output_report)

# Generating plots and saving them in the summary report file
# plot_histograms
plot_histograms(df, ['age', 'annual_income', 'purchase_amount', 'purchase_frequency'], 
                output_report)

# plot_scatter_with_hue
plot_scatter_with_hue(df, 'annual_income', 'purchase_amount', 'region', 
                      output_report)

# plot_box_by_category
plot_box_by_category(df, 'region', 'loyalty_score', output_report)

# plot_correlation_heatmap
plot_correlation_heatmap(df, ['purchase_amount', 'purchase_frequency', 'loyalty_score'], 
                         output_report)

# plot_scatter_with_trend
plot_scatter_with_trend(df, 'annual_income', 'purchase_amount', output_report)

# plot_bar_by_category
plot_bar_by_category(df, 'region', 'purchase_amount', output_report)
