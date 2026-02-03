"""
Generate Table 4-2: Text-only Model Performance (Stages 1-4)
Format: Stage-wise Performance Summary with Mean and 95% CI
"""

import pandas as pd
from pathlib import Path

# Paths
RESULTS_DIR = Path(__file__).parent.parent / 'results' / 'text_only_experiments'
OUTPUT_DIR = Path(__file__).parent.parent / 'tables'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Read summary
summary_df = pd.read_csv(RESULTS_DIR / 'text_only_stages_summary.csv')

# Format for Table 4-2
table_data = []

for _, row in summary_df.iterrows():
    stage = row['stage']
    
    # Format: Mean (CI_lower, CI_upper)
    roc_auc = f"{row['roc_auc_mean']:.4f} ({row['roc_auc_ci_lower']:.4f}, {row['roc_auc_ci_upper']:.4f})"
    roc_auc_range = row['roc_auc_range']
    recall = f"{row['recall_mean']:.4f} ({row['recall_ci_lower']:.4f}, {row['recall_ci_upper']:.4f})"
    f1 = f"{row['f1_score_mean']:.4f} ({row['f1_score_ci_lower']:.4f}, {row['f1_score_ci_upper']:.4f})"
    
    table_data.append({
        'Stage': stage,
        'ROC-AUC (mean)': roc_auc,
        'ROC-AUC (range)': roc_auc_range,
        'Recall (mean)': recall,
        'F1-score (mean)': f1
    })

# Create table
table_df = pd.DataFrame(table_data)

# Save
output_path = OUTPUT_DIR / 'table_4_2_text_only_performance.csv'
table_df.to_csv(output_path, index=False)

print("="*80)
print("Table 4-2: Text-only Model Performance (Stages 1-4)")
print("="*80)
print(table_df.to_string(index=False))
print("="*80)
print(f"\n✓ Table saved to: {output_path}")
print("\nNote: Values are mean and 95% confidence interval from 50 iterations.")
print("      Text-only models show near-random performance (ROC-AUC ≈ 0.49-0.51),")
print("      demonstrating that structured variables are essential for prediction.")
