from sklearn.model_selection import train_test_split
import yaml
from src.utils.logger import get_logger
from src.utils.exceptions import SplitError

logger = get_logger(__name__)

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def split_data(X, y):
    """Splits the dataset into training and testing sets."""
    config = load_config()
    test_size = config["preprocessing"]["test_size"]
    random_state = config["preprocessing"]["random_state"]

    try:
        logger.info(f"Splitting dataset with test_size={test_size}...")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        logger.info("Data split completed.")
        return X_train, X_test, y_train, y_test

    except Exception as e:
        logger.error(f"Data split failed: {e}")
        raise SplitError("Failed to split data.")
