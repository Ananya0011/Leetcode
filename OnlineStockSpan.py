class StockSpanner(object):

    def __init__(self):
        self.prices=[]
        self.stack=[]
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.prices.append(price)
        today=len(self.prices)-1
        span=0
        if not self.stack:
            span=1
        else:
            while self.stack and price>=self.prices[self.stack[-1]]:
                self.stack.pop()
            if self.stack:
                span=(today-self.stack[-1])
            else:
                span=today+1
        self.stack.append(today)
        return span
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

##########optimized code###############
#class StockSpanner(object):

 #   def __init__(self):
  #      self.stack = []          # (price, span)

   # def next(self, price):
    #    span = 1

     #   while self.stack and price >= self.stack[-1][0]:
      #      span += self.stack[-1][1]
       #     self.stack.pop()

        #self.stack.append((price, span))

        #return span
