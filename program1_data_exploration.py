"""
Lab Program 1: Basic Data Exploration using Pandas
Demonstrates: Dataset creation, display, summary statistics, and column listing
"""

import pandas as pd
import numpy as np

def main():
    print("=" * 70)
    print("LAB PROGRAM 1: BASIC DATA EXPLORATION")
    print("=" * 70)
    print()
    
    # Load the employee dataset
    print("Loading employee dataset...")
    df = pd.read_csv('employees_data.csv')
    print("Dataset loaded successfully!\n")
    
    # 1. Display the dataset in tabular format
    print("-" * 70)
    print("1. COMPLETE DATASET (Tabular Format)")
    print("-" * 70)
    print(df.to_string(index=False))
    print()
    
    # 2. Summary statistics
    print("-" * 70)
    print("2. SUMMARY STATISTICS")
    print("-" * 70)
    print(df.describe())
    print()
    
    # Additional descriptive statistics
    print("-" * 70)
    print("3. ADDITIONAL DATASET INFORMATION")
    print("-" * 70)
    print(f"Total number of records: {len(df)}")
    print(f"Total number of columns: {len(df.columns)}")
    print(f"\nData types:")
    print(df.dtypes)
    print()
    
    # Department-wise statistics
    print("-" * 70)
    print("4. DEPARTMENT-WISE ANALYSIS")
    print("-" * 70)
    dept_stats = df.groupby('Department').agg({
        'Salary': ['mean', 'min', 'max'],
        'Age': 'mean',
        'Experience_Years': 'mean',
        'Employee_ID': 'count'
    }).round(2)
    dept_stats.columns = ['Avg Salary', 'Min Salary', 'Max Salary', 'Avg Age', 
                          'Avg Experience', 'Employee Count']
    print(dept_stats)
    print()
    
    # 3. List all column names
    print("-" * 70)
    print("5. COLUMN NAMES")
    print("-" * 70)
    print(f"Total Columns: {len(df.columns)}\n")
    for i, col in enumerate(df.columns, 1):
        print(f"{i}. {col}")
    print()
    
    # Additional insights
    print("-" * 70)
    print("6. KEY INSIGHTS")
    print("-" * 70)
    print(f"• Average Salary: ${df['Salary'].mean():,.2f}")
    print(f"• Average Age: {df['Age'].mean():.1f} years")
    print(f"• Average Experience: {df['Experience_Years'].mean():.1f} years")
    print(f"• Highest Salary: ${df['Salary'].max():,}")
    print(f"• Lowest Salary: ${df['Salary'].min():,}")
    print(f"• Most common department: {df['Department'].mode()[0]}")
    print()
    
    print("=" * 70)
    print("✓ Data Exploration Complete!")
    print("=" * 70)

if __name__ == "__main__":
    main()
