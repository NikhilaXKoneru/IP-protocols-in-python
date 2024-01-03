import random

class RED:
    def __init__(self, min_threshold, max_threshold, min_p, max_p, tc):
        self.min_threshold = min_threshold
        self.max_threshold = max_threshold
        self.min_p = min_p
        self.max_p = max_p
        self.tc = tc
        self.avg_queue_length = 0.0
        self.drop_prob = 0.0

    def update(self, queue_length):
        self.avg_queue_length = (1 - 1 / self.tc) * self.avg_queue_length + (1 / self.tc) * queue_length
        self.drop_prob = self.max_p - ((self.avg_queue_length - self.min_threshold) / (self.max_threshold - self.min_threshold)) * (self.max_p - self.min_p)

    def packet_arrival(self):
        return random.uniform(0, 1) >= self.drop_prob

    def mark_packet(self):
        return random.choice([0, 1])  # Simulated marking of packets with DEC bit

class Sender:
    def __init__(self):
        self.sending_rate = 1  # Initial sending rate

    def react_to_marked_packet(self, dec_bit):
        if dec_bit == 1:
            self.sending_rate *= 0.9  # Reduce sending rate upon marking

class Receiver:
    def receive_packet(self, packet):
        return packet

red = RED(min_threshold=10, max_threshold=30, min_p=0.001, max_p=0.1, tc=5)
sender = Sender()
receiver = Receiver()

for _ in range(100):
    queue_length = random.randint(1, 40)  # Simulated queue length
    red.update(queue_length)
    if red.packet_arrival():
        dec_bit = red.mark_packet()
        sender.react_to_marked_packet(dec_bit)
        packet = "Packet with DEC bit: " + str(dec_bit)
        received_packet = receiver.receive_packet(packet)
        print(received_packet)
    else:
        print("Packet passed.")
