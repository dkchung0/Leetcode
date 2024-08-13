from typing import Optional,List

class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.pop(0)

        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)




if __name__== '__main__':
    
    # Input
    # ["RecentCounter", "ping", "ping", "ping", "ping"]
    # [[], [1], [100], [3001], [3002]]
    # Output
    # [null, 1, 2, 3, 3]
    
    recent_counter = RecentCounter()
    for i in [1,100,3001,3002]:
        print(recent_counter.ping(i))
    # RecentCounter recentCounter = new RecentCounter();
    # recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
    # recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
    # recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
    # recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3