class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # def need a dict
        flights = {}
        for fr, to in tickets:
            flights[fr] = flights.get(fr, [])
            flights[fr].append(to)
        print(flights)

        path = []
        stack = ["JFK"]

        while stack:
            popped = stack[-1]

            if popped in flights and flights[popped]:
                minimum = min(flights[popped])
                flights[popped].remove(minimum)
                stack.append(minimum)
            else:
                path.append(stack.pop())

        return path[::-1]

