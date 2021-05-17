\* question9.lp *\
Minimize
OBJ: 20 prod_0_thf1 + 44 prod_0_thf2 + 100 prod_0_thf3 + 20 prod_1_thf1
 + 44 prod_1_thf2 + 100 prod_1_thf3 + 20 prod_2_thf1 + 44 prod_2_thf2
 + 100 prod_2_thf3 + 20 prod_3_thf1 + 44 prod_3_thf2 + 100 prod_3_thf3
Subject To
balance_0: prod_0_hyd_00 + prod_0_thf1 + prod_0_thf2 + prod_0_thf3 = 940
balance_1: prod_1_hyd_00 + prod_1_thf1 + prod_1_thf2 + prod_1_thf3 = 1450
balance_2: prod_2_hyd_00 + prod_2_thf1 + prod_2_thf2 + prod_2_thf3 = -75
balance_3: prod_3_hyd_00 + prod_3_thf1 + prod_3_thf2 + prod_3_thf3 = 740
decomposition_turbinage_pompage_0: prod_0_hyd_00 - prod_pompe_0_hyd_00
 - prod_turbine_0_hyd_00 = 0
decomposition_turbinage_pompage_1: prod_1_hyd_00 - prod_pompe_1_hyd_00
 - prod_turbine_1_hyd_00 = 0
decomposition_turbinage_pompage_2: prod_2_hyd_00 - prod_pompe_2_hyd_00
 - prod_turbine_2_hyd_00 = 0
decomposition_turbinage_pompage_3: prod_3_hyd_00 - prod_pompe_3_hyd_00
 - prod_turbine_3_hyd_00 = 0
maj_stock0: 4800 prod_pompe_0_hyd_00 + 7200 prod_turbine_0_hyd_00
 + reservoir_0_0 = 1440000
maj_stock1: 4800 prod_pompe_1_hyd_00 + 7200 prod_turbine_1_hyd_00
 - reservoir_0_0 + reservoir_1_0 = 0
maj_stock2: 4800 prod_pompe_2_hyd_00 + 7200 prod_turbine_2_hyd_00
 - reservoir_1_0 + reservoir_2_0 = 0
maj_stock3: 4800 prod_pompe_3_hyd_00 + 7200 prod_turbine_3_hyd_00
 - reservoir_2_0 + reservoir_3_0 = 0
Bounds
prod_0_hyd_00 free
prod_0_thf1 <= 1000
prod_0_thf2 <= 550
prod_0_thf3 <= 200
prod_1_hyd_00 free
prod_1_thf1 <= 1000
prod_1_thf2 <= 550
prod_1_thf3 <= 200
prod_2_hyd_00 free
prod_2_thf1 = 0
prod_2_thf2 <= 550
prod_2_thf3 <= 200
prod_3_hyd_00 free
prod_3_thf1 <= 1000
prod_3_thf2 <= 550
prod_3_thf3 <= 200
-75 <= prod_pompe_0_hyd_00 <= 0
-75 <= prod_pompe_1_hyd_00 <= 0
-75 <= prod_pompe_2_hyd_00 <= 0
-75 <= prod_pompe_3_hyd_00 <= 0
prod_turbine_0_hyd_00 <= 75
prod_turbine_1_hyd_00 <= 75
prod_turbine_2_hyd_00 <= 75
prod_turbine_3_hyd_00 <= 75
reservoir_0_0 <= 1440000
reservoir_1_0 <= 1440000
reservoir_2_0 <= 1440000
reservoir_3_0 <= 1440000
End
