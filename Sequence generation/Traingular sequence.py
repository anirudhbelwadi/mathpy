class Mathematics :
    def __init__(self,n):
        self.n=int(n);
    def triang(self):
        i=1;
        while i<(self.n+1.0):
            t=(i*(i+1))/2;
            if i!=self.n:
                print(t,end=", ");
                i=i+1;
            else:
                print(t);
                return;
