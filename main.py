class Layer:
    def __init__(self, number, description):
        self.number = number
        self.description = description

    def process(self, message):
        return message


def display_layer(layer, message):
    print(f"{layer.number} - {layer.description}")
    print(f"{message}\n")


# Creating layers
physical_layer = Layer(1, "Physical Layer")
data_link_layer = Layer(2, "Data Link Layer")
network_layer = Layer(3, "Network Layer")
transport_layer = Layer(4, "Transport Layer")
session_layer = Layer(5, "Session Layer")
presentation_layer = Layer(6, "Presentation Layer")
application_layer = Layer(7, "Application Layer")

# Simulating the message encapsulation process
message = "Hello, World!"
for layer in [physical_layer, data_link_layer, network_layer, transport_layer, session_layer, presentation_layer, application_layer]:
    message = layer.process(message)
    display_layer(layer, message)
