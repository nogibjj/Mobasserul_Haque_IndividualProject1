import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from main import (
    summary_statistics, plot_histograms, plot_scatter_with_hue, 
    plot_box_by_category, plot_correlation_heatmap, 
    plot_scatter_with_trend, plot_bar_by_category
)

# Sample data for testing
sample_data = """customer_id,age,annual_income,purchase_amount,purchase_frequency,region,loyalty_score
1,23,50000,200,5,North,80
2,45,60000,300,7,South,85
3,34,55000,250,6,East,90
4,50,65000,400,8,West,70
5,29,70000,350,7,North,75
"""

# Function to create DataFrame from sample data using StringIO
def setup_dataframe():
    return pd.read_csv(StringIO(sample_data))

def test_main_workflow():
    """Test the full workflow in main.py"""
    df = setup_dataframe()
    output_report = "test_report.md"
    
    # Run each function in sequence
    summary_statistics(df, output_report)
    plot_histograms(
        df, ['age', 'annual_income', 'purchase_amount', 'purchase_frequency'], 
        output_report
    )
    plot_scatter_with_hue(
        df, 'annual_income', 'purchase_amount', 'region', output_report
    )
    plot_box_by_category(
        df, 'region', 'loyalty_score', output_report
    )
    plot_correlation_heatmap(
        df, ['purchase_amount', 'purchase_frequency', 'loyalty_score'], 
        output_report
    )
    plot_scatter_with_trend(
        df, 'annual_income', 'purchase_amount', output_report
    )
    plot_bar_by_category(
        df, 'region', 'purchase_amount', output_report
    )
    
    print("test_main_workflow passed")

# Mock plt.show to prevent actual plotting during tests
plt.show = lambda: None

# Run the test
if __name__ == "__main__":
    test_main_workflow()
