

class GameStats():
    """Tracking the game statistics"""
    
    def __init__(self, aw_settings):
        self.aw_settings = aw_settings
        self.game_state = True
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.aw_settings.ship_limit
