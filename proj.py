import random


class CheckoutLane:
    def __init__(self, lane_type, status, ):
        self.lane_type = lane_type  # 'self-service' or 'manned'
        self.status = status  # 'opened' or 'closed'

    def generate_lane(self, lane, time):
        self.lane = lane
        self.time = time

    def customer_add(self, customer):
        self.customer = customer
        random_number = random.randint(1, 10)

    def customer_remove(self, customer):
        self.customer = customer

