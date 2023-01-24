import saving_stat
import window_stages
import game


class Window(window_stages.Menu,
             window_stages.Help,
             window_stages.Options,
             window_stages.LeaderBoard,
             window_stages.MapMenu,
             window_stages.AngkorWatMiniMap,
             window_stages.BavariaMiniMap,
             window_stages.TibetMiniMap,
             window_stages.Shop,
             game.Game):
    """
    Main window class.
    """

    def __init__(self) -> None:
        """
        Initialization.
        """
        window_stages.Menu.__init__(self)
        self.prices_and_hp = (500, 5), (1000, 20), (2000, 80), (4000, 320)
        self.lives, self.amount_of_diamonds, self.available_levels = saving_stat.get_stat()
        self.info = [1, 2, 2]
        if self.available_levels == 3:
            self.info[0] = 0
        self.max_amount_of_diamonds_per_map = (21, 20, 37)
        if self.lives == 0:
            self.amount_of_options = 5
        else:
            self.amount_of_options = 6
        self.run()

    def run(self) -> None:
        """
        Runs the window.
        """
        ans = self.show_menu(self.amount_of_options)
        extra = ()
        while True:
            if ans == 0:
                self.terminate()
            elif ans == 1:
                ans = self.show_help()
            elif ans == 2:
                ans = self.show_options()
            elif ans == 3:
                ans = self.show_leaderboard()
            elif ans == 4:
                self.available_levels = 0
                self.amount_of_diamonds = 0
                self.amount_of_options = 6
                self.lives = 1
                self.info[0] = 1
                saving_stat.save_stat(self.lives, self.amount_of_diamonds, self.available_levels)
                ans = self.show_mapmenu(*self.info)
            elif ans == 5:
                ans = self.show_mapmenu(*self.info)
            elif ans == 6:
                ans = self.show_menu(self.amount_of_options)
            elif ans == 7:
                ans, *extra = self.run_angkor_wat()
            elif ans == 8:
                ans, *extra = self.run_bavaria()
            elif ans == 9:
                ans, *extra = self.run_tibet()
            elif ans == 10:
                ans = self.run_shop()
            elif ans == 11:
                ans, *extra = self.run_game(*extra)
