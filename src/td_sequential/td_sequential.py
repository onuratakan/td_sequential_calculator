
class tds:
  def __init__(self):
    self.td_seq_setup_6_price = 0
    self.td_seq_setup_7_price = 0
    self.td_seq_setup_8_price = 0
    self.lower_price_of_9 = 0
    self.sell_lower_price_of_9 = 0
 
 
    self.td_seq_buy_setup = 0
    self.td_seq_sell_setup = 0
 
 
    self.local_price_history = [0,0,0,0,0,0,0,0,0]
    self.td_seq_buy = False
    self.td_seq_sell = False
   
  def price_update(self, price):
    if len(self.local_price_history) == 9:
      del self.local_price_history[0]
  
  
    self.local_price_history.append(price)

    if self.td_seq_buy_setup == 9:

          self.td_seq_buy_setup = 0
          self.td_seq_buy = False
    elif self.td_seq_sell_setup == 9:
          self.td_seq_sell_setup = 0
          self.td_seq_sell = False


    if not self.local_price_history[5] == 0:

      if price > self.local_price_history[5]:


        self.td_seq_buy_setup += 1
        self.td_seq_sell_setup = 0

        if self.td_seq_buy_setup == 6:
          self.td_seq_setup_6_price = price
        if self.td_seq_buy_setup == 7:
          self.td_seq_setup_7_price = price
        if self.td_seq_buy_setup == 8:
          self.td_seq_setup_8_price = price
  
        if self.td_seq_buy_setup == 9:
          self.lower_price_of_9 = price
          if self.lower_price_of_9 > self.td_seq_setup_6_price and self.lower_price_of_9 > self.td_seq_setup_7_price or self.td_seq_setup_8_price > self.td_seq_setup_6_price and self.td_seq_setup_8_price > self.td_seq_setup_7_price:
            self.td_seq_buy = True

      elif price < self.local_price_history[5] : #SELL Setup

        self.td_seq_sell_setup += 1
        self.td_seq_buy_setup = 0
        if self.td_seq_sell_setup == 6:
          self.td_seq_sell_setup_6_price = price
        if self.td_seq_sell_setup == 7:
          self.td_seq_sell_setup_7_price = price
        if self.td_seq_sell_setup == 8:
          self.td_seq_sell_setup_8_price = price
  
        if self.td_seq_sell_setup == 9:
          self.sell_lower_price_of_9 = price
          if self.sell_lower_price_of_9 < self.td_seq_setup_6_price and self.sell_lower_price_of_9 < self.td_seq_setup_7_price or self.td_seq_setup_8_price < self.td_seq_setup_6_price and self.td_seq_setup_8_price < self.td_seq_setup_7_price:
            self.td_seq_sell = True
          
  
  
      elif price == self.local_price_history[5]:
        self.td_seq_buy_setup = 0
        self.td_seq_sell_setup = 0
  
    
    return self.td_seq_buy_setup, self.td_seq_sell_setup, self.td_seq_buy, self.td_seq_sell


TDS = tds()