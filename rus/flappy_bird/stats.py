class Stats():
    def __init__(self, settings):

        self.settings = settings
        self.reset_stats()
        self.game_active = True

        # Читает рекордный счёт в файле.
        try:
            record = open('record.txt', 'r')
            self.high_score = int(record.read())
            record.close()
        except FileNotFoundError:
            self.high_score = 0

    def reset_stats(self):
        self.bird_lives = self.settings.bird_lives
        self.score = 0
