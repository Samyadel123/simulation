from type import NT


def get_ranges(CUMULATIVE_PROB: dict[NT, float]) -> dict[NT, tuple[int, int]]:
    ranges = {}
    lower_bound = 1
    for nt in NT:
        # upper bound is cumulative probability * 100
        upper_bound = int(CUMULATIVE_PROB[nt] * 100)

        ranges[nt] = (lower_bound, upper_bound)
        # New lower is upper bound + 1
        lower_bound = upper_bound + 1
    return ranges


def get_comulative_prob(TN_PROB: dict[NT, float]) -> dict[NT, float]:
    cumulative_prob = {}
    cumulative = 0.0
    for nt in NT:
        cumulative += TN_PROB[nt]
        cumulative_prob[nt] = cumulative
    return cumulative_prob
