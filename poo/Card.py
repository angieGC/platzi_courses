from payment import Payment

class Card(Payment):
    numberCard = int
    dateCard = str
    cvv = str

    def __init__(self, id, numberCard, dateCard, cvv):
      super.__init__(id)
      self.numberCard = numberCard
      self.dateCard = dateCard
      self.cvv = cvv
     