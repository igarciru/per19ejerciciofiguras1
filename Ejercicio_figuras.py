class figura:
    def __init__(self):
        pass

    def dame_area(self):
        return print("Esta figura no tiene area")

    def dame_perimetro(self):
        return print("Esta figura no tiene perímetro")

class cuadrado(figura):
    def __init__(self,lado):
        self.lado=lado
        super().__init__()

    def dame_perimetro(self):
        perimetro = 4 * self.lado
        return perimetro
    def dame_area(self):
        area = self.lado**2
        return area


class rectangulo(figura):
    def __init__(self,largo,ancho):
        self.largo=largo
        self.ancho=ancho
        super().__init__()

    def dame_area:
        area=self.largo*self.ancho
        return area
    def dame_perimetro:
        perimetro=2*self.largo+2*self.ancho
        return perimetro

class circulo(figura):
    def __init__(self,radio):
        self.radio=radio
        super().__init__()

    def dame_area(self):
        area=math.pi*(self.radio**2)
        return area
    def dame_perimetro(self):
        perimetro=2*math.pi*self.radio
        return perimetro
