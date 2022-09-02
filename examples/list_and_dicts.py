def main():
    my_list = [1,"hello",True,4.5]
    my_dict = {"firstname": "Angie", "lastname": "Garcia"}
    
    super_list = [{"firstname": "Angie", "lastname": "Garcia"},
                {"firstname": "Pola", "lastname": "Garcia"},
                {"firstname": "Ana", "lastname": "Castro"},
                {"firstname": "Carlos", "lastname": "Garcia"},
                {"firstname": "Pedro", "lastname": "Murillo"},
    ]
    super_dict = {
        "natural_nums":[1, 2, 3, 4, 5],
        "integer_nums": [-1, -2 , 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.4]
    }
    # list_nums_2 = [i**2 for i in range(1, 101) if i % 3 != 0 ]
    # list_nums_2 = [i for i in range(1,100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    # list_nums_2 = {i:i**3 for i in range(1,101) if i % 3 != 0}
    list_nums_2 = {i:i**0.5 for i in range(1,101)}
    # diccionaro llaves 100 narutales y vals elevado al cubo
    print(list_nums_2)
    # for key, value in super_dict.items():
    #     print(key, "-", value)
if __name__ == '__main__':
    main()