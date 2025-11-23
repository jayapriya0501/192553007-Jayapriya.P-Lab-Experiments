"""
Lab Program 3: Data Visualization
Demonstrates: Bar Chart, Pie Chart, and Histogram for business data
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    print("=" * 70)
    print("LAB PROGRAM 3: DATA VISUALIZATION")
    print("=" * 70)
    print()
    
    # Load the products dataset
    print("Loading products dataset...")
    df = pd.read_csv('products_data.csv')
    print("Dataset loaded successfully!\n")
    
    # Display sample data
    print("Sample Data:")
    print(df.head(10).to_string(index=False))
    print()
    
    # Create figure with 3 subplots
    fig = plt.figure(figsize=(15, 5))
    fig.suptitle('Business Data Visualizations', fontsize=16, fontweight='bold')
    
    # =================================================================
    # 1. BAR CHART - Product Prices Comparison
    # =================================================================
    print("Creating visualizations...")
    print("1. Bar Chart - Product Prices")
    
    ax1 = plt.subplot(1, 3, 1)
    
    # Select top 10 products by price for better visibility
    top_products = df.nlargest(10, 'Price')
    
    bars = ax1.barh(top_products['Product_Name'], top_products['Price'], 
                    color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8',
                           '#F7DC6F', '#BB8FCE', '#85C1E2', '#F8B88B', '#AAB7B8'])
    
    ax1.set_xlabel('Price ($)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Product Name', fontsize=11, fontweight='bold')
    ax1.set_title('Top 10 Products by Price', fontsize=12, fontweight='bold', pad=15)
    ax1.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Add value labels on bars
    for i, (bar, price) in enumerate(zip(bars, top_products['Price'])):
        ax1.text(price + 20, bar.get_y() + bar.get_height()/2, 
                f'${price}', va='center', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    
    # =================================================================
    # 2. PIE CHART - Category Distribution
    # =================================================================
    print("2. Pie Chart - Category Distribution")
    
    ax2 = plt.subplot(1, 3, 2)
    
    # Calculate percentage distribution by category
    category_counts = df['Category'].value_counts()
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    explode = [0.05] * len(category_counts)  # Slightly separate slices
    
    wedges, texts, autotexts = ax2.pie(category_counts, 
                                        labels=category_counts.index,
                                        autopct='%1.1f%%',
                                        colors=colors[:len(category_counts)],
                                        explode=explode,
                                        shadow=True,
                                        startangle=90)
    
    # Enhance text
    for text in texts:
        text.set_fontsize(11)
        text.set_fontweight('bold')
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(10)
        autotext.set_fontweight('bold')
    
    ax2.set_title('Product Category Distribution', fontsize=12, fontweight='bold', pad=15)
    
    # =================================================================
    # 3. HISTOGRAM - Sales Count Frequency Distribution
    # =================================================================
    print("3. Histogram - Sales Frequency Distribution")
    
    ax3 = plt.subplot(1, 3, 3)
    
    # Create histogram
    n, bins, patches = ax3.hist(df['Sales_Count'], bins=10, 
                                color='#4ECDC4', edgecolor='black', 
                                alpha=0.7, linewidth=1.2)
    
    # Color bars with gradient
    cm = plt.cm.viridis
    bin_centers = 0.5 * (bins[:-1] + bins[1:])
    col = bin_centers - min(bin_centers)
    col /= max(col)
    
    for c, p in zip(col, patches):
        plt.setp(p, 'facecolor', cm(c))
    
    ax3.set_xlabel('Sales Count', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Frequency (Number of Products)', fontsize=11, fontweight='bold')
    ax3.set_title('Sales Count Distribution', fontsize=12, fontweight='bold', pad=15)
    ax3.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Add statistics to the plot
    mean_sales = df['Sales_Count'].mean()
    median_sales = df['Sales_Count'].median()
    ax3.axvline(mean_sales, color='red', linestyle='--', linewidth=2, 
                label=f'Mean: {mean_sales:.0f}')
    ax3.axvline(median_sales, color='orange', linestyle='--', linewidth=2, 
                label=f'Median: {median_sales:.0f}')
    ax3.legend(fontsize=9)
    
    # Adjust layout and display
    plt.tight_layout()
    
    print("\n✓ All visualizations created successfully!")
    print("\nClosing the plot window will continue the program...")
    plt.show()
    
    # =================================================================
    # Statistical Summary
    # =================================================================
    print("\n" + "=" * 70)
    print("STATISTICAL SUMMARY")
    print("=" * 70)
    
    print("\nPrice Statistics:")
    print(f"  • Average Price: ${df['Price'].mean():.2f}")
    print(f"  • Median Price: ${df['Price'].median():.2f}")
    print(f"  • Price Range: ${df['Price'].min()} - ${df['Price'].max()}")
    
    print("\nCategory Distribution:")
    for category, count in category_counts.items():
        percentage = (count / len(df)) * 100
        print(f"  • {category}: {count} products ({percentage:.1f}%)")
    
    print("\nSales Count Statistics:")
    print(f"  • Average Sales Count: {df['Sales_Count'].mean():.0f} units")
    print(f"  • Median Sales Count: {df['Sales_Count'].median():.0f} units")
    print(f"  • Total Units Sold: {df['Sales_Count'].sum():,} units")
    print(f"  • Best Seller: {df.loc[df['Sales_Count'].idxmax(), 'Product_Name']} ({df['Sales_Count'].max()} units)")
    
    print("\n" + "=" * 70)
    print("✓ Visualization Program Complete!")
    print("=" * 70)

if __name__ == "__main__":
    main()
