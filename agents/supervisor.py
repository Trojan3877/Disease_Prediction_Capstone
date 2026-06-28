# agents/supervisor.py
import time
from .state import DiagnosticState
from .guards import DiagnosticCircuitBreaker, DiagnosticDeadlineException

class DiagnosticSupervisorEngine:
    """
    The central Clinical Orchestration Core. Manages mathematical data ingestion workers,
    coordinates biomarker analytics, and triggers LLM diagnostic compliance audits.
    """
    def __init__(self, use_llm_analyst: bool = True):
        self.breaker = DiagnosticCircuitBreaker(hard_deadline_ms=5.0)
        self.use_llm_analyst = use_llm_analyst

    def process_patient_record(self, patient_id: str, biomarkers: dict, s_bp: float, d_bp: float) -> DiagnosticState:
        state = DiagnosticState(patient_id=patient_id, biomarker_features=biomarkers, systolic_bp=s_bp, diastolic_bp=d_bp)
        state = state.append_trace("Ingested raw patient biomarker telemetry frame.")
        
        start_time = time.time()
        try:
            # 1. Evaluate Quantitative Vital Threshold Boundaries (Worker 1)
            if state.systolic_bp > 140.0 or state.diastolic_bp > 90.0:  # Stage 2 Hypertension Indicators
                state = state.model_copy(update={"compliance_risk_score": 8.5}).append_trace("Worker 1: Critical physiological anomaly identified.")
            
            # 2. Invoke Generative LLM Compliance Layer (Agent 2)
            if self.use_llm_analyst and state.compliance_risk_score > 7.0:
                state = self._invoke_llm_clinical_analyst(state)

            # Check timing compliance constraints
            elapsed_ms = (time.time() - start_time) * 1000
            self.breaker.evaluate_execution_timing(elapsed_ms)
            
            # Populate baseline model mock inference output if healthy
            if not state.diagnostic_classification:
                state = state.model_copy(update={"diagnostic_classification": "NORMAL_EVALUATION", "risk_probability": 0.12})
            
            return state.model_copy(update={"processing_latency_ms": elapsed_ms})

        except DiagnosticDeadlineException as dde:
            # Emergency Circuit Breaker Fallback Path
            elapsed_ms = (time.time() - start_time) * 1000
            return state.model_copy(update={
                "override_active": True,
                "diagnostic_classification": "LATENCY_OVERRIDE_TRIGGERED",
                "llm_clinical_suggestions": "CRITICAL SLA OVERRIDE: ROUTE PATIENT TO SECONDARY METRIC CACHE INSTANTLY.",
                "processing_latency_ms": elapsed_ms
            }).append_trace(f"DIAGNOSTIC CIRCUIT BREAKER OPENED: {str(dde)}")

    def _invoke_llm_clinical_analyst(self, state: DiagnosticState) -> DiagnosticState:
        """Simulates structured Claude 3.5 Sonnet context-aware clinical data analysis."""
        mock_analysis = "High-risk hypertensive tracking pattern detected. Cross-reference with standard clinical pathways immediately."
        return state.model_copy(update={
            "llm_compliance_analysis": "COMPLIANCE_REVIEW_REQUIRED",
            "llm_clinical_suggestions": mock_analysis,
            "diagnostic_classification": "EVALUATE_HIGH_RISK_HYPERTENSION"
        }).append_trace("LLM Analyst Agent: Structural clinical safety insights computed and returned.")
