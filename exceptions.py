class DataLoadError(Exception):
    """Raised when the dataset fails to load."""
    pass

class PreprocessingError(Exception):
    """Raised when preprocessing fails."""
    pass

class SplitError(Exception):
    """Raised when train/test split fails."""
    pass

class FeatureEngineeringError(Exception):
    """Raised when feature engineering fails."""
    pass

class ModelTrainingError(Exception):
    """Raised during model training failure."""
    pass

class ModelLoadError(Exception):
    """Raised when model loading fails."""
    pass

class PredictionError(Exception):
    """Raised when prediction endpoint fails."""
    pass

class RAGError(Exception):
    """Raised when vector search or embedding fails."""
    pass

class MCPError(Exception):
    """Raised when MCP server or tools fail."""
    pass
