class CreditBasedFlowControl:
    def __init__(self, sender_rate, receiver_capacity):
        self.sender_rate = sender_rate
        self.receiver_capacity = receiver_capacity
        self.sender_credits = 0

    def update_receiver_capacity(self, new_capacity):
        self.receiver_capacity = new_capacity

    def send_data(self, data_size):
        if data_size <= self.sender_credits:
            print(f"Sender sending {data_size} bytes to the receiver.")
            self.sender_credits -= data_size
        else:
            print("Not enough credits. Waiting for more credits from the receiver.")

    def receive_acknowledgment(self, ack_size):
        self.sender_credits += ack_size
        print(f"Receiver acknowledges {ack_size} bytes. Sender credits updated to {self.sender_credits}.")

# Example usage:
flow_control = CreditBasedFlowControl(sender_rate=10, receiver_capacity=5)

# Simulate data transfer
data_to_send = 8
flow_control.send_data(data_to_send)

# Simulate acknowledgment from the receiver
ack_size = 4
flow_control.receive_acknowledgment(ack_size)

# Update receiver capacity
new_receiver_capacity = 10
flow_control.update_receiver_capacity(new_receiver_capacity)

# Send more data after the update
data_to_send = 6
flow_control.send_data(data_to_send)
