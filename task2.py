boys = input("Введите список юношей через пробел: ").split()
girls = input("Введите список девушек через пробел: ").split()
boys = sorted(boys)
girls = sorted(girls)

if boys and girls:
    print("\nИдеальные пары: ")
    for i in range(min(len(girls), len(boys))):
        print(boys[i] + " и " + girls[i])

