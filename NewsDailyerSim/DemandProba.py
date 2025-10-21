demand_good = {40: 0.03, 50: 0.05, 60: 0.15, 70: 0.20, 80: 0.35, 90: 0.15, 100: 0.07}
demand_fair = {40: 0.10, 50: 0.18, 60: 0.40, 70: 0.20, 80: 0.08, 90: 0.04, 100: 0.00}
demand_poor = {40: 0.44, 50: 0.22, 60: 0.16, 70: 0.12, 80: 0.06, 90: 0.00, 100: 0.00}


def get_cumulative_prob(demand_prob: dict[int, float]) -> dict[int, float]:
    cumulative_prob = {}
    cumulative = 0.0
    for demand in sorted(demand_prob.keys()):
        cumulative += demand_prob[demand]
        cumulative_prob[demand] = cumulative
    return cumulative_prob


def get_ranges(cumulative_prob: dict[int, float]) -> dict[int, tuple[int, int]]:
    ranges = {}
    lower_bound = 1
    for demand in sorted(cumulative_prob.keys()):
        upper_bound = int(cumulative_prob[demand] * 100)
        # check if lower_bound or upper_bound > 100
        if upper_bound > 100 or lower_bound > 100:
            ranges[demand] = (0, 0)
        else:
            ranges[demand] = (lower_bound, upper_bound)
        lower_bound = upper_bound + 1
    return ranges


Cumulative_Prob_Demand_Good = get_cumulative_prob(demand_good)
Cumulative_Prob_Demand_Fair = get_cumulative_prob(demand_fair)
Cumulative_Prob_Demand_Poor = get_cumulative_prob(demand_poor)
Ranges_Demand_Good = get_ranges(Cumulative_Prob_Demand_Good)
Ranges_Demand_Fair = get_ranges(Cumulative_Prob_Demand_Fair)
Ranges_Demand_Poor = get_ranges(Cumulative_Prob_Demand_Poor)
