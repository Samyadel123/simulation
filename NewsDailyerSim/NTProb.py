from type import NT
from util import get_ranges, get_comulative_prob

TN_PROB = {NT.Good: 0.35, NT.Fair: 0.45, NT.Poor: 0.20}


CUMULATIVE_PROB = get_comulative_prob(TN_PROB=TN_PROB)


RANGES = get_ranges(CUMULATIVE_PROB=CUMULATIVE_PROB)

