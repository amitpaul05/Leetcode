class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r_q = []
        d_q = []

        for i in range(len(senate)):
            if senate[i] == 'R':
                r_q.append(i)
            else:
                d_q.append(i)
            # if r_q and d_q:
            #     if d_q[0] > r_q[0]:
            #         r_q.append(n)
            #         n += 1
            #     elif d_q[0] < r_q[0]:
            #         d_q.append(n)
            #     r_q = r_q[1:]
            #     d_q = d_q[1:]
        while r_q and d_q:
            if d_q[0] > r_q[0]:
                r_q.append(n)
                n += 1
            elif d_q[0] < r_q[0]:
                d_q.append(n)
                n += 1
            r_q = r_q[1:]
            d_q = d_q[1:]
        return 'Radiant' if r_q else 'Dire'
        