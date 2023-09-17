class Solution:
    def DFS(self, origins: dict[str, str], currentAirport: str):
        # If there are no more tickets, return path
        if list(origins.values()) == [[]] * len(origins):
            return [currentAirport]
        
        # If the destination is a dead end, return None
        if currentAirport not in origins.keys() or origins[currentAirport] == []:
            return 'dead end'

        # If there are more tickets, check for paths
        destinations = sorted(origins[currentAirport])
        i = 0
        while i < len(destinations):
            origins[currentAirport].remove(destinations[i])
            path = self.DFS(origins, destinations[i])

            if path == 'dead end':
                origins[currentAirport].append(destinations[i])

            if isinstance(path, list):
                return [currentAirport] + path
            
            i += 1

        # If no path was found, return None
        return 'dead end'

    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # Organise tickets into dictionary for easy lookup
        origins = {}
        for ticket in tickets:
            # If airport is already registered as a origin, add destination
            if ticket[0] in origins.keys():
                origins[ticket[0]].append(ticket[1])
                continue
            # If airport isn't regisered yet, add it
            origins[ticket[0]] = [ticket[1]]

        # Run a DFS search through origins, prioritise lexically first airports when multiple destinations aviable, guarantees that first found path is also lexically first
        return self.DFS(origins, 'JFK')