class Ticket:
    def __init__(self, flight, class_):
        self.flight = flight
        self.class_ = class_

    def print(self):
        print(f"Я билетик на рейс {self.flight} в класс {self.class_}")


ticket_1 = Ticket("SP-1011", "econom")
ticket_2 = Ticket("SP-101", "econom")
tickets = [ticket_1, ticket_2]
for ticket in tickets:
    ticket.print()
