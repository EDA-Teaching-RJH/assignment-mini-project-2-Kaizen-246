# This file has the class definitions for the application
# It demonstrates OOP using a base class and inheritance
# Base class representing a general log entry
# Stores common attributes shared by all entry types
class LogEntry:
    def __init__(self, entry_id, date, email, equipment_id, description):
        self.entry_id = entry_id
        self.date = date
        self.email = email
        self.equipment_id = equipment_id
        self.description = description

    def display(self):
        print(self.entry_id, self.date, self.email)
# Base class representing a general log entry
# Stores common attributes shared by all entry types
class ExperimentEntry(LogEntry):
    def __init__(self, entry_id, date, email, equipment_id, description, voltage, current):
        super().__init__(entry_id, date, email, equipment_id, description)
        self.voltage = voltage
        self.current = current

    def power(self):
        return self.voltage * self.current

# Base class representing a general log entry
# Stores common attributes shared by all entry types
class FaultEntry(LogEntry):
    def __init__(self, entry_id, date, email, equipment_id, description, severity, resolved):
        super().__init__(entry_id, date, email, equipment_id, description)
        self.severity = severity
        self.resolved = resolved