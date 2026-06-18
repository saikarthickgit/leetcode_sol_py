class Solution:
    def angleClock(self, h: int, m: int) -> float:
         
        h_sec=(h*30)+m*.5  #12*30=360 + 180
        print("hour",h_sec)

        m_sec=m*6
        print("min",m_sec)
       
        return min(360-abs(h_sec-m_sec),abs(h_sec-m_sec))
        


        '''
        3-4--> 5 spaces --> 12 min=each space->30deg(1 dis-6 min)
        720
        1 min=60 sec
        1hr =60 min=3600sec

        180
        '''


        