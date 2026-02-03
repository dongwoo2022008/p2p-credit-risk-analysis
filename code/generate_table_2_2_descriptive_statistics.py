"""
Generate Table 2-2: Descriptive Statistics for 14 Selected Variables
Korean P2P Lending Credit Risk Analysis
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Paths
DATA_PATH = Path(__file__).parent.parent / 'data' / 'sentiment_scoring.25.12.30.xlsx'
OUTPUT_PATH = Path(__file__).parent.parent / 'tables' / 'table_2_2_descriptive_statistics.csv'

def generate_descriptive_statistics():
    """Generate descriptive statistics table for 14 selected variables"""
    
    print("="*80)
    print("Table 2-2: Descriptive Statistics for 14 Variables")
    print("="*80)
    
    # Load data
    df = pd.read_excel(DATA_PATH)
    print(f"Total samples: {len(df):,}")
    
    # Define 14 selected variables (Remove_Weak_14)
    variables = [
        ('Loan Period', '대출시기'),
        ('Cancel Count', '취소횟수'),
        ('Fail Count', '실패횟수'),
        ('Success Count', '성공횟수'),
        ('Total Count', '총횟수'),
        ('Success Rate', '성공률'),
        ('Region', '지역(수도권0)'),
        ('Age', '나이'),
        ('Credit Score', '신용평점'),
        ('Monthly Income', '월소득(만원)'),
        ('Loan Amount', '신청금액(만원)'),
        ('Loan Interest Rate', '신청금리'),
        ('Monthly DTI', '월DTI'),
        ('Number of Investors', '투자인원')
    ]
    
    # Calculate statistics
    stats_list = []
    
    for eng_name, kor_name in variables:
        data = df[kor_name].dropna()
        
        stats = {
            'Variable': eng_name,
            'Mean': round(data.mean(), 2),
            'Standard Deviation': round(data.std(), 2),
            'Median': round(data.median(), 1),
            'Q1': round(data.quantile(0.25), 1),
            'Q3': round(data.quantile(0.75), 1),
            'Min': round(data.min(), 1),
            'Max': round(data.max(), 1)
        }
        
        stats_list.append(stats)
    
    # Create DataFrame
    stats_df = pd.DataFrame(stats_list)
    
    # Save to CSV
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    stats_df.to_csv(OUTPUT_PATH, index=False, encoding='utf-8-sig')
    
    print("\n" + "="*80)
    print("Descriptive Statistics Summary")
    print("="*80)
    print(stats_df.to_string(index=False))
    
    print("\n" + "="*80)
    print(f"Table saved to: {OUTPUT_PATH}")
    print("="*80)
    
    return stats_df

if __name__ == '__main__':
    stats_df = generate_descriptive_statistics()
