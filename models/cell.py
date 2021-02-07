class Cell:
    """
    Class to represent every cell in board
    - owner: 
        0 if empty, 1 for player1 and 2 for player2
    """
    def __init__(self, owner):
        """ Cell constructor """
        self.owner = owner

    def set_owner(self, owner):
        self.owner = owner

    def __str__(self):
        print(f'{self.owner}')
