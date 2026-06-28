# agents/guards.py
class DiagnosticDeadlineException(Exception):
    """Raised when clinical safety checks cross strict execution latency limits."""
    pass

class DiagnosticCircuitBreaker:
    """
    Active hardware-simulated fail-safe designed to monitor processing latency
    and prevent hung threads from stalling critical healthcare interfaces.
    """
    def __init__(self, hard_deadline_ms: float = 5.0):
        self.hard_deadline_ms = hard_deadline_ms
        self.breaker_status = "CLOSED"  # CLOSED (Safe), OPEN (Emergency Bypass)

    def evaluate_execution_timing(self, elapsed_ms: float):
        """Trips the circuit breaker instantly if diagnostic evaluation stalls processing paths."""
        if elapsed_ms > self.hard_deadline_ms:
            self.breaker_status = "OPEN"
            raise DiagnosticDeadlineException(
                f"CRITICAL COMPUTE LATENCY FAULT: Diagnostic engine took {elapsed_ms:.2f}ms (Limit: {self.hard_deadline_ms}ms)."
            )
