from .DemandProba import (
    Ranges_Demand_Fair,
    Ranges_Demand_Good,
    Ranges_Demand_Poor,
)

# from NTProb import CUMULATIVE_PROB, RANGES
from .type import NT


class NewsDialerSim:
    def __init__(self, Random_Numbers: str):
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

        self.Random_Numbers = Random_Numbers
        # prepare RNforNT and RNforDemand
        pairs = [
            self.Random_Numbers[i : i + 2]
            for i in range(0, len(self.Random_Numbers), 2)
        ]
        for i, pair in enumerate(pairs):
            if len(pair) < 2:
                continue
            if i % 2 == 0:
                self.RNforNT.append(int(pair))
            else:
                self.RNforDemand.append(int(pair))

    def simulate(self, iterations: int):
        # start the simulation
        for i in range(iterations):
            self.Day.append(i + 1)

            # determine News Type : => remember that the right way is to use the computed ranges
            if self.RNforNT[i] < 35:
                self.NewsType.append(NT.Good)
            elif self.RNforNT[i] < 80:
                self.NewsType.append(NT.Fair)
            else:
                self.NewsType.append(NT.Poor)

            # determine Demand
            if self.NewsType[i] == NT.Good:
                demand_ranges = Ranges_Demand_Good
            elif self.NewsType[i] == NT.Fair:
                demand_ranges = Ranges_Demand_Fair
            else:
                demand_ranges = Ranges_Demand_Poor

            for j, (demand, (lower, upper)) in enumerate(demand_ranges.items()):
                if lower <= self.RNforDemand[i] <= upper:
                    self.Demand.append(demand)
                    break

            # calculate Revenue from Sales
            actual_sales = min(self.Demand[i], 70)
            self.RevenuefromSales.append(actual_sales * 0.50)
            # calculate Lost Profit
            if self.Demand[i] > 70:
                self.LostProfit.append((self.Demand[i] - 70) * (0.50 - 0.33))
            else:
                self.LostProfit.append(0)

            # calculate Scrap Revenue
            if self.Demand[i] < 70:
                self.ScrapRevenue.append((70 - self.Demand[i]) * 0.05)
            else:
                self.ScrapRevenue.append(0)

            # calculate Daily Profit
            daily_profit = (
                self.RevenuefromSales[i]
                + self.ScrapRevenue[i]
                - self.CostofNPs
                - self.LostProfit[i]
            )
            self.DailyProfit.append(daily_profit)
        # print the results

    def save_results(self,file_path:str):
        import pandas as pd
        data = {
            "Day": self.Day,
            "RN for NT": self.RNforNT[: len(self.Day) ],
            "News Type": [nt.name for nt in self.NewsType],
            "RN for Demand": self.RNforDemand[: len(self.Day)],
            "Demand": self.Demand,
            "Revenue from Sales": self.RevenuefromSales,
            "Lost Profit": self.LostProfit,
            "Scrap Revenue": self.ScrapRevenue,
            "Daily Profit": self.DailyProfit,
        }
        df = pd.DataFrame(data)
        df.to_csv(file_path , index=False)
