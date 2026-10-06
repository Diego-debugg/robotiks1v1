# Reporte 1: Brazo planar de 3 eslabones

**Nombre:** TU NOMBRE
**Fecha:** 6 de octubre de 2026

## Objetivo
Dibujar un brazo planar de tres eslabones con transformaciones homogéneas 2D,
mostrando un marco por eslabón, el marco del efector final y el alcance de cada eslabón.

## Parámetros
| Eslabón | Longitud |
|---|---|
| L1 | 5 |
| L2 | 3.5 |
| L3 | 2 |

## Metodología
(Explica con tus palabras: cada marco se obtiene multiplicando el anterior por
transl2(L, 0), que avanza a lo largo del eslabón, y trot2(th), que gira la
siguiente articulación. El origen de cada marco está en la última columna de su
matriz, y ese punto es el centro del círculo del eslabón siguiente.)

## Resultados
### Caso 1: th = (30°, 45°, -30°)
![caso 1](img/Test 1.png)

Posición del efector: x = 6.6502, y = 7.2949

### Caso 2: th = (90°, -60°, 45°)
![caso 2](img/Test 2.png)

Posición del efector: x = 3.5487, y = 8.6819

## Conclusiones
el alcance máximo es 5 + 3.5 + 2 = 10.5, cada círculo
se mueve con la articulación de su eslabón, el efector queda dentro del círculo
del último eslabón, etc.