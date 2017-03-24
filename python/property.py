class User(object):
    '''dhasjfhsadfhsf'''
    @property
    def score(self):
        return self.score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('integer')
        if value <0 or value >100:
            raise ValueError('0~100')
        self.score = value
