import time

class CheckoutLane:
    def __init__(self, lane_type, capacity):
        self.lane_type = lane_type
        self.status = 'closed'
        self.timestamp_created = time.strftime('%H:%M')
        self.customers = []
        self.capacity = capacity

    def open(self):
        self.status = 'open'

    def close(self):
        self.status = 'closed'

    def add_customer(self, customer):
        if len(self.customers) < self.capacity:
            self.customers.append(customer)
            return True
        else:
            return False

    def remove_customer(self, customer):
        if customer in self.customers:
            self.customers.remove(customer)

    def display_status(self):
        return f"{self.lane_type}({self.status}) -> {' '.join('*' for _ in range(len(self.customers)))}"

class CheckoutSimulation:
    def __init__(self):
        self.lanes = []

    def generate_lane(self, lane_type, capacity):
        lane = CheckoutLane(lane_type, capacity)
        self.lanes.append(lane)

    def add_customer_to_lane(self, customer, basket_size):
        for lane in self.lanes:
            if lane.status == 'closed':
                lane.open()

            if lane.add_customer(customer):
                return

        # If no lane is available, open a new one
        self.generate_lane(f"L{len(self.lanes) + 1}", capacity=10)
        self.add_customer_to_lane(customer, basket_size)

    def remove_customer_from_lane(self, customer):
        for lane in self.lanes:
            lane.remove_customer(customer)

    def open_close_lane(self):
        for lane in self.lanes:
            if lane.status == 'open' and len(lane.customers) == 0:
                lane.close()

            if lane.status == 'closed' and len(lane.customers) > 0:
                lane.open()

    def display_lane_status(self, timestamp):
        total_customers = sum(len(lane.customers) for lane in self.lanes)
        print(f"### Lane status at {timestamp} ###")
        print(f"Total number of customers waiting to check out at {timestamp} is: {total_customers}")

        for lane in self.lanes:
            print(lane.display_status())
class Customer:
    def __init__(self, identifier):
        self.identifier = identifier
        self.basket_size = random.randint(1, 30)

    def get_basket_size(self):
        return self.basket_size

    def get_checkout_time(self, is_self_service):
        processing_time_constant = 6 if is_self_service else 4
        return self.basket_size * processing_time_constant

    def award_lottery_ticket(self):
        return self.basket_size >= 10 and random.choice([True, False])

    def display_customer_details(self, is_self_service):
        lottery_status = "wins a lottery ticket!" if self.award_lottery_ticket() else "hard luck, no lottery ticket this time!"


# Example Usage
simulation = CheckoutSimulation()

# Initial Lanes
simulation.generate_lane("Ll(Reg)", capacity=5)
simulation.generate_lane("L2(Reg)", capacity=5)
simulation.generate_lane("L3(Reg)", capacity=5)
simulation.generate_lane("L4(Reg)", capacity=5)
simulation.generate_lane("LS(Reg)", capacity=5)
simulation.generate_lane("L6(Slf)", capacity=8)

# Start of Simulation
simulation.display_lane_status("00:00")

# Some time during simulation
simulation.add_customer_to_lane("Customer1", basket_size=4)
simulation.add_customer_to_lane("Customer2", basket_size=6)
simulation.add_customer_to_lane("Customer3", basket_size=8)
simulation.add_customer_to_lane("Customer4", basket_size=2)
simulation.add_customer_to_lane("Customer5", basket_size=10)
simulation.add_customer_to_lane("Customer6", basket_size=4)

simulation.open_close_lane()
simulation.display_lane_status("02:30")

checkout_time = self.get_checkout_time(is_self_service)

        print(f"### Customer details###")
        print(f"{self.identifier}-> items in basket: {self.basket_size}, {lottery_status}")
        print(f"time to process basket at {'self-service' if is_self_service else 'cashier'} till: {checkout_time} Secs")

# Example Usage
customer1 = Customer("C1")
customer2 = Customer("C2")

customer1.display_customer_details(is_self_service=False)

