"""A small interactive restaurant ordering CLI."""

from dataclasses import dataclass


MENU = {
    "1": {"name": "Jollof Rice", "price": 45.00, "category": "Main"},
    "2": {"name": "Fried Rice", "price": 48.00, "category": "Main"},
    "3": {"name": "Waakye", "price": 40.00, "category": "Main"},
    "4": {"name": "Chicken Sandwich", "price": 35.00, "category": "Quick Bites"},
    "5": {"name": " kelewele", "price": 20.00, "category": "Sides"},
    "6": {"name": "Fresh Sobolo", "price": 12.00, "category": "Drinks"},
    "7": {"name": "Mango Juice", "price": 15.00, "category": "Drinks"},
}


@dataclass
class MenuItem:
    """Represents one item available to order."""

    name: str
    price: float
    category: str


class Restaurant:
    """Stores menu data and manages a customer's basket."""

    def __init__(self, name: str, menu: dict[str, dict]):
        self.name = name
        self.menu = menu
        self.cart: dict[str, int] = {}

    def get_item(self, item_id: str) -> MenuItem | None:
        details = self.menu.get(item_id)
        if details is None:
            return None
        return MenuItem(
            name=details["name"].strip(),
            price=details["price"],
            category=details["category"],
        )

    def add_to_cart(self, item_id: str, quantity: int = 1) -> bool:
        if self.get_item(item_id) is None or quantity < 1:
            return False
        self.cart[item_id] = self.cart.get(item_id, 0) + quantity
        return True

    def remove_from_cart(self, item_id: str) -> bool:
        if item_id not in self.cart:
            return False
        del self.cart[item_id]
        return True

    def subtotal(self) -> float:
        return sum(
            self.menu[item_id]["price"] * quantity
            for item_id, quantity in self.cart.items()
        )

    def item_count(self) -> int:
        return sum(self.cart.values())

    def clear_cart(self) -> None:
        self.cart.clear()


def money(amount: float) -> str:
    """Format a price in Ghana cedis."""
    return f"GH₵{amount:.2f}"


def show_menu(restaurant: Restaurant) -> None:
    print("\nTODAY'S MENU")
    print("-" * 43)
    for item_id, details in restaurant.menu.items():
        print(
            f"{item_id}. {details['name'].strip():<22} "
            f"{money(details['price']):>10}  [{details['category']}]"
        )
    print("-" * 43)


def show_cart(restaurant: Restaurant) -> None:
    if not restaurant.cart:
        print("\nYour basket is empty. Add something delicious!")
        return

    print("\nYOUR BASKET")
    print("-" * 43)
    for item_id, quantity in restaurant.cart.items():
        item = restaurant.get_item(item_id)
        if item:
            line_total = item.price * quantity
            print(
                f"{item.name:<22} x{quantity:<3} "
                f"{money(line_total):>10}"
            )
    print("-" * 43)
    print(f"Subtotal: {money(restaurant.subtotal())}")
    print(f"Items:    {restaurant.item_count()}")


def read_quantity(prompt: str = "Quantity: ") -> int:
    while True:
        raw_value = input(prompt).strip()
        try:
            quantity = int(raw_value)
            if quantity > 0:
                return quantity
        except ValueError:
            pass
        print("Enter a whole number greater than zero.")


def checkout(restaurant: Restaurant) -> None:
    if not restaurant.cart:
        print("\nYour basket is empty. Add an item before checkout.")
        return

    show_cart(restaurant)
    print("\nORDER CONFIRMED!")
    print(f"Thank you for ordering from {restaurant.name}.")
    print(f"Your total is {money(restaurant.subtotal())}.")
    print("Your food adventure starts now!")
    restaurant.clear_cart()


def run_app() -> None:
    restaurant = Restaurant("Meals To Go", MENU)
    print("\n" + "=" * 43)
    print("       WELCOME TO MEALS TO GO")
    print("        Good food. Good mood.")
    print("=" * 43)

    while True:
        print("\nWhat would you like to do?")
        print("1. Browse menu")
        print("2. Add food to basket")
        print("3. View basket")
        print("4. Remove an item")
        print("5. Checkout")
        print("0. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            show_menu(restaurant)
        elif choice == "2":
            show_menu(restaurant)
            item_id = input("\nEnter the item number: ").strip()
            quantity = read_quantity()
            if restaurant.add_to_cart(item_id, quantity):
                item = restaurant.get_item(item_id)
                print(f"Added {quantity} x {item.name} to your basket!")
            else:
                print("That menu number is not valid.")
        elif choice == "3":
            show_cart(restaurant)
        elif choice == "4":
            show_cart(restaurant)
            if restaurant.cart:
                item_id = input("Enter the menu number to remove: ").strip()
                if restaurant.remove_from_cart(item_id):
                    print("Item removed from your basket.")
                else:
                    print("That item is not in your basket.")
        elif choice == "5":
            checkout(restaurant)
        elif choice == "0":
            print("\nThanks for stopping by. Come hungry, leave happy!")
            break
        else:
            print("Please choose one of the options shown.")


if __name__ == "__main__":
    run_app()
