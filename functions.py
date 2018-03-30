class space():
    def __init__(self,wf,hf,df):
        self.wf = wf
        self.hf = hf
        self.df = df
    def arnf(self):
        '''Area in squared feet'''
        r = self.wf * self.df
        return r
    def arnm(self):
        '''Area in squared meters'''
        r = self.arnf() * 0.092903
        return r
