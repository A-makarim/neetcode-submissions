class Solution:

    

    def encode(self, strs: List[str]) -> str:
        self.q = []
        self.s = []
        self.s1 = ""
        for i,n in enumerate(strs):
            print(len(n))
            self.q.append(len(n) + (self.q[-1] if self.q else 0))

            self.s1 = self.s1 + n
        return self.s1

        print(self.q)
        print(self.s1)

        


    def decode(self, s: str) -> List[str]:
        for i in range(len(self.q)):
            self.s.append(self.s1[0 if i==0 else self.q[i-1]: self.q[i]])

        print(self.s1)
        print(self.q)
        print(self.s1[3:8])

        return self.s