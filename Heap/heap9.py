class Event:
    def __init__(self, timestamp, plane_number, type):
        self.timestamp = timestamp
        self.plane_number = plane_number
        self.type = type

    def __lt__(self, other):
        return self.timestamp < other.timestamp

class AirportSimulation:
    def __init__(self):
        self.events = []

    def add_event(self, timestamp, plane_number, type):
        new_event = Event(timestamp, plane_number, type)
        for i, event in enumerate(self.events):
            if event > new_event:
                self.events.insert(i, new_event)
                return
        self.events.append(new_event)