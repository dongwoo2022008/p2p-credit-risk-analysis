"""
Generate Table 2-3: Descriptive Statistics for Text Length (Number of Characters)
Korean P2P Lending Credit Risk Analysis
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Paths
DATA_PATH = Path(__file__).parent.parent / 'data' / 'sentiment_scoring.25.12.30.xlsx'
OUTPUT_PATH = Path(__file__).parent.parent / 'tables' / 'table_2_3_text_statistics.csv'

def generate_text_statistics():
    """Generate text length statistics table"""
    
    print("="*80)
    print("Table 2-3: Descriptive Statistics for Text Length")
    print("="*80)
    
    # Load data
    df = pd.read_excel(DATA_PATH)
    print(f"Total samples: {len(df):,}")
    
    # Calculate text lengths
    df['title_length'] = df['제목'].fillna('').astype(str).str.len()
    df['purpose_length'] = df['신청목적'].fillna('').astype(str).str.len()
    df['plan_length'] = df['상환계획'].fillna('').astype(str).str.len()
    df['total_length'] = df['title_length'] + df['purpose_length'] + df['plan_length']
    
    # Define fields
    fields = [
        ('Title', 'title_length'),
        ('Loan Purpose', 'purpose_length'),
        ('Repayment Plan', 'plan_length'),
        ('Total (Title + Purpose + Plan)', 'total_length')
    ]
    
    # Calculate statistics
    stats_list = []
    
    for field_name, col_name in fields:
        data = df[col_name]
        
        stats = {
            'Field': field_name,
            'Mean': round(data.mean(), 1),
            'Standard Deviation': round(data.std(), 1),
            'Median': round(data.median(), 1),
            'Q1': round(data.quantile(0.25), 1),
            'Q3': round(data.quantile(0.75), 1),
            'Min': int(data.min()),
            'Max': int(data.max())
        }
        
        stats_list.append(stats)
    
    # Create DataFrame
    stats_df = pd.DataFrame(stats_list)
    
    # Save to CSV
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    stats_df.to_csv(OUTPUT_PATH, index=False, encoding='utf-8-sig')
    
    print("\n" + "="*80)
    print("Text Length Statistics Summary")
    print("="*80)
    print(stats_df.to_string(index=False))
    
    print("\n" + "="*80)
    print("Additional Statistics")
    print("="*80)
    print(f"Average total text length: {df['total_length'].mean():.1f} characters")
    print(f"Median total text length: {df['total_length'].median():.1f} characters")
    print(f"Samples with no text: {(df['total_length'] == 0).sum():,}")
    print(f"Samples with text: {(df['total_length'] > 0).sum():,}")
    
    print("\n" + "="*80)
    print(f"Table saved to: {OUTPUT_PATH}")
    print("="*80)
    
    return stats_df

if __name__ == '__main__':
    stats_df = generate_text_statistics()
