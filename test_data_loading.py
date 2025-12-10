from src.data.load_data import load_data

def test_load_data():
    df = load_data()
    assert df is not None
    assert len(df) > 0
    assert "Outcome" in df.columns
