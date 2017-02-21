class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def generate_itinerary(start, dest_map, itinerary, stops_to_go):
            if stops_to_go == 0:
                # Find the final destination.
                itinerary.append(start)
                return True
            if not dest_map[start]:
                return False
            itinerary.append(start)
            for i, dest in enumerate(dest_map[start]):
                dest_map[start].pop(i)
                if generate_itinerary(dest, dest_map, itinerary, stops_to_go-1):
                    return True
                dest_map[start].insert(i, dest)
            itinerary.pop()
            return False
        
        import bisect
        from collections import defaultdict
        dest_map = defaultdict(list)
        for t in tickets:
            bisect.insort_left(dest_map[t[0]], t[1])
        itinerary = []
        generate_itinerary('JFK', dest_map, itinerary, len(tickets))
        return itinerary

