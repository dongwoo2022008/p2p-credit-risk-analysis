# Directory Structure

## Overview

This document describes the organization of the repository for reproducibility and clarity.

## Directory Layout

```
p2p-credit-risk-analysis/
├── data/                          # Raw data files (DO NOT MODIFY)
│   └── sentiment_scoring.25.12.30.xlsx
│
├── tables/                        # Generated tables (CSV format)
│   ├── table_2_1_repayment_distribution.csv
│   ├── table_2_2_descriptive_statistics.csv
│   ├── table_2_3_text_statistics.csv
│   └── table_4_1_model_performance.csv (to be added)
│
├── figures/                       # Generated figures and plots
│   ├── figure_1_*.png            # Figure 1: ...
│   ├── figure_2_*.png            # Figure 2: ...
│   └── ...
│
├── code/                          # Source code
│   ├── generate_table_2_1_repayment_distribution.py
│   ├── generate_table_2_2_descriptive_statistics.py
│   ├── generate_table_2_3_text_statistics.py
│   │
│   ├── preprocessing/             # Data preprocessing
│   │   ├── load_data.py
│   │   ├── clean_data.py
│   │   └── feature_engineering.py
│   │
│   ├── models/                    # Model training
│   │   ├── baseline_models.py
│   │   ├── text_integration.py
│   │   └── ensemble_models.py
│   │
│   └── evaluation/                # Model evaluation
│       ├── metrics.py
│       ├── cross_validation.py
│       └── statistical_tests.py
│
├── results/                       # Experimental results
│   ├── baseline/                  # Baseline model results
│   ├── text_integration/          # Text integration results
│   └── ensemble/                  # Ensemble model results
│
├── docs/                          # Documentation
│   ├── DIRECTORY_STRUCTURE.md     # This file
│   ├── DATA_DESCRIPTION.md        # Data description
│   └── METHODOLOGY.md             # Methodology description
│
├── .gitignore                     # Git ignore file
├── requirements.txt               # Python dependencies
└── README.md                      # Main documentation
```

## Directory Purposes

### `data/`
- Contains raw, unmodified data files
- **DO NOT MODIFY** files in this directory
- All preprocessing should be done in code

### `tables/`
- Contains generated tables in CSV format
- Named as `table_X_Y_description.csv`
- Can be regenerated from code

### `figures/`
- Contains generated figures and plots
- Named as `figure_X_description.png`
- Can be regenerated from code

### `code/`
- Contains all source code
- Self-contained scripts that start from raw data
- Organized by functionality (preprocessing, models, evaluation)

### `results/`
- Contains experimental results
- Organized by experiment type
- Includes logs, metrics, and intermediate outputs

### `docs/`
- Contains documentation files
- Describes data, methodology, and structure

## Naming Conventions

### Tables
- Format: `table_X_Y_description.csv`
- Example: `table_2_1_repayment_distribution.csv`

### Figures
- Format: `figure_X_description.png`
- Example: `figure_1_roc_curve.png`

### Code
- Format: `verb_noun_description.py`
- Example: `generate_table_2_1_repayment_distribution.py`

### Results
- Format: `experiment_name_YYYYMMDD.csv`
- Example: `baseline_50iterations_20250203.csv`

## Reproducibility Guidelines

1. **All code starts from raw data** (`data/` directory)
2. **No intermediate files required** (except explicitly documented)
3. **Version control** for all code and documentation
4. **Clear dependencies** listed in `requirements.txt`
5. **Self-contained scripts** (no external dependencies except standard libraries)

## Adding New Content

### New Table
1. Create script in `code/generate_table_X_Y_description.py`
2. Generate CSV in `tables/table_X_Y_description.csv`
3. Update README.md with description and usage

### New Figure
1. Create script in `code/generate_figure_X_description.py`
2. Generate PNG in `figures/figure_X_description.png`
3. Update README.md with description and usage

### New Experiment
1. Create script in `code/models/` or `code/evaluation/`
2. Save results in `results/experiment_name/`
3. Document methodology in `docs/METHODOLOGY.md`

## Version Control

- Commit all code, tables, and documentation
- **DO NOT** overwrite previous versions
- Create new versions with date suffix if needed
- Use meaningful commit messages

## Questions?

Open an issue on GitHub or contact the repository maintainer.
