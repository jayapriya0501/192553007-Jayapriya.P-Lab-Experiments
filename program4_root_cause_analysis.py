"""
Lab Program 4: Root Cause Analysis
Demonstrates: Performance drop identification and cause analysis using metrics
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    print("=" * 70)
    print("LAB PROGRAM 4: ROOT CAUSE ANALYSIS")
    print("=" * 70)
    print()
    
    # Load the monthly performance dataset
    print("Loading monthly performance dataset...")
    df = pd.read_csv('monthly_performance.csv')
    print("Dataset loaded successfully!\n")
    
    # Display the data
    print("-" * 70)
    print("MONTHLY PERFORMANCE DATA")
    print("-" * 70)
    print(df.to_string(index=False))
    print()
    
    # =================================================================
    # 1. Identify Performance Drops
    # =================================================================
    print("=" * 70)
    print("1. PERFORMANCE DROP IDENTIFICATION")
    print("=" * 70)
    
    # Calculate month-over-month changes
    df['Revenue_Change_Pct'] = df['Revenue'].pct_change() * 100
    df['Satisfaction_Change'] = df['Customer_Satisfaction'].diff()
    
    # Identify months with drops
    revenue_threshold = -5  # 5% drop
    satisfaction_threshold = -0.3  # 0.3 point drop
    
    print("\nRevenue Changes (Month-over-Month):")
    for i, row in df.iterrows():
        if pd.notna(row['Revenue_Change_Pct']):
            change = row['Revenue_Change_Pct']
            indicator = "📉 DROP" if change < 0 else "📈 GROWTH"
            print(f"  {row['Month']}: {change:+.1f}% {indicator}")
    
    print("\nCustomer Satisfaction Changes:")
    for i, row in df.iterrows():
        if pd.notna(row['Satisfaction_Change']):
            change = row['Satisfaction_Change']
            indicator = "📉 DROP" if change < 0 else "📈 IMPROVEMENT"
            print(f"  {row['Month']}: {change:+.1f} points {indicator}")
    
    # Identify problem months
    problem_months = df[
        (df['Revenue_Change_Pct'] < revenue_threshold) | 
        (df['Satisfaction_Change'] < satisfaction_threshold)
    ]['Month'].tolist()
    
    print(f"\n⚠️  MONTHS WITH SIGNIFICANT PERFORMANCE DROPS:")
    if problem_months:
        for month in problem_months:
            print(f"  • {month}")
    else:
        print("  No significant drops detected")
    
    print()
    
    # =================================================================
    # 2. Root Cause Analysis
    # =================================================================
    print("=" * 70)
    print("2. ROOT CAUSE ANALYSIS")
    print("=" * 70)
    
    # Analyze correlations
    print("\nCorrelation Analysis:")
    metrics = ['Revenue', 'Customer_Satisfaction', 'Marketing_Budget', 'Returns', 'Support_Tickets']
    correlation_matrix = df[metrics].corr()
    print(correlation_matrix.round(3))
    print()
    
    # Key findings
    print("Key Correlation Findings:")
    rev_sat_corr = df['Revenue'].corr(df['Customer_Satisfaction'])
    rev_returns_corr = df['Revenue'].corr(df['Returns'])
    sat_tickets_corr = df['Customer_Satisfaction'].corr(df['Support_Tickets'])
    
    print(f"  • Revenue vs Customer Satisfaction: {rev_sat_corr:.3f}")
    print(f"    → {'Strong positive' if rev_sat_corr > 0.7 else 'Moderate'} relationship")
    print(f"  • Revenue vs Returns: {rev_returns_corr:.3f}")
    print(f"    → Returns {'negatively' if rev_returns_corr < 0 else 'positively'} impact revenue")
    print(f"  • Satisfaction vs Support Tickets: {sat_tickets_corr:.3f}")
    print(f"    → More tickets {'strongly reduce' if sat_tickets_corr < -0.7 else 'reduce'} satisfaction")
    print()
    
    # Detailed analysis for problem months
    if problem_months:
        print("Detailed Analysis of Problem Months:")
        print("-" * 70)
        
        for month in problem_months:
            month_data = df[df['Month'] == month].iloc[0]
            month_idx = df[df['Month'] == month].index[0]
            
            if month_idx > 0:
                prev_data = df.iloc[month_idx - 1]
                
                print(f"\n{month}:")
                print(f"  Revenue: ${month_data['Revenue']:,} ({month_data['Revenue_Change_Pct']:+.1f}%)")
                print(f"  Customer Satisfaction: {month_data['Customer_Satisfaction']:.1f}/10 ({month_data['Satisfaction_Change']:+.1f})")
                
                print(f"\n  Possible Root Causes:")
                
                # Check returns
                if month_data['Returns'] > df['Returns'].mean():
                    increase = ((month_data['Returns'] / prev_data['Returns']) - 1) * 100
                    print(f"    ⚠️  High product returns: {month_data['Returns']} (+{increase:.1f}% from previous month)")
                    print(f"       → Suggests quality issues or unmet customer expectations")
                
                # Check support tickets
                if month_data['Support_Tickets'] > df['Support_Tickets'].mean():
                    increase = ((month_data['Support_Tickets'] / prev_data['Support_Tickets']) - 1) * 100
                    print(f"    ⚠️  High support tickets: {month_data['Support_Tickets']} (+{increase:.1f}% from previous month)")
                    print(f"       → Indicates customer service issues or product problems")
                
                # Check marketing
                marketing_change = ((month_data['Marketing_Budget'] / prev_data['Marketing_Budget']) - 1) * 100
                if marketing_change < 0:
                    print(f"    ⚠️  Reduced marketing budget: ${month_data['Marketing_Budget']:,} ({marketing_change:.1f}%)")
                    print(f"       → Lower marketing spend may have reduced customer acquisition")
    
    print()
    
    # =================================================================
    # 3. Recommendations
    # =================================================================
    print("=" * 70)
    print("3. RECOMMENDATIONS")
    print("=" * 70)
    
    print("\nBased on the analysis, here are the recommended actions:\n")
    
    avg_returns = df['Returns'].mean()
    avg_tickets = df['Support_Tickets'].mean()
    
    print("1. QUALITY IMPROVEMENT")
    print(f"   • Average returns: {avg_returns:.0f} units/month")
    print(f"   • ACTION: Investigate products with high return rates")
    print(f"   • ACTION: Implement better quality control measures")
    print()
    
    print("2. CUSTOMER SUPPORT ENHANCEMENT")
    print(f"   • Average support tickets: {avg_tickets:.0f} tickets/month")
    print(f"   • ACTION: Increase support staff during high-volume months")
    print(f"   • ACTION: Create self-service resources to reduce ticket volume")
    print()
    
    print("3. MARKETING OPTIMIZATION")
    best_marketing_month = df.loc[df['Revenue'].idxmax(), 'Month']
    best_marketing_budget = df.loc[df['Revenue'].idxmax(), 'Marketing_Budget']
    print(f"   • Best performing month: {best_marketing_month} (${best_marketing_budget:,} marketing)")
    print(f"   • ACTION: Maintain consistent marketing investment")
    print(f"   • ACTION: Focus on high-ROI marketing channels")
    print()
    
    print("4. PROACTIVE MONITORING")
    print(f"   • ACTION: Set up real-time alerts for satisfaction drops")
    print(f"   • ACTION: Monthly review of returns and support ticket trends")
    print(f"   • ACTION: Customer feedback surveys to identify issues early")
    print()
    
    # =================================================================
    # 4. Visualizations
    # =================================================================
    print("=" * 70)
    print("4. VISUALIZATIONS")
    print("=" * 70)
    print("\nGenerating visualizations...")
    
    # Create comprehensive visualization
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Root Cause Analysis - Monthly Performance Metrics', 
                 fontsize=16, fontweight='bold')
    
    months_short = df['Month'].str[:3]  # Abbreviated month names
    
    # Plot 1: Revenue Trend
    ax1 = axes[0, 0]
    ax1.plot(months_short, df['Revenue'], marker='o', linewidth=2, 
             color='#2E86AB', markersize=8)
    ax1.fill_between(range(len(df)), df['Revenue'], alpha=0.3, color='#2E86AB')
    ax1.set_xlabel('Month', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Revenue ($)', fontsize=11, fontweight='bold')
    ax1.set_title('Monthly Revenue Trend', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.tick_params(axis='x', rotation=45)
    
    # Highlight problem months
    for month in problem_months:
        month_idx = df[df['Month'] == month].index[0]
        ax1.scatter(month_idx, df.loc[month_idx, 'Revenue'], 
                   color='red', s=200, zorder=5, marker='X')
    
    # Plot 2: Customer Satisfaction
    ax2 = axes[0, 1]
    ax2.plot(months_short, df['Customer_Satisfaction'], marker='s', 
             linewidth=2, color='#A23B72', markersize=8)
    ax2.fill_between(range(len(df)), df['Customer_Satisfaction'], alpha=0.3, color='#A23B72')
    ax2.set_xlabel('Month', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Satisfaction Score', fontsize=11, fontweight='bold')
    ax2.set_title('Customer Satisfaction Trend', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3, linestyle='--')
    ax2.tick_params(axis='x', rotation=45)
    ax2.set_ylim(7, 10)
    
    # Highlight problem months
    for month in problem_months:
        month_idx = df[df['Month'] == month].index[0]
        ax2.scatter(month_idx, df.loc[month_idx, 'Customer_Satisfaction'], 
                   color='red', s=200, zorder=5, marker='X')
    
    # Plot 3: Returns and Support Tickets
    ax3 = axes[1, 0]
    x = np.arange(len(months_short))
    width = 0.35
    
    bars1 = ax3.bar(x - width/2, df['Returns'], width, label='Returns', 
                    color='#F18F01', alpha=0.8)
    ax3_2 = ax3.twinx()
    bars2 = ax3_2.bar(x + width/2, df['Support_Tickets'], width, 
                      label='Support Tickets', color='#C73E1D', alpha=0.8)
    
    ax3.set_xlabel('Month', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Returns', fontsize=11, fontweight='bold', color='#F18F01')
    ax3_2.set_ylabel('Support Tickets', fontsize=11, fontweight='bold', color='#C73E1D')
    ax3.set_title('Returns vs Support Tickets', fontsize=12, fontweight='bold')
    ax3.set_xticks(x)
    ax3.set_xticklabels(months_short, rotation=45)
    ax3.tick_params(axis='y', labelcolor='#F18F01')
    ax3_2.tick_params(axis='y', labelcolor='#C73E1D')
    ax3.legend(loc='upper left')
    ax3_2.legend(loc='upper right')
    ax3.grid(True, alpha=0.3, linestyle='--')
    
    # Plot 4: Histogram of Revenue Distribution
    ax4 = axes[1, 1]
    n, bins, patches = ax4.hist(df['Revenue'], bins=8, color='#06A77D', 
                                edgecolor='black', alpha=0.7, linewidth=1.2)
    
    # Color gradient
    cm = plt.cm.RdYlGn
    bin_centers = 0.5 * (bins[:-1] + bins[1:])
    col = bin_centers - min(bin_centers)
    col /= max(col)
    
    for c, p in zip(col, patches):
        plt.setp(p, 'facecolor', cm(c))
    
    ax4.set_xlabel('Revenue ($)', fontsize=11, fontweight='bold')
    ax4.set_ylabel('Frequency (Number of Months)', fontsize=11, fontweight='bold')
    ax4.set_title('Revenue Distribution (Histogram)', fontsize=12, fontweight='bold')
    ax4.axvline(df['Revenue'].mean(), color='red', linestyle='--', 
                linewidth=2, label=f"Mean: ${df['Revenue'].mean():,.0f}")
    ax4.axvline(df['Revenue'].median(), color='orange', linestyle='--', 
                linewidth=2, label=f"Median: ${df['Revenue'].median():,.0f}")
    ax4.legend()
    ax4.grid(True, alpha=0.3, linestyle='--', axis='y')
    
    plt.tight_layout()
    print("✓ Visualizations created successfully!")
    print("\nClosing the plot window will complete the program...")
    plt.show()
    
    print("\n" + "=" * 70)
    print("✓ Root Cause Analysis Complete!")
    print("=" * 70)

if __name__ == "__main__":
    main()
