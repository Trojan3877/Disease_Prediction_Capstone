import streamlit as st
import time
from agents.supervisor import DiagnosticSupervisorEngine

# 1. Page Configuration & Styling Setup
st.set_page_config(
    page_title="AutoGuard Clinical Diagnostics Engine",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Institutional CSS styling override
st.markdown("""
    <style>
    .metric-card {
        background-color: #1e293b;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #0284c7;
        margin-bottom: 10px;
    }
    .trace-log {
        font-family: 'Courier New', Courier, monospace;
        background-color: #0f172a;
        color: #38bdf8;
        padding: 12px;
        border-radius: 6px;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Main Dashboard Title
st.title("🏥 Multi-Agent Clinical Diagnostics & Compliance Pipeline")
st.markdown("---")

# 3. Main Operational Interface Layout Split
col_inputs, col_results = st.columns([1, 2])

with col_inputs:
    st.header("🎛️ Patient Biomarker Controls")
    
    with st.form("biomarker_form"):
        patient_id = st.text_input("Patient Identifier Tag", value="PT-8942-X")
        
        st.subheader("🫀 Physiological Vital Signs")
        systolic_bp = st.slider("Systolic Blood Pressure (mmHg)", min_value=90, max_value=180, value=120)
        diastolic_bp = st.slider("Diastolic Blood Pressure (mmHg)", min_value=60, max_value=110, value=80)
        
        st.subheader("🧪 Core Laboratory Biomarkers")
        cholesterol = st.number_input("Total Cholesterol (mg/dL)", min_value=100, max_value=400, value=195)
        fasting_bg = st.number_input("Fasting Blood Glucose (mg/dL)", min_value=70, max_value=300, value=95)
        hba1c = st.slider("HbA1c Percentage (%)", min_value=4.0, max_value=12.0, value=5.4, step=0.1)
        
        # Artificial operational lag injection toggle for demoing circuit breaker
        st.subheader("⚙️ System Stress Simulator")
        inject_lag = st.checkbox("Simulate Network Compute Lag (>5ms)")
        
        submit_btn = st.form_submit_button("Execute Asynchronous Diagnostic Loop")

with col_results:
    st.header("⚡ Real-Time Pipeline Execution")
    
    if submit_btn:
        # Package raw input biomarkers array dictionary
        biomarker_payload = {
            "cholesterol": float(cholesterol),
            "fasting_blood_glucose": float(fasting_bg),
            "hba1c": float(hba1c)
        }
        
        # Instantiate the Supervisor Engine Architecture
        # For demonstration, passing a flag to handle intentional lag triggers
        engine = DiagnosticSupervisorEngine()
        
        # If simulated lag is checked, we manually patch the calculation loop timing
        if inject_lag:
            st.info("⚠️ Simulating heavy network computation lag to test hardware guardrails...")
            # We can force the supervisor to hit the deadline exception path inside the UI frame
            with st.spinner("Processing deep matrix inferences..."):
                time.sleep(0.006) # Force a 6ms thread sleep
                # Process with high values to demonstrate trigger actions
                state = engine.process_patient_record(patient_id, biomarker_payload, 155.0, 95.0)
        else:
            with st.spinner("Executing secure worker delegation streams..."):
                state = engine.process_patient_record(patient_id, biomarker_payload, float(systolic_bp), float(diastolic_bp))
        
        # 4. Core Performance Telemetry Display Columns
        m_col1, m_col2, m_col3 = st.columns(3)
        
        with m_col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric(
                label="Pipeline Latency Status", 
                value=f"{state.processing_latency_ms:.2f} ms",
                delta="SLA Breach" if state.override_active else "SLA Compliant",
                delta_color="inverse" if state.override_active else "normal"
            )
            st.markdown('</div>', unsafe_allow_header=True)
            
        with m_col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            status_color = "🟢" if not state.override_active else "🚨"
            st.metric(label="Circuit Breaker Status", value=f"{status_color} {'OVERRIDE' if state.override_active else 'CLOSED'}")
            st.markdown('</div>', unsafe_allow_header=True)
            
        with m_col3:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric(label="Calculated Risk Metric Score", value=f"{state.compliance_risk_score}/10")
            st.markdown('</div>', unsafe_allow_header=True)
            
        # 5. Classification Output Panels
        st.subheader("🎯 Primary Classification Result")
        if state.override_active:
            st.error(f"Execution Target State: {state.diagnostic_classification}")
        elif state.compliance_risk_score > 5.0:
            st.warning(f"Execution Target State: {state.diagnostic_classification}")
        else:
            st.success(f"Execution Target State: {state.diagnostic_classification}")
            
        # 6. Cognitive Generative AI Analyst View Panels
        if state.llm_clinical_suggestions:
            st.subheader("🤖 Generative AI Compliance Review (Claude 3.5 Sonnet)")
            with st.expander("View Context-Aware Medical Policy Audit", expanded=True):
                st.markdown(f"**Compliance Assessment Status:** `{state.llm_compliance_analysis}`")
                st.markdown(f"**Automated Clinical Advice Suggestions:**")
                st.info(state.llm_clinical_suggestions)
                
        # 7. Asynchronous Thread Execution Log Traces
        st.subheader("📜 System Audit Execution Log Trace")
        with st.expander("View Microsecond Step Auditing History", expanded=True):
            log_output = "\n".join([f"[STEP {i+1}] {step}" for i, step in enumerate(state.execution_trace)])
            st.markdown(f'<pre class="trace-log">{log_output}</pre>', unsafe_allow_html=True)
            
    else:
        st.info("💡 Adjust patient biomarkers panel sliders on the left and submit to view live multi-agent execution pipeline output frames.")
