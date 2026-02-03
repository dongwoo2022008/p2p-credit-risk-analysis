"""
Generate Table 2-1: Distribution of Repayment Outcomes (2-Class) and Binary Target Composition
Korean P2P Lending Credit Risk Analysis
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Paths
DATA_PATH = Path(__file__).parent.parent / 'data' / 'sentiment_scoring.25.12.30.xlsx'
OUTPUT_PATH = Path(__file__).parent.parent / 'tables' / 'table_2_1_repayment_distribution.csv'

def generate_repayment_distribution():
    """Generate repayment outcome distribution table"""
    
    print("="*80)
    print("Table 2-1: Distribution of Repayment Outcomes (2-Class)")
    print("="*80)
    
    # Load data
    df = pd.read_excel(DATA_PATH)
    print(f"Total samples: {len(df):,}")
    
    # Create binary target
    df['target'] = (df['상환결과'] == '채무불이행').astype(int)
    
    # Count distribution
    total = len(df)
    default_count = (df['target'] == 1).sum()
    repayment_count = (df['target'] == 0).sum()
    
    # Create table
    table_data = [
        {
            'Repayment Outcome': 'Default',
            'Number': default_count,
            'Ratio (%)': round(default_count / total * 100, 2),
            'y (target)': 1
        },
        {
            'Repayment Outcome': 'Repayment',
            'Number': repayment_count,
            'Ratio (%)': round(repayment_count / total * 100, 2),
            'y (target)': 0
        },
        {
            'Repayment Outcome': 'Total',
            'Number': total,
            'Ratio (%)': 100.00,
            'y (target)': ''
        }
    ]
    
    table_df = pd.DataFrame(table_data)
    
    # Save to CSV
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    table_df.to_csv(OUTPUT_PATH, index=False, encoding='utf-8-sig')
    
    print("\n" + "="*80)
    print("Table 2-1: Repayment Outcome Distribution")
    print("="*80)
    print(table_df.to_string(index=False))
    
    print("\n" + "="*80)
    print("Additional Statistics")
    print("="*80)
    print(f"Imbalance Ratio: {repayment_count / default_count:.2f}:1")
    print(f"Default Rate: {default_count / total * 100:.2f}%")
    print(f"Repayment Rate: {repayment_count / total * 100:.2f}%")
    
    print("\n" + "="*80)
    print(f"Table saved to: {OUTPUT_PATH}")
    print("="*80)
    
    return table_df

if __name__ == '__main__':
    table_df = generate_repayment_distribution()
