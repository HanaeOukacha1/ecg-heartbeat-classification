# ECG Heartbeat Classification

**CNN Conv1D on MIT-BIH Arrhythmia Dataset — 98.67% accuracy | F1-Macro 0.92**

*Individual project — Kaggle intra-promotion competition @ ENSIASD (2025-2026)*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

---

## Overview

This project implements and compares multiple ML/DL models for automatic ECG heartbeat classification on the **MIT-BIH Arrhythmia Dataset** (Kaggle). The goal is to classify each heartbeat into one of 5 cardiac categories, supporting automated arrhythmia detection.

## Results

| Model | Accuracy | F1-Macro | Training Time |
|:---|:---:|:---:|:---:|
| Random Forest (baseline) | 97.20% | 0.8554 | 79s |
| ANN (MLP) | 98.11% | 0.8964 | 60s |
| BiLSTM | 98.03% | 0.8944 | 719s |
| **CNN Conv1D** | **98.67%** | **0.9192** | 190s |

**Best model: CNN Conv1D** — captures local morphological patterns (QRS complex, P and T waves) which are the discriminating features between ECG classes.

## Dataset

- **Source:** [ECG Heartbeat Categorization Dataset](https://www.kaggle.com/datasets/shayanfazeli/heartbeat) — MIT-BIH Arrhythmia Database
- **Train:** 87,554 samples | **Test:** 21,892 samples
- **Features:** 187 normalized time points per heartbeat
- **Classes:** Normal, Supraventricular, Ventricular, Fusion, Unknown

## Models Compared

### 1. Random Forest (Baseline)
- 200 trees, class_weight='balanced'
- 5-fold stratified cross-validation: F1-Macro = 0.8367

### 2. ANN / MLP
- 4 hidden layers: 256 → 128 → 64 → 32
- BatchNorm + Dropout regularization

### 3. BiLSTM
- 2 bidirectional LSTM layers
- Designed for temporal dependencies

### 4. CNN Conv1D (Best)
- 3 Conv1D blocks: 64 → 128 → 256 filters
- GlobalAveragePooling to prevent overfitting
- **Best model** — local morphological patterns > long-range dependencies for short ECG sequences

## Architecture: CNN Conv1D

```
Input (187,)
  -> Conv1D(64, k=5) + BN + MaxPool(2) + Dropout(0.2)
  -> Conv1D(128, k=5) + BN + MaxPool(2) + Dropout(0.2)
  -> Conv1D(256, k=3) + BN + GlobalAvgPool + Dropout(0.3)
  -> Dense(128) + BN + Dropout(0.3)
  -> Dense(5, softmax)
Total parameters: 174,725
```

## Files

| File | Description |
|:---|:---|
| notebooka20fc60088.ipynb | Full Jupyter notebook — EDA, preprocessing, training, evaluation |
| rapport.pdf | Technical report (LaTeX) — detailed methodology and results |
| Cahier_des_Charges_Projet_IA.pdf | Project specifications |
| image*.png | Results visualizations (confusion matrices, learning curves) |
| check_nb.py | Notebook validation script |

## Key Findings

- CNN outperforms BiLSTM on short ECG sequences (187 points) because local morphological patterns matter more than long-range temporal dependencies
- Class imbalance (Normal = 82.77%) is the main challenge — minority classes (Supraventricular, Fusion) are the hardest to classify
- BatchNorm + Dropout + EarlyStopping prevented all overfitting

---

*Kaggle competition dataset — MIT-BIH Arrhythmia Database*