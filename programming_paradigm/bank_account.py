class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance (default is 0)."""
        self.account_balance = initial_balance
        
        def deposit(self, amount):
            """Add money to the account balance."""
            self.account_balance += amount

            def withdraw(self, amount):
                """
                Withdraw money if enough funds are available.

                """

                if amount <= self.account_balance:
                    self.account_balance -= amount
                    return True
                else:
                    return False
                
                def display_balance(self):
                    """Print the current account balance."""

                    print(f"Current Balance: ${self.account_balance:.2f}")

        