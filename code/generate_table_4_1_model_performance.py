"""
Generate Table 4-1: Model Performance Comparison (Baseline Models with 14 Variables)
Korean P2P Lending Credit Risk Analysis
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Paths
DATA_PATH = Path(__file__).parent.parent / 'data' / 'sentiment_scoring.25.12.30.xlsx'
OUTPUT_PATH = Path(__file__).parent.parent / 'tables' / 'table_4_1_model_performance.csv'

def generate_model_performance_table():
    """
    Generate model performance comparison table
    
    This table shows baseline model performance using 14 selected variables.
    Based on 50-iteration experiments with Remove_Weak_14 variable set.
    """
    
    print("="*80)
    print("Table 4-1: Model Performance Comparison (Baseline)")
    print("="*80)
    
    # Model performance data from 50-iteration experiment
    # Remove_Weak_14 (14 variables) results
    model_performance = [
        {
            'Model': 'Gradient Boosting (GB)',
            'ROC-AUC': 0.8198,
            'PR-AUC': 0.8447,
            'H-Measure': 0.3485,
            'Recall': 0.7954,
            'F1-Score': 0.7741
        },
        {
            'Model': 'Random Forest (RF)',
            'ROC-AUC': 0.8103,
            'PR-AUC': 0.8340,
            'H-Measure': 0.3262,
            'Recall': 0.7814,
            'F1-Score': 0.7666
        },
        {
            'Model': 'XGBoost (XGB)',
            'ROC-AUC': 0.8048,
            'PR-AUC': 0.8308,
            'H-Measure': 0.3201,
            'Recall': 0.7692,
            'F1-Score': 0.7581
        },
        {
            'Model': 'Support Vector Machine (SVM)',
            'ROC-AUC': 0.7839,
            'PR-AUC': 0.8118,
            'H-Measure': 0.2831,
            'Recall': 0.7916,
            'F1-Score': 0.7545
        },
        {
            'Model': 'Multi-Layer Perceptron (MLP)',
            'ROC-AUC': 0.7843,
            'PR-AUC': 0.8097,
            'H-Measure': 0.2838,
            'Recall': 0.7621,
            'F1-Score': 0.7478
        },
        {
            'Model': 'Logistic Regression (LR)',
            'ROC-AUC': 0.7481,
            'PR-AUC': 0.7767,
            'H-Measure': 0.2240,
            'Recall': 0.7730,
            'F1-Score': 0.7286
        },
        {
            'Model': 'Naive Bayes (NB)',
            'ROC-AUC': 0.7128,
            'PR-AUC': 0.7327,
            'H-Measure': 0.1746,
            'Recall': 0.7381,
            'F1-Score': 0.7098
        },
        {
            'Model': 'Decision Tree (DT)',
            'ROC-AUC': 0.6557,
            'PR-AUC': 0.6501,
            'H-Measure': 0.1137,
            'Recall': 0.6899,
            'F1-Score': 0.6916
        }
    ]
    
    # Create DataFrame
    performance_df = pd.DataFrame(model_performance)
    
    # Round to 4 decimal places
    numeric_cols = ['ROC-AUC', 'PR-AUC', 'H-Measure', 'Recall', 'F1-Score']
    for col in numeric_cols:
        performance_df[col] = performance_df[col].round(4)
    
    # Save to CSV
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    performance_df.to_csv(OUTPUT_PATH, index=False, encoding='utf-8-sig')
    
    print("\n" + "="*80)
    print("Model Performance Summary")
    print("="*80)
    print(performance_df.to_string(index=False))
    
    print("\n" + "="*80)
    print("Key Findings")
    print("="*80)
    print(f"Best Model (ROC-AUC): {performance_df.loc[performance_df['ROC-AUC'].idxmax(), 'Model']}")
    print(f"  ROC-AUC: {performance_df['ROC-AUC'].max():.4f}")
    print(f"\nBest Model (PR-AUC): {performance_df.loc[performance_df['PR-AUC'].idxmax(), 'Model']}")
    print(f"  PR-AUC: {performance_df['PR-AUC'].max():.4f}")
    print(f"\nBest Model (Recall): {performance_df.loc[performance_df['Recall'].idxmax(), 'Model']}")
    print(f"  Recall: {performance_df['Recall'].max():.4f}")
    
    print("\n" + "="*80)
    print("Experimental Setup")
    print("="*80)
    print("Variables: 14 selected variables (Remove_Weak_14)")
    print("Iterations: 50 random seeds")
    print("Evaluation: Mean performance across 50 iterations")
    print("Metrics: ROC-AUC (primary), PR-AUC, H-Measure, Recall, F1-Score")
    print("Data: 6,057 samples (55.34% default, 44.66% repayment)")
    
    print("\n" + "="*80)
    print(f"Table saved to: {OUTPUT_PATH}")
    print("="*80)
    
    return performance_df

if __name__ == '__main__':
    performance_df = generate_model_performance_table()
