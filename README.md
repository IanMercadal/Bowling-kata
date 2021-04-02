# Bowling-kata
## Objetivos
- Programan un programa que calcula correctamente la puntuación final de la partida al acabar.
## Reglas del negocio
- Cada partida consta de 10 frames.
- Un frame (exceptuando el último frame, del que ya hablaré) consiste en dos intentos o tiradas para tirar todos los pins(bolos). Esto es, para cada frame normal (del primero al noveno) tienes dos tiradas, a menos que tires todos los pins (strike) en la primera, en ese caso la segunda tirada no se lleva a cabo.
- En caso de no tirar todos los pins en un frame, la puntuación de ese frame (que se sumará a la puntuación total) será el número de pins tirados.
- En el caso de tirar todos los pins en la primera tirada del frame, eso se llama strike, y la puntuación de ese frame que será sumada a la puntuación total será de 10 (número de pins tirados) + el número de pins tirados en las dos siguientes tiradas.
- En el caso de tirar todos los pins haciendo uso de las dos tiradas del frame, la puntuación que se sumará será de 10 (número de pins tirados en el frame) + el número de pins tirados en la siguiente tirada.
- El último frame o tenth tiene una lógica distinta.
- Si se ejecuta un spare el jugador tendrá una tirada extra, y la puntuación del frame será de 10 + los pins tirados en la siguiente tirada.
- Si se ejecuta un strike el jugador tendrá dos tiradas extra y la puntuación del frame será de 10 + los pins tirados en las dos siguientes tiradas.
- Este bonus solo puede ocurrir una vez (esto es, da igual que en la tirada extra vuelvas a hacer strike, no tendrás más tiradas extra, simplemente se sumará la puntuación de los 10 bolos tirados al frame.
- La puntuación total de la partida es la suma de las puntuaciones de los frames.

## Colaboración de Victor Porlan Soto
- https://github.com/VictorPorlan
