"""
Generate Table 4-2: Text-only Model Performance (Stages 1-4)
Format: Matching Table 4-1 format with all 5 metrics
"""

import pandas as pd
from pathlib import Path

# Paths
RESULTS_DIR = Path(__file__).parent.parent / 'results' / 'text_only_experiments'
OUTPUT_DIR = Path(__file__).parent.parent / 'tables'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Read complete metrics summary
summary_df = pd.read_csv(RESULTS_DIR / 'text_only_complete_metrics_summary.csv')

# Format for Table 4-2 (matching Table 4-1 format)
table_data = []

for _, row in summary_df.iterrows():
    stage = row['stage']
    
    # Format: Mean (CI_lower, CI_upper) - each on separate line
    roc_auc_line1 = f"{row['roc_auc_mean']:.4f} ({row['roc_auc_ci_lower']:.4f},"
    roc_auc_line2 = f"{row['roc_auc_ci_upper']:.4f})"
    
    pr_auc_line1 = f"{row['pr_auc_mean']:.4f} ({row['pr_auc_ci_lower']:.4f},"
    pr_auc_line2 = f"{row['pr_auc_ci_upper']:.4f})"
    
    h_measure_line1 = f"{row['h_measure_mean']:.4f} ({row['h_measure_ci_lower']:.4f},"
    h_measure_line2 = f"{row['h_measure_ci_upper']:.4f})"
    
    recall_line1 = f"{row['recall_mean']:.4f} ({row['recall_ci_lower']:.4f},"
    recall_line2 = f"{row['recall_ci_upper']:.4f})"
    
    f1_line1 = f"{row['f1_score_mean']:.4f} ({row['f1_score_ci_lower']:.4f},"
    f1_line2 = f"{row['f1_score_ci_upper']:.4f})"
    
    table_data.append({
        'Stage': stage,
        'ROC-AUC': f"{roc_auc_line1}\n{roc_auc_line2}",
        'PR-AUC': f"{pr_auc_line1}\n{pr_auc_line2}",
        'H-Measure': f"{h_measure_line1}\n{h_measure_line2}",
        'Recall': f"{recall_line1}\n{recall_line2}",
        'F1-Score': f"{f1_line1}\n{f1_line2}"
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
print("      Format matches Table 4-1 with all 5 metrics.")
