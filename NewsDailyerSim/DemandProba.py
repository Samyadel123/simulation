from type import NT
from util import get_ranges, get_comulative_prob

demand_good = {40: 0.03, 50: 0.05, 60: 0.15, 70: 0.20, 80: 0.35, 90: 0.15, 100: 0.07}
demand_fair = {40: 0.10, 50: 0.18, 60: 0.40, 70: 0.20, 80: 0.08, 90: 0.04, 100: 0.00}
demand_poor = {40: 0.44, 50: 0.22, 60: 0.16, 70: 0.12, 80: 0.06, 90: 0.00, 100: 0.00}

Cumulative_Prob_Demand_Good = get_comulative_prob(demand_good)
Cumulative_Prob_Demand_Fair = get_comulative_prob(demand_fair)
Cumulative_Prob_Demand_Poor = get_comulative_prob(demand_poor)
Ranges_Demand_Good = get_ranges(Cumulative_Prob_Demand_Good)
Ranges_Demand_Fair = get_ranges(Cumulative_Prob_Demand_Fair)
Ranges_Demand_Poor = get_ranges(Cumulative_Prob_Demand_Poor)
