class Bolera:
    #Variables Globales  definidas#
    pleno = 10
    nulo = 0
    ultimo_numero = 0
    
    def __init__(self,puntos):
        self.puntos = list(puntos)
    
    @staticmethod
    def sumas_especiales(rolls):
        valor_total = 0
        for roll in rolls:
            if roll.isdigit():
                valor_total += int(roll)
                Bolera.ultimo_numero = int(roll)
            if roll == '-':
                Bolera.ultimo_numero = 0
            if roll == 'X':
                valor_total += Bolera.pleno
            if roll == '/':
                valor_total += (Bolera.pleno - int(Bolera.ultimo_numero))
        return valor_total
    
    def calcular_puntos(self):
        puntuación_final = 0
        cantidad_tiradas = 0
        cantidad_tiradas_frame = 0
        frame = 0
        for numero in self.puntos:
            if frame == 9:
                puntuación_final += Bolera.sumas_especiales(self.puntos[cantidad_tiradas:])
                return puntuación_final
            if numero.isdigit():
                puntuacion_final += int(numero)
                Bolera.ultimo_numero = numero
                if cantidad_tiradas_frame > 0:
                    cantidad_tiradas_frame = 0
                    frame += 1
                else:
                    cantidad_tiradas_frame += 1
                cantidad_tiradas +=1
        #Hasta aquí#