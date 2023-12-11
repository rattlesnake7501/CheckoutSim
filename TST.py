from enum import Enum
from datetime import datetime

class LaneType(Enum):
    REGULAR = "Regular"
    SELF_SERVICE = "Self-Service"

class LaneStatus(Enum):
    OPENED = "Opened"
    CLOSED = "Closed"

class CheckoutLane:
    def __init__(self, lane_type, capacity):
        self.lane_type = lane_type
        self.status = LaneStatus.CLOSED
        self.timestamp = datetime.now()
        self.customers = []
        self.capacity = capacity

def generate_lane(lane_type, capacity):
    return CheckoutLane(lane_type, capacity)

def add_customer_to_lane(customer, lane):
    if len(lane.customers) < lane.capacity:
        lane.customers.append(customer)
    else:
        open_new_lane(customer.lane_type, customer.basket_size)

def remove_customer_from_lane(customer, lane):
    lane.customers.remove(customer)

def open_new_lane(customer_type, basket_size):
    # Placeholder logic to determine if a new lane needs to be opened
    if customer_type == LaneType.REGULAR and basket_size > 5:
        new_lane = generate_lane(LaneType.REGULAR, capacity=10)
        new_lane.status = LaneStatus.OPENED
        return new_lane
    elif customer_type == LaneType.SELF_SERVICE and basket_size > 3:
        new_lane = generate_lane(LaneType.SELF_SERVICE, capacity=8)
        new_lane.status = LaneStatus.OPENED
        return new_lane
    else:
        display_lane_saturation()

def close_lane(lane):
    lane.status = LaneStatus.CLOSED

def display_lane_status(lanes):
    print("### Lane status at some time during simulation###")
    total_customers = sum(len(lane.customers) for lane in lanes)
    print(f"Total number of customers waiting to check out at {datetime.now().strftime('%H:%M')} is: {total_customers}")

    for idx, lane in enumerate(lanes, start=1):
        customer_display = " ".join("*" for _ in range(len(lane.customers)))
        status_display = f"{lane.lane_type.value}{idx}({lane.status.value})-> {customer_display}" if lane.status == LaneStatus.OPENED else f"{lane.lane_type.value}{idx}({lane.status.value})"
        print(status_display)

def display_lane_saturation():
    print("No new lane available. Displaying lane saturation on the console.")

# Example usage
lane1 = generate_lane(LaneType.REGULAR, capacity=5)
lane2 = generate_lane(LaneType.REGULAR, capacity=8)
lanes = [lane1, lane2]

class Customer:
    def __init__(self, lane_type, basket_size):
        self.lane_type = lane_type
        self.basket_size = basket_size

customer1 = Customer(LaneType.REGULAR, basket_size=7)
customer2 = Customer(LaneType.SELF_SERVICE, basket_size=4)

add_customer_to_lane(customer1, lane1)
add_customer_to_lane(customer2, lane1)

display_lane_status(lanes)