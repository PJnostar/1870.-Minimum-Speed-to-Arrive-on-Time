import math

class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        n = len(dist)
        if (n-1 >= hour): return -1     #   warunek nieistnienia prędkości, dla której da się dojechac na czas
                                        #   czyli ilość stacji jest większa niz ilość godzin (minus jedna-ostatnia
                                        #   stacja, bo po niej nie trzeba czekac do pelnej godziny)

        def time(speed):                #   liczy czas pokonania calej trasy dla predkosci speed
            t=0
            for i in dist[:n-1]:
                t += math.ceil(i/speed)
            t += dist[n-1]/speed
            return t
        
        minspeed = 1
        maxspeed = pow(10,7)
        while(minspeed<=maxspeed):
            midspeed = math.floor((minspeed+maxspeed)/2.)
            print(minspeed, maxspeed, midspeed)
            time_total = time(midspeed)
            if (time_total <= hour):
                maxspeed = midspeed-1
                bestMinSpeed = midspeed
            else:
                minspeed = midspeed+1
                # bestMinSpeed = maxspeed

        print(bestMinSpeed)
        return int(bestMinSpeed)