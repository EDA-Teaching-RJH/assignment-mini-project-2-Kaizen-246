print ("LabLog Manager starting...")

from lablog.models import LogEntry 
entry = LogEntry("EXP-001", "2026-03-17", "test@email.com", "EQ-1", "Test")
entry.display()

from lablog.models import ExperimentEntry, FaultEntry

exp = ExperimentEntry(
    "EXP-001",
    "2026-03-17",
    "test@email.com",
    "EQ-AB123",
    "Voltage test",
    10,
    2
)

fault = FaultEntry(
    "FLT-001",
    "2026-03-17",
    "fault@email.com",
    "EQ-XY999",
    "Motor failure",
    "high",
    False
)

print("Experiment Power:", exp.power())
fault.display()
