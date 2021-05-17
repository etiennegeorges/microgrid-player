\* question6.lp *\
Minimize
OBJ: 20 prod_0_thf1 + 44 prod_0_thf2 + 100 prod_0_thf3 + 20 prod_1_thf1
 + 44 prod_1_thf2 + 100 prod_1_thf3 + 20 prod_2_thf1 + 44 prod_2_thf2
 + 100 prod_2_thf3 + 20 prod_3_thf1 + 44 prod_3_thf2 + 100 prod_3_thf3
Subject To
balance_0: prod_0_hyd_00 + prod_0_thf1 + prod_0_thf2 + prod_0_thf3 = 1000
balance_1: prod_1_hyd_00 + prod_1_thf1 + prod_1_thf2 + prod_1_thf3 = 1600
balance_2: prod_2_hyd_00 + prod_2_thf1 + prod_2_thf2 + prod_2_thf3 = 800
balance_3: prod_3_hyd_00 + prod_3_thf1 + prod_3_thf2 + prod_3_thf3 = 900
maj_stock0: 7200 prod_0_hyd_00 + reservoir_0_0 = 1440000
maj_stock1: 7200 prod_1_hyd_00 - reservoir_0_0 + reservoir_1_0 = 0
maj_stock2: 7200 prod_2_hyd_00 - reservoir_1_0 + reservoir_2_0 = 0
maj_stock3: 7200 prod_3_hyd_00 - reservoir_2_0 + reservoir_3_0 = 0
Bounds
prod_0_hyd_00 <= 75
prod_0_thf1 <= 1000
prod_0_thf2 <= 550
prod_0_thf3 <= 200
prod_1_hyd_00 <= 75
prod_1_thf1 <= 1000
prod_1_thf2 <= 550
prod_1_thf3 <= 200
prod_2_hyd_00 <= 75
prod_2_thf1 = 0
prod_2_thf2 <= 550
prod_2_thf3 <= 200
prod_3_hyd_00 <= 75
prod_3_thf1 <= 1000
prod_3_thf2 <= 550
prod_3_thf3 <= 200
reservoir_0_0 <= 1440000
reservoir_1_0 <= 1440000
reservoir_2_0 <= 1440000
reservoir_3_0 <= 1440000
End
