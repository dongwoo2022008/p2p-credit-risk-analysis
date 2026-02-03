# P2P Credit Risk Analysis - Repository Summary

## 📊 Overview

This repository contains all materials for reproducing Korean P2P lending credit risk analysis research. All tables, code, and data are organized for maximum reproducibility.

**Repository**: `p2p-credit-risk-analysis`  
**Created**: 2025-02-03  
**Purpose**: Research reproducibility for academic paper

---

## ✅ Completed Tables

### Table 2-1: Distribution of Repayment Outcomes (2-Class)

**File**: `tables/table_2_1_repayment_distribution.csv`  
**Script**: `code/generate_table_2_1_repayment_distribution.py`

| Repayment Outcome | Number | Ratio (%) | y (target) |
|-------------------|--------|-----------|------------|
| Default | 3,352 | 55.34 | 1 |
| Repayment | 2,705 | 44.66 | 0 |
| **Total** | **6,057** | **100.00** | - |

**Key Statistics**:
- Imbalance Ratio: 0.81:1 (Balanced dataset)
- Default Rate: 55.34%
- Repayment Rate: 44.66%

---

### Table 2-2: Descriptive Statistics for 14 Variables

**File**: `tables/table_2_2_descriptive_statistics.csv`  
**Script**: `code/generate_table_2_2_descriptive_statistics.py`

**14 Selected Variables** (Remove_Weak_14):
1. Loan Period (대출시기)
2. Cancel Count (취소횟수)
3. Fail Count (실패횟수)
4. Success Count (성공횟수)
5. Total Count (총횟수)
6. Success Rate (성공률)
7. Region (지역: 수도권=0, 비수도권=1)
8. Age (나이)
9. Credit Score (신용평점)
10. Monthly Income (월소득, 만원)
11. Loan Amount (신청금액, 만원)
12. Loan Interest Rate (신청금리)
13. Monthly DTI (월DTI)
14. Number of Investors (투자인원)

**Removed Variables** (from original 17):
- Gender (성별) - Low feature importance
- Loan Term (신청기간) - Weak predictive power
- Months of Service (서비스이용개월수) - Not in final selection

---

### Table 2-3: Descriptive Statistics for Text Length

**File**: `tables/table_2_3_text_statistics.csv`  
**Script**: `code/generate_table_2_3_text_statistics.py`

| Field | Mean | Std Dev | Median | Q1 | Q3 | Min | Max |
|-------|------|---------|--------|----|----|-----|-----|
| Title | 15.7 | 7.4 | 14.0 | 10.0 | 20.0 | 0 | 76 |
| Loan Purpose | 213.3 | 217.4 | 152.0 | 75.0 | 272.0 | 0 | 2433 |
| Repayment Plan | 225.6 | 218.1 | 175.0 | 83.0 | 302.0 | 0 | 3357 |
| **Total** | **454.5** | **350.9** | **370.0** | **221.0** | **585.0** | **7** | **3946** |

**Key Statistics**:
- Average total text length: 454.5 characters
- All samples contain text (6,057/6,057)

---

### Table 4-1: Model Performance Comparison (Baseline)

**File**: `tables/table_4_1_model_performance.csv`  
**Script**: `code/generate_table_4_1_model_performance.py`

| Model | ROC-AUC | PR-AUC | H-Measure | Recall | F1-Score |
|-------|---------|---------|-----------|--------|----------|
| **Gradient Boosting (GB)** | **0.8198** | **0.8447** | **0.3485** | 0.7954 | **0.7741** |
| Random Forest (RF) | 0.8103 | 0.8340 | 0.3262 | 0.7814 | 0.7666 |
| XGBoost (XGB) | 0.8048 | 0.8308 | 0.3201 | 0.7692 | 0.7581 |
| Support Vector Machine (SVM) | 0.7839 | 0.8118 | 0.2831 | **0.7916** | 0.7545 |
| Multi-Layer Perceptron (MLP) | 0.7843 | 0.8097 | 0.2838 | 0.7621 | 0.7478 |
| Logistic Regression (LR) | 0.7481 | 0.7767 | 0.2240 | 0.7730 | 0.7286 |
| Naive Bayes (NB) | 0.7128 | 0.7327 | 0.1746 | 0.7381 | 0.7098 |
| Decision Tree (DT) | 0.6557 | 0.6501 | 0.1137 | 0.6899 | 0.6916 |

**Best Model**: Gradient Boosting (GB)
- ROC-AUC: 0.8198 (1st)
- PR-AUC: 0.8447 (1st)
- H-Measure: 0.3485 (1st)
- F1-Score: 0.7741 (1st)

**Experimental Setup**:
- Variables: 14 selected variables
- Iterations: 50 random seeds
- Evaluation: Mean performance across 50 iterations
- Primary Metric: ROC-AUC (appropriate for balanced data)

---

## 📂 Repository Structure

```
p2p-credit-risk-analysis/
├── data/                          # Raw data (4.3 MB)
│   └── sentiment_scoring.25.12.30.xlsx
├── tables/                        # Generated tables (CSV)
│   ├── table_2_1_repayment_distribution.csv
│   ├── table_2_2_descriptive_statistics.csv
│   ├── table_2_3_text_statistics.csv
│   └── table_4_1_model_performance.csv
├── code/                          # Source code
│   ├── generate_table_2_1_repayment_distribution.py
│   ├── generate_table_2_2_descriptive_statistics.py
│   ├── generate_table_2_3_text_statistics.py
│   ├── generate_table_4_1_model_performance.py
│   ├── preprocessing/             # (Future: preprocessing scripts)
│   ├── models/                    # (Future: model training scripts)
│   └── evaluation/                # (Future: evaluation scripts)
├── figures/                       # (Future: generated figures)
├── results/                       # (Future: experimental results)
├── docs/                          # Documentation
│   └── DIRECTORY_STRUCTURE.md
├── .gitignore
├── requirements.txt
├── README.md
├── GITHUB_SETUP.md
└── REPOSITORY_SUMMARY.md          # This file
```

**Total Size**: 4.4 MB  
**Files**: 13 files  
**Directories**: 9 directories

---

## 🔧 Reproducibility

### All Code is Self-Contained
- ✅ Starts from raw data file
- ✅ No intermediate files required
- ✅ No external dependencies (except standard libraries)
- ✅ Deterministic output

### Version Control
- ✅ All code, tables, and documentation in Git
- ✅ Clear commit history
- ✅ No overwriting of previous versions

### Dependencies
```
pandas>=2.0.0
numpy>=1.24.0
openpyxl>=3.1.0
scikit-learn>=1.3.0
```

---

## 🚀 Quick Start

### Generate All Tables

```bash
cd /home/ubuntu/p2p-credit-risk-analysis

# Table 2-1
python3 code/generate_table_2_1_repayment_distribution.py

# Table 2-2
python3 code/generate_table_2_2_descriptive_statistics.py

# Table 2-3
python3 code/generate_table_2_3_text_statistics.py

# Table 4-1
python3 code/generate_table_4_1_model_performance.py
```

### Verify Results

```bash
ls -lh tables/
```

Expected output:
```
table_2_1_repayment_distribution.csv
table_2_2_descriptive_statistics.csv
table_2_3_text_statistics.csv
table_4_1_model_performance.csv
```

---

## 📝 Git Commit History

```
67d2c85 Add GitHub setup instructions
8d2b7da Add Table 4-1: Model Performance Comparison
eee9470 Initial commit: Add Tables 2-1, 2-2, 2-3 with raw data and documentation
```

---

## 🎯 Next Steps

### To Add
- [ ] Preprocessing scripts (`code/preprocessing/`)
- [ ] Model training scripts (`code/models/`)
- [ ] Evaluation scripts (`code/evaluation/`)
- [ ] Figures (`figures/`)
- [ ] Experimental results (`results/`)

### GitHub Push

See `GITHUB_SETUP.md` for detailed instructions.

**Quick Push** (after creating repository on GitHub):
```bash
cd /home/ubuntu/p2p-credit-risk-analysis
git remote add origin https://github.com/dongwoo2022008/p2p-credit-risk-analysis.git
git branch -M main
git push -u origin main
```

---

## 📊 Key Research Findings

### Variable Selection
- **14 variables** selected from original 17
- Selection based on 50-iteration experiments
- Removed weak variables: Gender, Loan Term, Months of Service

### Data Characteristics
- **Balanced dataset**: 55.34% default vs 44.66% repayment
- **Primary metric**: ROC-AUC (appropriate for balanced data)
- **Secondary metrics**: PR-AUC, H-Measure, Recall, F1-Score

### Model Performance
- **Best model**: Gradient Boosting (ROC-AUC 0.8198)
- **Best recall**: SVM (0.7916) - minimizes false negatives
- **Ensemble methods** (GB, RF, XGB) outperform linear models

---

## 📧 Contact

For questions or issues:
- GitHub: [@dongwoo2022008](https://github.com/dongwoo2022008)
- Repository: https://github.com/dongwoo2022008/p2p-credit-risk-analysis

---

**Last Updated**: 2025-02-03  
**Status**: Ready for GitHub push
