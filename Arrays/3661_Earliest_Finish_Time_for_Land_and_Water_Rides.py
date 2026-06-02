class Solution:
    def earliestFinishTime(
        self,
        landStartTime: list[int],
        landDuration: list[int],
        waterStartTime: list[int],
        waterDuration: list[int]
    ) -> int:
        ans = float('inf')

        for ls, ld in zip(landStartTime, landDuration):
            for ws, wd in zip(waterStartTime, waterDuration):

                # Land -> Water
                land_finish = ls + ld
                water_start = max(ws, land_finish)
                ans = min(ans, water_start + wd)

                # Water -> Land
                water_finish = ws + wd
                land_start = max(ls, water_finish)
                ans = min(ans, land_start + ld)

        return ans
