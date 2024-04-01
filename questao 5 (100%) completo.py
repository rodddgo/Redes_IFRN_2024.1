minutos_permanencia = int(input('informe o tempo de permanencia em minutos, do veiculo: '))
min_p_hrs = minutos_permanencia // 60
f_hora = minutos_permanencia % 60
v_perm = 0

if f_hora > 0:
    min_p_hrs +=1 
if  min_p_hrs <= 2:
    v_perm = 8 * min_p_hrs
elif min_p_hrs <= 4:
    v_perm = 16 + (min_p_hrs - 2) * 5
elif min_p_hrs <= 12:
    v_perm = 26 + (min_p_hrs - 4) * 3
else: 
     v_perm = 30 # valor fixo
print(f'O valor do período de permanência de {minutos_permanencia} minutos ficou: {v_perm:.2f}R$')