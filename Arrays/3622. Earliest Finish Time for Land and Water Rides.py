from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        min_land_finish = min(
            start + duration
            for start, duration in zip(landStartTime, landDuration)
        )

        min_water_finish = min(
            start + duration
            for start, duration in zip(waterStartTime, waterDuration)
        )

        answer = float("inf")

        # Land -> Water
        for start, duration in zip(waterStartTime, waterDuration):
            answer = min(
                answer,
                max(min_land_finish, start) + duration
            )

        # Water -> Land
        for start, duration in zip(landStartTime, landDuration):
            answer = min(
                answer,
                max(min_water_finish, start) + duration
            )

        return answer
