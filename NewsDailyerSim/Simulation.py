from DemandProba import (
    Cumulative_Prob_Demand_Fair,
    Cumulative_Prob_Demand_Good,
    Cumulative_Prob_Demand_Poor,
    Ranges_Demand_Fair,
    Ranges_Demand_Good,
    Ranges_Demand_Poor,
)
from NTProb import CUMULATIVE_PROB, RANGES
from type import NT


class NewsDialerSim:
    def __init__(self):
        self.Day = []

        self.RNforNT = []

        self.NewsType = []

        self.RNforDemand = []

        self.Demand = []

        self.RevenuefromSales = []

        self.CostofNPs = 70 * 0.33

        self.LostProfit = []

        self.ScrapRevenue = []

        self.DailyProfit = []

    def simulate(iterations: int):
        pass
