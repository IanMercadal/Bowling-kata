class Bowls:
    #Variables Globales  definidas#
    strike = 10
    nulo = 0
    spare = 0
    ultimo_numero = 0
    
    def __init__(self,puntos):
        self.puntos = list(puntos)
    
    @staticmethod
    def sumas_especiales(rolls):
        valor_total = 0
        for roll in rolls:
            if roll.isdigit():
                valor_total += int(roll)
                Bowls.ultimo_numero = int(roll)
            if roll == '-':
                Bowls.ultimo_numero = 0
            if roll == 'X':
                valor_total += Bowls.strike
            if roll == '/':
                valor_total += (Bowls.strike - int(Bowls.ultimo_numero))
        return valor_total
    
    def calcular_puntos(self):
        puntuacion_total = 0
        numero_tiradas = 0
        numero_tiradas_frame = 0
        frame = 0
        for numero in self.puntos:
            if frame == 9:
                puntuacion_total += Bowls.sumas_especiales(self.puntos[numero_tiradas:])
                return puntuacion_total
            if numero.isdigit():
                puntuacion_total += int(numero)
                Bowls.ultimo_numero = numero
                if numero_tiradas_frame > 0:
                    numero_tiradas_frame = 0
                    frame += 1
                else:
                    numero_tiradas_frame += 1
                numero_tiradas +=1
            if numero == '-':
                Bowls.ultimo_numero = 0
                if numero_tiradas_frame > 0:
                    numero_tiradas_frame = 0
                    frame += 1
                else:
                    numero_tiradas_frame += 1
                numero_tiradas +=1
            if numero == 'X':
                puntuacion_total += Bowls.sumas_especiales(self.puntos[numero_tiradas: numero_tiradas+3])
                numero_tiradas +=1
                frame += 1
            if numero == '/':
                puntuacion_total += Bowls.sumas_especiales(self.puntos[numero_tiradas: numero_tiradas+2])
                numero_tiradas+=1
                numero_tiradas_frame = 0
                frame += 1