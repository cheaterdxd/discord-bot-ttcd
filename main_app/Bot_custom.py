from discord.ext import commands

class Bot_with_javis(commands.Bot):
    """
        Just a custom Commands Bot class.

        Args:
            intents (discord.Intents): The intents to be used by the client.

        Returns:
            None
    """
    javis = None
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def get_javis(self):
    #     return self.javis

    # def set_javis(self, value):
    #     self.javis = value