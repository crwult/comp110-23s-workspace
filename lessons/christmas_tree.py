class ChristmasTreeFarm():
    plots: list[int]

    def __init__(self, plots: int, initial_planting: int) -> None:
        self.plots = []
        for num in range (0, initial_planting):
            self.plots.append(1)
        for num in range (0, (plots - initial_planting)):
            self.plots.append(0)

    def plant(self, plot_num):
        self.plots[plot_num] = 1

    def growth(self):
        for elem in self.plots:
            if elem > 0:
                elem += 1
    
    def replant(self, is_replanted: bool) -> int:
        harvested: int = 0
        for elem in self.plots:
            if elem > 4:
                harvested += 1
                if is_replanted:
                    elem = 1
                else:
                    elem = 0
        return harvested
    
    def __add__(self, farm2: ChristmasTreeFarm) -> ChristmasTreeFarm:
        
        return 

