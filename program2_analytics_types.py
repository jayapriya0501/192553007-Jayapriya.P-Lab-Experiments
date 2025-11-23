"""
Lab Program 2: Four Types of Data Analytics
Demonstrates: Descriptive, Diagnostic, Predictive, and Prescriptive Analytics
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

def main():
    print("=" * 70)
    print("LAB PROGRAM 2: FOUR TYPES OF DATA ANALYTICS")
    print("=" * 70)
    print()
    
    # Load the sales dataset
    print("Loading sales dataset...")
    df = pd.read_csv('sales_data.csv')
    print("Dataset loaded successfully!\n")
    
    # Display sample data
    print("-" * 70)
    print("SAMPLE DATA (First 10 rows)")
    print("-" * 70)
    print(df.head(10).to_string(index=False))
    print()
    
    # =================================================================
    # 1. DESCRIPTIVE ANALYTICS - What happened?
    # =================================================================
    print("=" * 70)
    print("1. DESCRIPTIVE ANALYTICS - What Happened?")
    print("=" * 70)
    
    total_sales = df['Sales'].sum()
    avg_sales = df['Sales'].mean()
    total_profit = df['Profit'].sum()
    avg_profit = df['Profit'].mean()
    
    print(f"• Total Sales: ${total_sales:,}")
    print(f"• Average Sales: ${avg_sales:,.2f}")
    print(f"• Total Profit: ${total_profit:,}")
    print(f"• Average Profit: ${avg_profit:,.2f}")
    print()
    
    # Product-wise performance
    print("Product-wise Performance:")
    product_summary = df.groupby('Product').agg({
        'Sales': ['sum', 'mean'],
        'Profit': 'sum',
        'Customer_Count': 'sum'
    }).round(2)
    product_summary.columns = ['Total Sales', 'Avg Sales', 'Total Profit', 'Total Customers']
    print(product_summary)
    print()
    
    # Monthly trends
    print("Monthly Sales Trend:")
    monthly_summary = df.groupby('Month')['Sales'].sum()
    print(monthly_summary)
    print()
    
    # =================================================================
    # 2. DIAGNOSTIC ANALYTICS - Why did it happen?
    # =================================================================
    print("=" * 70)
    print("2. DIAGNOSTIC ANALYTICS - Why Did It Happen?")
    print("=" * 70)
    
    # Correlation analysis
    print("Correlation Analysis:")
    correlation_cols = ['Sales', 'Profit', 'Marketing_Spend', 'Customer_Count']
    correlation_matrix = df[correlation_cols].corr()
    print(correlation_matrix.round(3))
    print()
    
    # Key correlations
    sales_profit_corr = df['Sales'].corr(df['Profit'])
    sales_marketing_corr = df['Sales'].corr(df['Marketing_Spend'])
    sales_customers_corr = df['Sales'].corr(df['Customer_Count'])
    
    print("Key Correlation Findings:")
    print(f"• Sales vs Profit correlation: {sales_profit_corr:.3f}")
    print(f"  → {'Strong positive' if sales_profit_corr > 0.7 else 'Moderate'} relationship")
    print(f"• Sales vs Marketing Spend correlation: {sales_marketing_corr:.3f}")
    print(f"  → Marketing spend {'significantly' if sales_marketing_corr > 0.7 else 'moderately'} impacts sales")
    print(f"• Sales vs Customer Count correlation: {sales_customers_corr:.3f}")
    print(f"  → More customers {'strongly' if sales_customers_corr > 0.7 else 'somewhat'} correlate with higher sales")
    print()
    
    # =================================================================
    # 3. PREDICTIVE ANALYTICS - What will happen?
    # =================================================================
    print("=" * 70)
    print("3. PREDICTIVE ANALYTICS - What Will Happen?")
    print("=" * 70)
    
    # Prepare data for prediction (aggregate by month)
    monthly_data = df.groupby('Month').agg({
        'Sales': 'sum',
        'Marketing_Spend': 'sum',
        'Customer_Count': 'sum'
    }).reset_index()
    
    # Create month number for time series
    monthly_data['Month_Num'] = range(1, len(monthly_data) + 1)
    
    # Train linear regression model
    X = monthly_data[['Month_Num', 'Marketing_Spend', 'Customer_Count']]
    y = monthly_data['Sales']
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Current model performance
    train_score = model.score(X, y)
    print(f"Model R² Score: {train_score:.3f}")
    print(f"Model Accuracy: {train_score * 100:.1f}%")
    print()
    
    # Predict next 3 months
    print("Sales Forecast for Next 3 Months:")
    next_months = ['January (Next)', 'February (Next)', 'March (Next)']
    
    for i, future_month in enumerate(next_months, 1):
        month_num = len(monthly_data) + i
        # Estimate future marketing spend and customers based on trend
        avg_marketing = monthly_data['Marketing_Spend'].mean()
        avg_customers = monthly_data['Customer_Count'].mean()
        growth_factor = 1.05  # 5% growth assumption
        
        future_marketing = avg_marketing * growth_factor
        future_customers = avg_customers * growth_factor
        
        future_X = np.array([[month_num, future_marketing, future_customers]])
        predicted_sales = model.predict(future_X)[0]
        
        print(f"• {future_month}: ${predicted_sales:,.0f}")
    
    print()
    
    # =================================================================
    # 4. PRESCRIPTIVE ANALYTICS - What should we do?
    # =================================================================
    print("=" * 70)
    print("4. PRESCRIPTIVE ANALYTICS - What Should We Do?")
    print("=" * 70)
    
    print("Business Recommendations Based on Analysis:\n")
    
    # Recommendation 1: Best performing product
    best_product = df.groupby('Product')['Profit'].sum().idxmax()
    best_product_profit = df.groupby('Product')['Profit'].sum().max()
    print(f"1. FOCUS ON TOP PERFORMER")
    print(f"   • {best_product} generates highest profit (${best_product_profit:,})")
    print(f"   • ACTION: Increase inventory and marketing for {best_product}")
    print()
    
    # Recommendation 2: Marketing optimization
    roi = (df['Sales'].sum() / df['Marketing_Spend'].sum() - 1) * 100
    print(f"2. MARKETING OPTIMIZATION")
    print(f"   • Current Marketing ROI: {roi:.1f}%")
    if roi > 100:
        print(f"   • ACTION: Marketing is performing well, maintain current strategy")
    else:
        print(f"   • ACTION: Optimize marketing channels for better ROI")
    print()
    
    # Recommendation 3: Seasonal strategy
    best_month = df.groupby('Month')['Sales'].sum().idxmax()
    worst_month = df.groupby('Month')['Sales'].sum().idxmin()
    print(f"3. SEASONAL STRATEGY")
    print(f"   • Best performing month: {best_month}")
    print(f"   • Weakest month: {worst_month}")
    print(f"   • ACTION: Plan promotions and stock accordingly")
    print()
    
    # Recommendation 4: Customer acquisition
    avg_sale_per_customer = df['Sales'].sum() / df['Customer_Count'].sum()
    print(f"4. CUSTOMER ACQUISITION")
    print(f"   • Average revenue per customer: ${avg_sale_per_customer:.2f}")
    print(f"   • ACTION: Invest in customer acquisition if cost < ${avg_sale_per_customer * 0.3:.2f}")
    print(f"   • ACTION: Implement loyalty programs to increase repeat purchases")
    print()
    
    # Recommendation 5: Growth strategy
    print(f"5. GROWTH STRATEGY")
    print(f"   • Predicted sales show upward trend")
    print(f"   • ACTION: Scale operations to meet forecasted demand")
    print(f"   • ACTION: Hire additional staff for peak months")
    print()
    
    print("=" * 70)
    print("✓ Analytics Complete!")
    print("=" * 70)

if __name__ == "__main__":
    main()
