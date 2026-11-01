# Predictive Hypervisor Resource Orchestration

## Project Overview
This project implements a predictive resource-monitoring and early-warning prototype for virtual machines. It collects system resource metrics, uses machine learning to estimate potential resource risks, and generates resource-management recommendations.

## Objectives
- Monitor CPU and RAM utilization across virtual machines.
- Collect advanced system signals.
- Prepare datasets for early-warning prediction.
- Train a Random Forest classifier.
- Classify virtual machines according to predicted warning risk.
- Generate resource-management recommendations.

## Technologies Used
- Python
- Ubuntu Linux
- Oracle VirtualBox
- Pandas
- Scikit-learn
- Matplotlib
- Psutil
- Joblib

## Project Structure

| File | Purpose |
|---|---|
| `heavy.py` | Generates the Heavy VM workload |
| `light.py` | Generates the Light VM workload |
| `monitor.py` | Basic resource monitoring |
| `advanced_monitor.py` | Collects advanced system metrics |
| `prepare_early_warning.py` | Prepares the early-warning dataset |
| `train_early_warning.py` | Trains and evaluates the Random Forest model |
| `run_early_warning.py` | Performs early-warning predictions |
| `feature_importance.py` | Analyzes model feature importance |
| `decision_engine.py` | Classifies risk and generates recommendations |

## Machine Learning
A Random Forest classifier is used to predict potential resource warnings based on collected system metrics.

The model considers:
- CPU utilization
- RAM utilization
- Page-fault rate
- Major page-fault rate
- Context-switch rate
- Interrupt rate
- Memory pressure
- Disk read and write activity

## Decision Engine
The decision engine classifies VMs into three categories:

- NORMAL
- CAUTION
- HIGH RISK

It generates recommendations based on the predicted warning probability.

## Experimental Result
In the final recorded decision-engine run:

| VM | Warning Probability | Status |
|---|---:|---|
| Heavy VM | 32% | CAUTION |
| Light VM | 0% | NORMAL |

## Important Limitation
This is a working prototype using VirtualBox and Ubuntu virtual machines. It generates resource-management recommendations but does not automatically resize VM allocations or perform live migration. These are planned future enhancements.

The early-warning dataset is relatively small, so model evaluation is preliminary and requires further testing.

## Future Scope
- Actual dynamic CPU and RAM resizing.
- Live virtual-machine migration.
- Resource rebalancing across hosts.
- Larger datasets and improved model evaluation.
- Feedback-driven model improvement.

## Output Files
The repository includes experimental datasets, the trained early-warning model, prediction graphs, and the resource recommendation report.
