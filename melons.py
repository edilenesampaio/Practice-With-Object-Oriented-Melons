""""Classes for melon orders."""


class DomesticMelonOrder:
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder:
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        # christmas_base = base_price * 1.5
        if self.species == "Christmas melon":
            total = (1 + self.tax) * self.qty * base_price * 1.5
        if self.order_type == "international" and self.qty < 10: 
            total += 3
                    
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class AbstractMelonOrder:

    # order_type = None
    # tax = 0
    
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty

class InternationalMelonOrder(AbstractMelonOrder):

    order_type = "international"
    tax = 0.17
    
    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code

    
class GovernmentMelonOrder(AbstractMelonOrder):
    """Create a class GovernmentMelonOrder that inherits from 
    AbstractMelonOrder. There will be no tax on government orders. 
    The GovernmentMelonOrder class should include:
    - a variable passed_inspection which is False until a 
    successful inspection occurs.
    - a method mark_inspection(passed) that takes a Boolean input, 
    passed, and updates whether or not the melon has passed inspection. 
    This method should update the attribute passed_inspection."""

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False

    
    def mark_inspection(self, passed):
        self.passed_inspection = passed