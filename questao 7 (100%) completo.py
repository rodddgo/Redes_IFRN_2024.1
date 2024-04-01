import math

print('Insira a seguir, o valor dos 3 lados do triângulo a ser calculado.')
ld1 = float(input('Insira o comprimento do lado A do triângulo: '))
ld2 = float(input('Insira o comprimento do lado B do triângulo: '))
ld3 = float(input('Insira o comprimento do lado C do triângulo: '))

if ld1 < ld2 + ld3 and ld2 < ld1 + ld3 and ld3 < ld2 + ld1:
  print('=-='*20)
  print('O triângulo pode ser formado!')
    
  if ld1 == ld2 == ld3: 
    print('O triângulo é equilátero.')
  elif ld1 != ld2 != ld3 != ld1:
    print('O triângulo é escaleno.')
  elif ld1 == ld2 or ld2 == ld3 or ld1 == ld3:
    print('O triângulo é isósceles.')
else:
  print('O triângulo nâo pode ser formado!')   

cos_a = math.degrees(math.acos((math.pow(ld2, 2) + math.pow(ld3, 2) - math.pow(ld1, 2))/(2 * ld2 * ld3)))
cos_b = math.degrees(math.acos((math.pow(ld1, 2) + math.pow(ld3, 2) - math.pow(ld2, 2)) / (2 * ld1 * ld3)))
cos_c = math.degrees(math.acos((math.pow(ld1, 2) + math.pow(ld2, 2) - math.pow(ld3, 2)) / (2 * ld2 * ld1)))
if cos_a == 180 or cos_b == 180 or cos_c == 180:
    print('O triângulo nâo pode ser formado!')

else:
  if cos_a> 90 or cos_b > 90 or cos_c > 90:
    print('O triângulo tem ângulo obtuso.')
  elif cos_a == 90 or cos_b == 90 or cos_c == 90:
    print('O triângulo tem ângulo reto.')
  else:
    print('O triângulo tem ângulo agudo.')
    
  print(f'O Cos de A tem um ângulo de: {cos_a:.2f}° graus.')
  print(f'O Cos de B tem um ângulo de: {cos_b:.2f}° graus.')
  print(f'O Cos de C tem um ângulo de: {cos_c:.2f}° graus.')







