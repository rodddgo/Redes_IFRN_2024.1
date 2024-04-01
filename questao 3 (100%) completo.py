import sys

h_partida,m_partida = input('informe o horario de partida da viagem: ').split(':')
h_part_int = int(h_partida)
m_part_int = int(m_partida) 

h_chegada,m_chegada = input('informe o horario de chegada da viagem: ').split(':')
h_cheg_int = int(h_chegada)
m_cheg_int = int(m_chegada)

mins_part = h_part_int * 60 + m_part_int
mins_cheg = h_cheg_int * 60 + m_cheg_int

dist_viagem = float(input('informe a distancia em km dessa viagem: '))
t_descanso = int(input('informe em minutos quanto tempo houve de descanso: '))
l_gastos = float(input('informe quantos litro de combustivel foram gastos:'))
p_comb = float(input('informe o valor do L do combustivel: '))

consumo_comb = dist_viagem / l_gastos
gasto_viagem = l_gastos * p_comb
rs_km = p_comb / consumo_comb

if dist_viagem and t_descanso and l_gastos and p_comb <= 0:
    sys.exit('insira um valor valido! o programa sera encerrado!')


if h_cheg_int < 0 and h_part_int < 0 or h_part_int > 24 and h_cheg_int > 24:
    sys.exit('erro! digite um horario valido! o programa sera encerrado!')
elif m_cheg_int < 0 and m_part_int < 0 or m_part_int > 60 and m_cheg_int > 60:
    sys.exit('erro! digite um horario valido! o programa sera encerrado!')
else:

    if mins_cheg == mins_part:

        viagem_24h = 86400                                            #ok
        md_veloc = dist_viagem / (viagem_24h / 60 / 60)
        ms_md = (dist_viagem * 1000) / (viagem_24h)
        l_p_hora = consumo_comb / ((viagem_24h/60) - (t_descanso/60))
        print('-'*30)
        print(f'o tempo da sua viagem foi de: {viagem_24h} segundos')
        print(f'a velocidade media nessa viagem foi de: {md_veloc:.2f}km/h e {ms_md:.2f} m/s')
        print(f'durante a viagem foi tido uma media de: {l_p_hora:.2f}l/h')

    elif mins_cheg < mins_part:

        calculo_tviagem = 86400 - (((mins_cheg - mins_part)* (-1)) * 60)        #ok
        md_veloc1 = dist_viagem / (calculo_tviagem / 60 / 60)
        ms_md = (dist_viagem * 1000) / (calculo_tviagem)
        l_p_hora1 = l_gastos / ((calculo_tviagem  - t_descanso) / 60)
        print('-'*30)
        print(f'o tempo da sua viagem foi de: {calculo_tviagem} segundos')
        print(f'a velocidade media nessa viagem foi de: {md_veloc1:.2f}km/h e {ms_md:.2f} m/s')
        print(f'durante a viagem foi tido uma media de: {l_p_hora1:.2f}l/h')

    elif mins_cheg > mins_part:

        calculo_tviagem2 = (mins_cheg - mins_part) * 60                     #ok
        md_veloc2 = dist_viagem / (calculo_tviagem2 / 60 / 60)
        ms_md = (dist_viagem * 1000) / (calculo_tviagem2)
        l_p_hora2 = l_gastos / ((calculo_tviagem2 - t_descanso) /60)
        print('-'*30)
        print(f'o tempo da sua viagem foi de: {calculo_tviagem2} segundos')
        print(f'a velocidade media nessa viagem foi de: {md_veloc2:.2f}km/h e {ms_md:.2f} m/s')
        print(f'durante a viagem foi tido uma media de: {l_p_hora2:.2f}l/h')

    print(f'o consumo de combustivel foi de: {consumo_comb:.2f} km/l')
    print(f'o consumo foi de {rs_km:.2f}R$/Km')
    print(f'o total gasto na viagem foi de: {gasto_viagem:.2f}R$')

