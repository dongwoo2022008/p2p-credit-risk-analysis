# P2P Lending Credit Risk Analysis

## 📋 Overview

This repository contains all materials for reproducing the research on Korean P2P lending credit risk evaluation using machine learning and text analysis.

**Research Focus**: Evaluating the impact of text information (loan purpose, repayment plan) on credit risk prediction performance.

---

## 📁 Repository Structure

```
p2p-credit-risk-analysis/
├── data/                          # Raw data files
│   └── sentiment_scoring.25.12.30.xlsx
├── tables/                        # Generated tables (CSV format)
│   ├── table_2_1_repayment_distribution.csv
│   ├── table_2_2_descriptive_statistics.csv
│   └── table_2_3_text_statistics.csv
├── figures/                       # Generated figures and plots
├── code/                          # Source code
│   ├── generate_table_2_1_repayment_distribution.py
│   ├── generate_table_2_2_descriptive_statistics.py
│   ├── generate_table_2_3_text_statistics.py
│   ├── preprocessing/             # Data preprocessing scripts
│   ├── models/                    # Model training scripts
│   └── evaluation/                # Model evaluation scripts
├── results/                       # Experimental results
├── docs/                          # Documentation
└── README.md                      # This file
```

---

## 📊 Tables

### Table 2-1: Distribution of Repayment Outcomes (2-Class)

Binary classification target distribution.

**Generation:**
```bash
python3 code/generate_table_2_1_repayment_distribution.py
```

**Output:** `tables/table_2_1_repayment_distribution.csv`

**Key Statistics:**
- Total samples: 6,057
- Default (1): 3,352 (55.34%)
- Repayment (0): 2,705 (44.66%)
- Imbalance ratio: 0.81:1 (Balanced)

---

### Table 2-2: Descriptive Statistics for 14 Variables

Descriptive statistics for the 14 selected structured variables.

**Generation:**
```bash
python3 code/generate_table_2_2_descriptive_statistics.py
```

**Output:** `tables/table_2_2_descriptive_statistics.csv`

**14 Selected Variables:**
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

**Note:** Removed 3 weak variables from original 17:
- Gender (성별) - Low feature importance
- Loan Term (신청기간) - Weak predictive power
- Months of Service (서비스이용개월수) - Not in final selection

---

### Table 2-3: Descriptive Statistics for Text Length

Text length statistics for title, loan purpose, and repayment plan.

**Generation:**
```bash
python3 code/generate_table_2_3_text_statistics.py
```

**Output:** `tables/table_2_3_text_statistics.csv`

**Text Fields:**
- Title (제목)
- Loan Purpose (신청목적)
- Repayment Plan (상환계획)
- Total (combined)

**Key Statistics:**
- Average total text length: 454.5 characters
- Median total text length: 370.0 characters
- All samples contain text (6,057/6,057)

---

## 🔧 Requirements

### Python Environment
```bash
Python 3.11+
pandas
numpy
openpyxl
scikit-learn
```

### Installation
```bash
pip install pandas numpy openpyxl scikit-learn
```

---

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/dongwoo2022008/p2p-credit-risk-analysis.git
cd p2p-credit-risk-analysis
```

### 2. Generate All Tables
```bash
# Table 2-1: Repayment distribution
python3 code/generate_table_2_1_repayment_distribution.py

# Table 2-2: Descriptive statistics
python3 code/generate_table_2_2_descriptive_statistics.py

# Table 2-3: Text length statistics
python3 code/generate_table_2_3_text_statistics.py
```

### 3. Check Results
```bash
ls -lh tables/
```

---

## 📈 Key Findings

### Variable Selection
- **14 variables selected** from original 17
- Removed: Gender, Loan Term, Months of Service
- Selection based on 50-iteration experiments with 95% CI overlap test

### Data Characteristics
- **Balanced dataset**: 55.34% default vs 44.66% repayment
- **Primary metric**: ROC-AUC (appropriate for balanced data)
- **Secondary metrics**: PR-AUC, H-Measure, Recall, F1-Score

### Text Information
- Average text length: 454.5 characters
- All samples contain textual information
- Text fields: Title + Loan Purpose + Repayment Plan

---

## 📝 Reproducibility

### Data
- Raw data: `data/sentiment_scoring.25.12.30.xlsx`
- Total samples: 6,057
- No missing values in selected 14 variables

### Code
- All table generation scripts are self-contained
- Start from raw data file
- No intermediate files required
- Deterministic output

### Version Control
- All code, tables, and documentation tracked in Git
- Each experiment version maintained separately
- No overwriting of previous results

---

## 📚 Citation

If you use this code or data, please cite:

```bibtex
@article{p2p_credit_risk_2025,
  title={Text-Enhanced Credit Risk Evaluation in P2P Lending: A Machine Learning Approach},
  author={[Author Names]},
  journal={[Journal Name]},
  year={2025}
}
```

---

## 📧 Contact

For questions or issues, please open an issue on GitHub or contact:
- GitHub: [@dongwoo2022008](https://github.com/dongwoo2022008)

---

## 📄 License

[To be determined]

---

## 🔄 Updates

### 2025-02-03
- Initial repository creation
- Added Table 2-1, 2-2, 2-3 generation scripts
- Added raw data file
- Created comprehensive documentation

---

## 🎯 Future Work

- [ ] Add Table 4-1: Model performance comparison
- [ ] Add preprocessing scripts
- [ ] Add model training scripts
- [ ] Add evaluation scripts
- [ ] Add figures and visualizations
- [ ] Add experiment configuration files
- [ ] Add requirements.txt
- [ ] Add automated testing

---

**Last Updated:** 2025-02-03
