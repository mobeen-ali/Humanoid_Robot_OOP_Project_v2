class Battery:
    """
        A class to represent the battery of a humanoid robot,
        handling charge monitoring and recharging.
    """

    def __init__(self, max_charge=100):
        """
        Initialize the battery with a maximum charge.

        Args:
            max_charge (int): Maximum battery level. Default is 100.
        """
        self.max_charge = max_charge
        self.charge = max_charge

    def check_battery(self):
        """
        Return the current battery level as a formatted string.

        Returns:
            str: Battery level percentage.
        """
        return f"Battery level: {self.charge}%"

    def drain(self, amount):
        """
        Drain the battery by a specified amount.

        Args:
            amount (int): The amount of charge to remove.
        """
        self.charge -= amount
        if self.charge < 0:
            self.charge = 0
        print(f"Battery drained by {amount}%. Current level: {self.charge}%")

    def recharge(self):
        """
        Recharge the battery to its full capacity.
        """
        self.charge = self.max_charge
        print("Battery recharged to 100%.")
