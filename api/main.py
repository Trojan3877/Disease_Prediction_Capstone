# main.py
import sys
from agents.supervisor import DiagnosticSupervisorEngine

def run_system_audit():
    print("======================================================================")
    print("🏥 AUTO-GUARD CLINICAL DIAGNOSTICS: SYSTEM ORCHESTRATION RUN")
    print("======================================================================\n")
    
    # Initialize the institutional Multi-Agent Supervisor
    supervisor = DiagnosticSupervisorEngine()
    
    # Test Case 1: Healthy Patient Biomarker Vector Frame (SLA Compliant)
    print("[TEST 1] Processing standard physiological patient matrix...")
    normal_biomarkers = {"cholesterol": 185.0, "fasting_blood_glucose": 90.0, "hba1c": 5.2}
    state_one = supervisor.process_patient_record(
        patient_id="PT-001-NORMAL", 
        biomarkers=normal_biomarkers, 
        s_bp=118.0, 
        d_bp=76.0
    )
    
    print(f" -> Latency Profile: {state_one.processing_latency_ms:.4f} ms")
    print(f" -> Execution State: {state_one.diagnostic_classification}")
    print(f" -> Circuit Override Status: {state_one.override_active}")
    print(" -> Trace Log Snapshot:")
    for trace in state_one.execution_trace:
        print(f"    {trace}")
    print("\n----------------------------------------------------------------------\n")

    # Test Case 2: Volatile Biomarker Pattern (Triggers AI Compliance Audit Agent)
    print("[TEST 2] Processing high-risk hypertensive biomarker matrix...")
    risk_biomarkers = {"cholesterol": 285.0, "fasting_blood_glucose": 165.0, "hba1c": 8.1}
    state_two = supervisor.process_patient_record(
        patient_id="PT-999-CRITICAL", 
        biomarkers=risk_biomarkers, 
        s_bp=165.0, 
        d_bp=98.0
    )
    
    print(f" -> Latency Profile: {state_two.processing_latency_ms:.4f} ms")
    print(f" -> Execution State: {state_two.diagnostic_classification}")
    print(f" -> Compliance Status: {state_two.llm_compliance_analysis}")
    print(f" -> AI Suggestions: {state_two.llm_clinical_suggestions}")
    print(" -> Trace Log Snapshot:")
    for trace in state_two.execution_trace:
        print(f"    {trace}")
    print("\n======================================================================")

if __name__ == "__main__":
    run_system_audit()
