v_inserido = int(input("insira um valor até 4 dígitos: "))
if v_inserido < 0 or v_inserido > 9999:
    print("erro! digite um valor até quatro digitos!")
else:
    mil = v_inserido // 1000
    cem = (v_inserido % 1000) // 100
    dez = (v_inserido % 100) // 10
    und = v_inserido % 10
    soma = mil + cem + dez + und
    print("A soma dos algarismos é:", soma)