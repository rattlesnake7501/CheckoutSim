import random
class CheckoutLane:
    def __init__(self, lane_type, status, timestamp):
        self.lane_type = lane_type  # 'regular' or 'self-service'
        self.status = status  # 'opened' or 'closed'
        self.timestamp = timestamp  # Timestamp when the lane was created
        self.customers = []  # List to store customer objects in the lane

    def add_customer(self, customer):
        """Add a customer to the lane."""
        self.customers.append(customer)
        print(f"Customer {customer.identifier} added to {self.lane_type} lane.")

    def remove_customer(self, customer):
        """Remove a customer from the lane."""

        self.customers.remove(customer)
        print(f"Customer {customer.identifier} removed from {self.lane_type} lane.")
    def open_lane(self):
        """Open the lane if it is closed."""
        if self.status == 'closed':
            self.status = 'opened'
            print(f"{self.lane_type.capitalize()} lane is now open.")

    def close_lane(self):
        """Close the lane if there are no customers."""
        if not self.customers:
            self.status = 'closed'
            print(f"{self.lane_type.capitalize()} lane is now closed.")
        else:
            print(f"Cannot close {self.lane_type} lane. Customers still in the lane.")

    def display_status(self):
        """Display the status of the lane."""
        customer_symbols = '*' * len(self.customers)
        print(f"{self.lane_type.capitalize()} Lane ({self.status}): {customer_symbols}")

    @classmethod
    def customer_add(cls):
        pass


class Customer:
    def __init__(self, identifier, items_in_basket):
        self.identifier = identifier
        self.items_in_basket = items_in_basket

    def get_basket_items(self):
        """Return the number of items in the customer's basket."""
        return self.items_in_basket

    def get_checkout_time(self, lane_type):
        """Calculate the time needed to process a customer's basket based on the number of items and lane type."""
        checkout_time_constant = 4  # Fixed time at cashier tills (in seconds)
        self_service_checkout_time_constant = 6  # Fixed time at self-service tills (in seconds)

        if lane_type == 'regular':
            return self.items_in_basket * checkout_time_constant
        elif lane_type == 'self-service':
            return self.items_in_basket * self_service_checkout_time_constant
        else:
            raise ValueError("Invalid lane type.")

    def award_lottery_ticket(self):
        """Randomly award a lottery ticket if the customer has at least 10 items in their basket."""
        if self.items_in_basket >= 10 and random.choice([True, False]):
            print(f"Lucky customer {self.identifier} wins a lottery ticket!")

    def display_details(self, lane_type):
        """Display details about the customer, including identifier, items in basket, lottery status, and checkout time."""
        lottery_status = "wins a lottery ticket!" if self.items_in_basket >= 10 and random.choice([True, False]) else "hard luck, no lottery ticket this time!"

        print(f"Customer {self.identifier} -> Items in basket: {self.items_in_basket}, {lottery_status}")
        print(f"Time to process basket at {lane_type} till: {self.get_checkout_time(lane_type)} Secs")

