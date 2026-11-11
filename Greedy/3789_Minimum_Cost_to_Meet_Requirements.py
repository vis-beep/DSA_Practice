
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int,
                    need1: int, need2: int) -> int:

        common = min(need1, need2)

        # Buy common requirements using type 3 items
        cost = common * min(costBoth, cost1 + cost2)

        # Buy remaining requirements individually
        if need1 > need2:
            cost += (need1 - need2) * min(cost1, costBoth)
        else:
            cost += (need2 - need1) * min(cost2, costBoth)

        return cost
