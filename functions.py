def myfunc(str):
    mod_str = ''

    for item in str:
        if str.index(item) % 2 == 0:
            mod_str += item.lower()

        else:
            mod_str += item.upper()

    print(mod_str)
    # return mod_str

myfunc("Anticipate")


# def myfunc(x):
#     out = []
#     for i in range(len(x)):
#         if i%2==0:
#             out.append(x[i].lower())
#         else:
#             out.append(x[i].upper())
#     return ''.join(out)
