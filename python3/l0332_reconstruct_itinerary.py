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

    def findItineraryGlobalResult(self, tickets: List[List[str]]) -> List[str]:
        
        def itinerary(tickets, itr, used, result):
            if len(itr) == len(tickets) + 1:
                result.append(itr)
                return True
            for i in range(len(tickets)):
                if i in used:
                    continue
                if tickets[i][0] == itr[-1]:    
                    used.add(i)
                    if itinerary(tickets, itr + [tickets[i][1]], used, result):
                        return True
                    used.remove(i)
            return False
        
        result = []
        itinerary(sorted(tickets), ['JFK'], set([]), result)
        return result[0]

