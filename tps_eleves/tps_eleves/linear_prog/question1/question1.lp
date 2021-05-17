\* question1.lp *\
Minimize
OBJ: 20 prod_0_thf1 + 44 prod_0_thf2 + 100 prod_0_thf3 + 20 prod_1_thf1
 + 44 prod_1_thf2 + 100 prod_1_thf3 + 20 prod_2_thf1 + 44 prod_2_thf2
 + 100 prod_2_thf3 + 20 prod_3_thf1 + 44 prod_3_thf2 + 100 prod_3_thf3
Subject To
balance_0: prod_0_thf1 + prod_0_thf2 + prod_0_thf3 = 1000
balance_1: prod_1_thf1 + prod_1_thf2 + prod_1_thf3 = 1600
balance_2: prod_2_thf1 + prod_2_thf2 + prod_2_thf3 = 800
balance_3: prod_3_thf1 + prod_3_thf2 + prod_3_thf3 = 900
Bounds
prod_0_thf1 <= 1000
prod_0_thf2 <= 550
prod_0_thf3 <= 200
prod_1_thf1 <= 1000
prod_1_thf2 <= 550
prod_1_thf3 <= 200
prod_2_thf1 <= 1000
prod_2_thf2 <= 550
prod_2_thf3 <= 200
prod_3_thf1 <= 1000
prod_3_thf2 <= 550
prod_3_thf3 <= 200
End
