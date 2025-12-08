import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Setup and Style
# Setting the theme for a professional "Ryan and Sons" look
sns.set_style("whitegrid")
sns.set_context("talk") # Makes fonts readable for presentations

# 2. Generate Synthetic Data
# Creating realistic data for 100 customers across 3 marketing channels
np.random.seed(42) # Ensures the random numbers are the same every time
n_points = 150

data = {
    'Acquisition Cost': np.random.normal(loc=45, scale=12, size=n_points),
    'Lifetime Value': np.random.normal(loc=280, scale=65, size=n_points),
    'Campaign Channel': np.random.choice(['Email', 'Social Media', 'Organic Search'], size=n_points)
}

# Adjust CLV to have some positive correlation with Cost (higher cost -> slightly higher value)
data['Lifetime Value'] += data['Acquisition Cost'] * 1.5

df = pd.DataFrame(data)

# 3. Initialize the Figure
# Requirement: 8x64 = 512 pixels roughly
plt.figure(figsize=(8, 8))

# 4. Create the Scatterplot
scatter = sns.scatterplot(
    data=df,
    x='Acquisition Cost',
    y='Lifetime Value',
    hue='Campaign Channel',
    style='Campaign Channel', # Different shapes for accessibility/clarity
    s=100, # Marker size
    palette='deep',
    alpha=0.8 # Slight transparency
)

# 5. Professional Styling
plt.title('Customer Lifetime Value vs. Acquisition Cost', fontsize=16, pad=20)
plt.xlabel('Customer Acquisition Cost ($)', fontsize=12)
plt.ylabel('Customer Lifetime Value ($)', fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0) # Move legend outside if needed, or keep standard

# 6. Save the Chart
# Requirement: Save as PNG, 512x512 (8 inches * 64 dpi)
# Note: bbox_inches='tight' trims whitespace which makes the chart look better
# but might slightly alter exact pixel dimensions. This is standard for the assignment.
plt.tight_layout()
plt.savefig('chart.png', dpi=64)

print("Chart generated successfully as chart.png")