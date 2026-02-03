"""
Generate Table 4-1: Model Performance Comparison with 95% Confidence Intervals
Korean P2P Lending Credit Risk Analysis

Format: Mean (CI Lower, CI Upper)
Based on 50-iteration experiments with Remove_Weak_14 variable set
"""

import pandas as pd
import numpy as np
from pathlib import Path
from scipy import stats

# Paths
RAW_RESULTS_PATH = '/home/ubuntu/credit-risk-reproducibility/results/tables/variable_combination_50iterations_17vars.csv'
OUTPUT_PATH = Path(__file__).parent.parent / 'tables' / 'table_4_1_model_performance.csv'

def calculate_ci(values, confidence=0.95):
    """
    Calculate mean and 95% confidence interval
    
    Args:
        values: array of values from multiple iterations
        confidence: confidence level (default 0.95)
    
    Returns:
        mean, ci_lower, ci_upper
    """
    n = len(values)
    mean = np.mean(values)
    se = stats.sem(values)  # Standard error
    ci_margin = se * stats.t.ppf((1 + confidence) / 2, n - 1)
    
    return mean, mean - ci_margin, mean + ci_margin

def generate_model_performance_table_with_ci():
    """
    Generate model performance comparison table with 95% CI
    """
    
    print("="*80)
    print("Table 4-1: Model Performance Comparison with 95% Confidence Intervals")
    print("="*80)
    
    # Load raw 50-iteration results
    print("\nLoading 50-iteration experiment results...")
    df = pd.read_csv(RAW_RESULTS_PATH)
    
    # Filter for Remove_Weak_14 variable set
    df_14vars = df[df['Variable_Set'] == 'Remove_Weak_14'].copy()
    
    print(f"Total experiments: {len(df_14vars)}")
    print(f"Models: {df_14vars['Model'].unique()}")
    print(f"Seeds: {df_14vars['Seed'].nunique()}")
    
    # Model name mapping
    model_names = {
        'LR': 'Logistic Regression (LR)',
        'NB': 'Naive Bayes (NB)',
        'SVM': 'Support Vector Machine (SVM)',
        'DT': 'Decision Tree (DT)',
        'RF': 'Random Forest (RF)',
        'GB': 'Gradient Boosting (GB)',
        'XGB': 'XGBoost (XGB)',
        'MLP': 'Multi-Layer Perceptron (MLP)',
        'KNN': 'K-Nearest Neighbors (KNN)'
    }
    
    # Metrics to calculate
    metrics = ['ROC_AUC', 'PR_AUC', 'H_Measure', 'Recall', 'F1_Score']
    
    # Calculate mean and CI for each model
    results = []
    
    for model in df_14vars['Model'].unique():
        model_data = df_14vars[df_14vars['Model'] == model]
        
        row = {'Model': model_names.get(model, model)}
        
        for metric in metrics:
            values = model_data[metric].values
            mean, ci_lower, ci_upper = calculate_ci(values)
            
            # Format: Mean (CI Lower, CI Upper)
            metric_name = metric.replace('_', '-')
            
            row[metric_name] = f"{mean:.4f} ({ci_lower:.4f}, {ci_upper:.4f})"
            row[f'{metric_name}_mean'] = mean  # For sorting
        
        results.append(row)
    
    # Create DataFrame
    performance_df = pd.DataFrame(results)
    
    # Sort by ROC-AUC mean (descending)
    performance_df = performance_df.sort_values('ROC-AUC_mean', ascending=False)
    
    # Drop mean columns (used only for sorting)
    mean_cols = [col for col in performance_df.columns if col.endswith('_mean')]
    performance_df_display = performance_df.drop(columns=mean_cols)
    
    # Save to CSV
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    performance_df_display.to_csv(OUTPUT_PATH, index=False, encoding='utf-8-sig')
    
    print("\n" + "="*80)
    print("Model Performance Summary (Mean and 95% CI)")
    print("="*80)
    print(performance_df_display.to_string(index=False))
    
    print("\n" + "="*80)
    print("Key Findings")
    print("="*80)
    best_model = performance_df.iloc[0]['Model']
    print(f"Best Model (ROC-AUC): {best_model}")
    print(f"  ROC-AUC: {performance_df.iloc[0]['ROC-AUC']}")
    print(f"  PR-AUC: {performance_df.iloc[0]['PR-AUC']}")
    
    print("\n" + "="*80)
    print("Experimental Setup")
    print("="*80)
    print("Variables: 14 selected variables (Remove_Weak_14)")
    print("Iterations: 50 random seeds")
    print("Evaluation: Mean and 95% confidence interval")
    print("CI Method: t-distribution (n=50)")
    print("Metrics: ROC-AUC (primary), PR-AUC, H-Measure, Recall, F1-Score")
    print("Data: 6,057 samples (55.34% default, 44.66% repayment)")
    
    print("\n" + "="*80)
    print("Table Format")
    print("="*80)
    print("Format: Mean (CI Lower, CI Upper)")
    print("Example: 0.8198 (0.8175, 0.8221)")
    print("Note: Values are mean and 95% confidence interval from 50 iterations")
    
    print("\n" + "="*80)
    print(f"Table saved to: {OUTPUT_PATH}")
    print("="*80)
    
    return performance_df_display

if __name__ == '__main__':
    performance_df = generate_model_performance_table_with_ci()
