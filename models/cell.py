class Cell:
    """
    Class to represent every cell in board
    - region
    - owner:
        0 if empty, 1 for player1 and 2 for player2
    """

    def __init__(self, owner, region):
        """ Constructor """
        self.owner = owner
        self.region = region

    def set_owner(self, owner):
        self.owner = owner
    
    def set_region(self, region):
        self.region = region

    def __str__(self):
        return f"{self.owner}"
