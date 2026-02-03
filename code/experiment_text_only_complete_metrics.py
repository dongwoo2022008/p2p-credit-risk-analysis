"""
Text-only Model Experiments with Complete Metrics (5 metrics)
Korean P2P Lending Credit Risk Analysis

Model: Logistic Regression
Evaluation: ROC-AUC, PR-AUC, H-Measure, Recall, F1-Score with 95% CI
Iterations: 50 random seeds
"""

import pickle
import pandas as pd
import numpy as np
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, recall_score, f1_score, average_precision_score
from sklearn.model_selection import train_test_split
from scipy.stats import sem, t

# Paths
PKL_DIR = Path('/home/ubuntu/upload')
OUTPUT_DIR = Path(__file__).parent.parent / 'results' / 'text_only_experiments'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# PKL files mapping
PKL_FILES = {
    'Stage 1 (TF-IDF)': PKL_DIR / 'preprocessed_text_only_binary.pkl',
    'Stage 2 (Subword)': PKL_DIR / 'preprocessed_text_subword_binary.pkl',
    'Stage 3 (MiniLM)': PKL_DIR / 'preprocessed_text_minilm_binary.pkl',
    'Stage 4 (KoSimCSE)': PKL_DIR / 'preprocessed_text_kosimcse_binary.pkl',
}

# Experiment settings
RANDOM_SEEDS = list(range(1, 51))  # 50 iterations
TEST_SIZE = 0.2

print("="*80)
print("Text-only Model Experiments: Complete Metrics (5 metrics)")
print("="*80)
print(f"PKL files directory: {PKL_DIR}")
print(f"Iterations: {len(RANDOM_SEEDS)}")
print(f"Metrics: ROC-AUC, PR-AUC, H-Measure, Recall, F1-Score")
print(f"Output: {OUTPUT_DIR}")
print("="*80)

def calculate_h_measure(y_true, y_pred_proba, c=0.5):
    """
    Calculate H-Measure
    c: cost ratio (default 0.5 for balanced cost)
    """
    from sklearn.metrics import roc_curve
    
    # Get ROC curve
    fpr, tpr, thresholds = roc_curve(y_true, y_pred_proba)
    
    # Calculate H-measure
    # Simplified version: H = 1 - sqrt((FPR^2 + (1-TPR)^2) / 2)
    # More accurate: weighted by cost
    
    # Find optimal threshold based on cost
    costs = c * fpr + (1 - c) * (1 - tpr)
    optimal_idx = np.argmin(costs)
    
    # H-measure at optimal threshold
    h_measure = 1 - costs[optimal_idx]
    
    return h_measure

def calculate_ci(values, confidence=0.95):
    """Calculate mean and 95% CI"""
    n = len(values)
    mean_val = np.mean(values)
    se_val = sem(values)
    ci_margin = se_val * t.ppf((1 + confidence) / 2, n - 1)
    return mean_val, mean_val - ci_margin, mean_val + ci_margin

def run_experiments(stage_name, pkl_path, seeds):
    """Run experiments for a stage with all 5 metrics"""
    print(f"\n{'='*80}")
    print(f"{stage_name}")
    print(f"{'='*80}")
    
    # Load data
    print(f"Loading: {pkl_path.name}")
    with open(pkl_path, 'rb') as f:
        data = pickle.load(f)
    
    print(f"  Description: {data.get('description', 'N/A')}")
    
    # Get full dataset
    X_full = np.vstack([data['X_train'], data['X_test']])
    y_full = pd.concat([data['y_train'], data['y_test']]).values
    
    print(f"  Full dataset shape: {X_full.shape}")
    print(f"  Running {len(seeds)} iterations...")
    
    results = []
    
    for i, seed in enumerate(seeds, 1):
        # Split
        X_train, X_test, y_train, y_test = train_test_split(
            X_full, y_full, test_size=TEST_SIZE, random_state=seed, stratify=y_full
        )
        
        # Train
        model = LogisticRegression(max_iter=1000, random_state=seed, class_weight='balanced')
        model.fit(X_train, y_train)
        
        # Predict
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        y_pred = model.predict(X_test)
        
        # Evaluate - 5 metrics
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        pr_auc = average_precision_score(y_test, y_pred_proba)
        h_measure = calculate_h_measure(y_test, y_pred_proba)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        
        results.append({
            'seed': seed,
            'roc_auc': roc_auc,
            'pr_auc': pr_auc,
            'h_measure': h_measure,
            'recall': recall,
            'f1_score': f1
        })
        
        if i % 10 == 0:
            print(f"    Completed {i}/{len(seeds)}...")
    
    # Calculate statistics
    results_df = pd.DataFrame(results)
    
    output = {'stage': stage_name}
    
    for metric in ['roc_auc', 'pr_auc', 'h_measure', 'recall', 'f1_score']:
        values = results_df[metric].values
        mean_val, ci_lower, ci_upper = calculate_ci(values)
        output[f'{metric}_mean'] = mean_val
        output[f'{metric}_ci_lower'] = ci_lower
        output[f'{metric}_ci_upper'] = ci_upper
    
    print(f"\n  Results:")
    print(f"    ROC-AUC:   {output['roc_auc_mean']:.4f} ({output['roc_auc_ci_lower']:.4f}, {output['roc_auc_ci_upper']:.4f})")
    print(f"    PR-AUC:    {output['pr_auc_mean']:.4f} ({output['pr_auc_ci_lower']:.4f}, {output['pr_auc_ci_upper']:.4f})")
    print(f"    H-Measure: {output['h_measure_mean']:.4f} ({output['h_measure_ci_lower']:.4f}, {output['h_measure_ci_upper']:.4f})")
    print(f"    Recall:    {output['recall_mean']:.4f} ({output['recall_ci_lower']:.4f}, {output['recall_ci_upper']:.4f})")
    print(f"    F1:        {output['f1_score_mean']:.4f} ({output['f1_score_ci_lower']:.4f}, {output['f1_score_ci_upper']:.4f})")
    
    return output, results_df

# Run all stages
all_results = []
all_details = {}

for stage_name, pkl_path in PKL_FILES.items():
    if not pkl_path.exists():
        print(f"\n⚠️  {stage_name} skipped: file not found")
        continue
    
    try:
        output, details = run_experiments(stage_name, pkl_path, RANDOM_SEEDS)
        all_results.append(output)
        all_details[stage_name] = details
        
        # Save individual results
        stage_num = stage_name.split()[1]
        stage_method = stage_name.split('(')[1].rstrip(')').lower().replace(' ', '_')
        details.to_csv(OUTPUT_DIR / f'stage{stage_num}_{stage_method}_complete_results.csv', index=False)
        
    except Exception as e:
        print(f"\n❌ Error in {stage_name}: {e}")
        import traceback
        traceback.print_exc()

# Summary
print("\n" + "="*80)
print("SUMMARY: Complete Metrics")
print("="*80)

if all_results:
    summary_df = pd.DataFrame(all_results)
    summary_df.to_csv(OUTPUT_DIR / 'text_only_complete_metrics_summary.csv', index=False)
    
    print(f"\n{'Stage':<25} {'ROC-AUC':<15} {'PR-AUC':<15} {'H-Measure':<15} {'Recall':<15} {'F1':<15}")
    print("-"*100)
    
    for _, row in summary_df.iterrows():
        print(f"{row['stage']:<25} {row['roc_auc_mean']:.4f:<15} {row['pr_auc_mean']:.4f:<15} {row['h_measure_mean']:.4f:<15} {row['recall_mean']:.4f:<15} {row['f1_score_mean']:.4f:<15}")
    
    print(f"\n✓ Results saved to: {OUTPUT_DIR}")
else:
    print("\n❌ No experiments completed")
