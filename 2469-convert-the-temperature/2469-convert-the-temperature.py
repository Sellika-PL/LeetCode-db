class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        r=[]
        r.append(celsius+273.15)
        r.append(celsius*1.80+32.00)
        return r
        