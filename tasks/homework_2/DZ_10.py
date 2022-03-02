s_1_dis = str(input("Заявка: английский, немецкий, право, математика, сольфеджио "))
s_2_dis = str(input("Заявка: английский, немецкий, право, математика, сольфеджио"))
s_3_dis = str(input("Заявка: английский, немецкий, право, математика, сольфеджио"))

s_3_dis = s_3_dis.split(" ")
s_1_dis = s_1_dis.split(" ")
s_2_dis = s_2_dis.split(" ")
#print(s_1_dis)
set(s_1_dis)
set(s_3_dis)
set(s_2_dis)

new_list = list(set(s_1_dis) & set(s_2_dis) & set(s_3_dis))
print("Кол-во факультативов, которые откроются:", len(new_list))




