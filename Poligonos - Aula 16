from math import pi
class Retangulo():
    
    def __init__(self,a,b):
        self.ladoA = a
        self.ladoB = b
        
    def area(self):
        return round(self.ladoA*self.ladoB,2)
    
    def perimetro(self):
        return round(self.ladoA+self.ladoB,2)
    
class Caixa(Retangulo):
    
    def __init__(self,a,b,h):
        super().__init__(a,b)
        self.altura = h
        
    def arealateral(self):
        a1 = 2*Retangulo(self.ladoA,self.ladoB).area()
        a2 = 2*Retangulo(self.ladoA,self.altura).area()
        a3 = 2*Retangulo(self.ladoB,self.altura).area()
        return round(a1+a2+a3,2)
    
    def volume(self):
        return round(Retangulo(self.ladoA,self.ladoB).area()*self.altura,2)
    

class Circulo():
    def __init__(self,r):
        self.raio = r
        
    def area(self):
        return round(pi*(self.raio**2),2)

    def perimetro(self):
        return round(2*pi*self.raio,2)

class Cilindro(Circulo):
    def __init__(self,r,h):
        super().__init__(r)
        self.altura = h
        
    def arealateral(self):
        return round(self.altura*Circulo(self.raio).perimetro(),2)

    def volume(self):
        return round(Circulo(self.raio).area()*self.altura,2)
    
