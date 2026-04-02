from unittest.mock import patch
import pandas as pd
from load_data import load_data

@patch("load_data.load_config")
@patch("pandas.read_csv")
def test_load_data(mock_read_csv, mock_load_config):
    mock_load_config.return_value = {"paths": {"raw_data": "data/raw/diabetes.csv"}}
    mock_read_csv.return_value = pd.DataFrame({
        "Pregnancies": [1, 2],
        "Glucose": [85, 120],
        "Outcome": [0, 1],
    })

    df = load_data()

    assert df is not None
    assert len(df) > 0
    assert "Outcome" in df.columns
