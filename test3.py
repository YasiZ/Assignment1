class Time:
    def __init__(self, h, m, s):
        self.s = s
        self.m = m
        self.h = h


    def sum(self, time2):
        result_h = self.h + time2.h
        result_m = self.m + time2.m
        result_s = self.s + time2.s
        if result_s >= 60:
            result_s -= 60
            result_m += 1

        if result_m >= 60:
            result_m -= 60
            result_h += 1
                
        result = Time(result_h, result_m, result_s)
        return result

    def sub(self, time2):
        if time2.s > self.s:
           self.s += 60
           self.m -= 1

        if time2.m > self.m:
           self.m += 60
           self.h -= 1

        result_subs = self.s - time2.s
        result_subm = self.m - time2.m
        result_subh = self.h - time2.h
        result = Time(result_subh, result_subm, result_subs)
        return result
    
    def time_to_min(self):
        self.h *= 3600
        self.m *= 60
        result = self.h + self.m + self.s
        return result

    def min_to_time(self):
        if self.s >= 60:
           self.m += int(self.s/60)
           self.m %= 60
        result = Time(self.h, self.m, self.s)
        return result
           

    def show(self):
        print(f"{self.h} : {self.m} : {self.s}")

    def gmt_to_teh(self):
        self.h += 3
        self.m += 30

        if self.m >= 60:
            self.m -= 60
            self.h += 1

        result_teh = Time(self.h, self.m, self.s)
        return result_teh    
    

time1 = Time(8, 20, 45)
time1.show()

time2 =  Time(7, 35, 20)
time2.show()

result_sum = time1.sum(time2)
result_sum.show()
