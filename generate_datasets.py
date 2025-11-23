"""
Dataset Generator for Lab Assignment
Creates synthetic datasets for all lab programs
"""

import pandas as pd
import numpy as np
from datetime import datetime
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

def generate_employees_dataset():
    """Generate employee dataset for Program 1"""
    print("Generating employees dataset...")
    
    departments = ['IT', 'HR', 'Finance', 'Marketing', 'Sales']
    first_names = ['John', 'Sarah', 'Michael', 'Emily', 'David', 'Jessica', 'Daniel', 
                   'Lisa', 'James', 'Maria', 'Robert', 'Jennifer', 'Christopher', 
                   'Amanda', 'Matthew', 'Ashley', 'Joshua', 'Stephanie', 'Andrew', 
                   'Elizabeth', 'Ryan', 'Michelle', 'Kevin', 'Laura', 'Brian']
    last_names = ['Smith', 'Johnson', 'Brown', 'Davis', 'Wilson', 'Martinez', 
                  'Anderson', 'Taylor', 'Thomas', 'Garcia', 'Rodriguez', 'Lee', 
                  'White', 'Harris', 'Clark', 'Lewis', 'Robinson', 'Walker', 
                  'Hall', 'Allen', 'Young', 'King', 'Wright', 'Lopez', 'Hill']
    
    n_employees = 250
    
    data = {
        'Employee_ID': [f'E{str(i+1).zfill(3)}' for i in range(n_employees)],
        'Name': [f'{random.choice(first_names)} {random.choice(last_names)}' for _ in range(n_employees)],
        'Department': [random.choice(departments) for _ in range(n_employees)],
        'Age': np.random.randint(24, 50, n_employees),
        'Salary': np.random.randint(50000, 100000, n_employees),
        'Experience_Years': np.random.randint(2, 23, n_employees)
    }
    
    df = pd.DataFrame(data)
    # Make salary correlate somewhat with experience
    df['Salary'] = df['Salary'] + (df['Experience_Years'] * 1000)
    df.to_csv('employees_data.csv', index=False)
    print(f"✓ Created employees_data.csv with {len(df)} records\n")
    return df

def generate_sales_dataset():
    """Generate sales dataset for Program 2"""
    print("Generating sales dataset...")
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    products = ['Laptop', 'Phone', 'Tablet']
    
    data = []
    for month in months:
        base_sales = np.random.randint(25000, 50000)
        for product in products:
            # Add some seasonal variation
            seasonal_factor = 1.0 + (months.index(month) / 12) * 0.5
            sales = int(base_sales * seasonal_factor * np.random.uniform(0.8, 1.2))
            profit = int(sales * 0.3)  # 30% profit margin
            marketing = int(sales * 0.1)  # 10% marketing spend
            customers = int(sales / (200 + np.random.randint(-50, 50)))
            
            data.append({
                'Month': month,
                'Product': product,
                'Sales': sales,
                'Profit': profit,
                'Marketing_Spend': marketing,
                'Customer_Count': customers
            })
    
    df = pd.DataFrame(data)
    df.to_csv('sales_data.csv', index=False)
    print(f"✓ Created sales_data.csv with {len(df)} records\n")
    return df

def generate_products_dataset():
    """Generate products dataset for Program 3"""
    print("Generating products dataset...")
    
    products_data = {
        'Product_Name': [
            'Gaming Laptop', 'Business Laptop', 'Smartphone Pro', 'Smartphone Lite',
            'Tablet Premium', 'Tablet Basic', 'Wireless Headphones', 'Bluetooth Speaker',
            'Smart Watch', 'Fitness Tracker', 'Laptop Bag', 'Phone Case',
            'Screen Protector', 'USB Cable', 'Power Bank', 'Wireless Mouse',
            'Keyboard', 'Webcam', 'External SSD', 'Monitor'
        ],
        'Price': [1299, 899, 799, 399, 599, 299, 199, 149, 
                  349, 129, 49, 25, 15, 12, 45, 35, 79, 89, 159, 299],
        'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics',
                     'Electronics', 'Electronics', 'Accessories', 'Accessories',
                     'Electronics', 'Electronics', 'Accessories', 'Accessories',
                     'Accessories', 'Accessories', 'Accessories', 'Accessories',
                     'Accessories', 'Accessories', 'Accessories', 'Electronics']
    }
    
    df = pd.DataFrame(products_data)
    # Generate sales count inversely proportional to price (cheaper items sell more)
    df['Sales_Count'] = (3000 / df['Price'] * np.random.uniform(0.8, 1.2, len(df))).astype(int)
    df.to_csv('products_data.csv', index=False)
    print(f"✓ Created products_data.csv with {len(df)} records\n")
    return df

def generate_monthly_performance_dataset():
    """Generate monthly performance dataset for Program 4"""
    print("Generating monthly performance dataset...")
    
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    
    # Create realistic performance data with intentional drops in Sep-Oct
    base_revenue = 150000
    data = []
    
    for i, month in enumerate(months):
        # Create normal growth with drops in Sep-Oct
        if month in ['September', 'October']:
            revenue_factor = 0.85 + np.random.uniform(-0.05, 0.05)
            satisfaction = 7.5 + np.random.uniform(0, 0.3)
            returns = 55 + np.random.randint(0, 15)
            tickets = 145 + np.random.randint(0, 30)
        else:
            revenue_factor = 1.0 + (i / 12) * 0.3 + np.random.uniform(-0.05, 0.05)
            satisfaction = 8.2 + np.random.uniform(0, 1.0)
            returns = 20 + np.random.randint(0, 30)
            tickets = 65 + np.random.randint(0, 60)
        
        revenue = int(base_revenue * revenue_factor)
        marketing = int(revenue * 0.12)
        
        data.append({
            'Month': month,
            'Revenue': revenue,
            'Customer_Satisfaction': round(satisfaction, 1),
            'Marketing_Budget': marketing,
            'Returns': returns,
            'Support_Tickets': tickets
        })
    
    df = pd.DataFrame(data)
    df.to_csv('monthly_performance.csv', index=False)
    print(f"✓ Created monthly_performance.csv with {len(df)} records\n")
    return df

def main():
    """Generate all datasets"""
    print("=" * 60)
    print("SYNTHETIC DATASET GENERATOR FOR LAB ASSIGNMENT")
    print("=" * 60)
    print()
    
    generate_employees_dataset()
    generate_sales_dataset()
    generate_products_dataset()
    generate_monthly_performance_dataset()
    
    print("=" * 60)
    print("✓ All datasets generated successfully!")
    print("=" * 60)
    print("\nGenerated files:")
    print("  1. employees_data.csv")
    print("  2. sales_data.csv")
    print("  3. products_data.csv")
    print("  4. monthly_performance.csv")
    print()

if __name__ == "__main__":
    main()
