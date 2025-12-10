from src.models.train import train_models

def test_training_pipeline():
    model, auc = train_models()

    assert model is not None
    assert auc >= 0 and auc <= 1
