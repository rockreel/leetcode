from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def find_itinerary(start, tickets) -> List[str]:
            if not tickets:
                return [[start]]
                
            for i, t in enumerate(tickets):
                if t[0] != start:
                    continue
                for it in find_itinerary(t[1], tickets[:i]+tickets[i+1:]):
                    return [[start] + it]
            return []
            
        tickets = sorted(tickets)
        return find_itinerary('JFK', tickets)[0]

