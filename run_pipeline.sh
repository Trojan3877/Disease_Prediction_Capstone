#!/usr/bin/env bash
set -e

# 1. Preprocess & train
python src/train.py --data_path data/raw/diabetes.csv --output_model models/trained_model.pkl

# 2. Evaluate
python src/evaluate.py --model_path models/trained_model.pkl --data_path data/raw/diabetes.csv

echo "🚀 Pipeline complete! Check results/ for metrics and plots."
