class Cart:
    MAX_NUMBERS_ORDERED = 20

    def __init__(self):
        self.items = []

    def add_digital_video_disc(self, disc):
        if len(self.items) >= self.MAX_NUMBERS_ORDERED:
            print("Gio hang da day! Khong the them dia.")
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

    def total_cost_with_discount(self, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Percent must be between 0 and 100")
        return self.total_cost() * (1 - percent / 100)

    def print_cart(self):
        if not self.items:
            print("The cart is empty")
            return
        print("***********************CART***********************")
        print("Ordered Items:")
        for idx, item in enumerate(self.items, 1):
            print(f"{idx}. DVD - {item.title} - {item.category} - {item.director} - {item.length}: {item.cost} $")
        print(f"Total cost: {self.total_cost():.2f} $")
        print("***************************************************")
