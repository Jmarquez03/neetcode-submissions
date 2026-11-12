class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        cars = {}
        # If there is at least one car, there is at least one fleet. 
        fleets = 0        
        for i in range(len(position)):
            cars[position[i]] = speed[i]
        sortedPositions = sorted(position)
        timeToTarget = 0.0
        while sortedPositions:
            position = sortedPositions.pop()
            # Time to reach target (in hours)
            t = float(target - position)/float(cars[position]) 
            # How to check if the car belongs to a fleet?
            # idea: if t <= time to target
            if t <= timeToTarget:
                continue
            else:
                fleets += 1
                timeToTarget = t
        return fleets