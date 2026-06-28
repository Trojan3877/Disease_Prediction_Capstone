# agents/state.py
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class DiagnosticState(BaseModel):
    """
    The immutable telemetry data contract governing the Disease Prediction Capstone.
    Enforces rigid data validation on incoming raw biomarkers and vital vectors.
    """
    patient_id: str
    biomarker_features: Dict[str, float] = Field(default_factory=dict)
    systolic_bp: float
    diastolic_bp: float
    
    # Mathematical Diagnostic Outputs
    risk_probability: float = 0.0
    diagnostic_classification: Optional[str] = None
    compliance_risk_score: float = 0.0
    
    # LLM Clinical Analyst Inference Space
    llm_compliance_analysis: Optional[str] = None
    llm_clinical_suggestions: Optional[str] = None
    override_active: bool = False
    
    # Pipeline Observability Tracking
    processing_latency_ms: float = 0.0
    execution_trace: List[str] = Field(default_factory=list)

    def append_trace(self, log_msg: str) -> "DiagnosticState":
        """Generates a thread-safe read-only snapshot with appended auditing logs."""
        return self.model_copy(update={"execution_trace": list(self.execution_trace) + [log_msg]})
