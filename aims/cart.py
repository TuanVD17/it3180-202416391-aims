class Cart:
    MAX_NUMBERS_ORDERED = 20

    def __init__(self):
        self.items = []

    def add_digital_video_disc(self, disc):
        if len(self.items) > self.MAX_NUMBERS_ORDERED:
            print("The cart is full.")
            return False
        self.items.append(disc)
        return True

    def remove_digital_video_disc(self, disc):
        if disc in self.items:
            self.items.remove(disc)
            return True
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items)
