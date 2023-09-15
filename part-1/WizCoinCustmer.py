import wizCoin


class WizCoinCustomer:
    def __init__(self, name):
        self.name = name
        self.purse = wizCoin.WizCoin(0, 0, 0)
