\* question10_local.lp *\
Minimize
OBJ: 320 payed_0 + 320 payed_1 + 320 payed_2 + 320 payed_3
 - 160 sold_local_production_0 - 160 sold_local_production_1
 - 160 sold_local_production_2 - 160 sold_local_production_3
Subject To
cnt_local_conso_0: auto_conso_0 + payed_0 = 50
cnt_local_conso_1: auto_conso_1 + payed_1 = 25
cnt_local_conso_2: auto_conso_2 + payed_2 = 50
cnt_local_conso_3: auto_conso_3 + payed_3 = 50
cnt_local_solar_0: auto_conso_0 + sold_local_production_0 = 350
cnt_local_solar_1: auto_conso_1 + sold_local_production_1 = 0
cnt_local_solar_2: auto_conso_2 + sold_local_production_2 = 0
cnt_local_solar_3: auto_conso_3 + sold_local_production_3 = 50
Bounds
auto_conso_0 <= 50
auto_conso_1 <= 25
auto_conso_2 <= 50
auto_conso_3 <= 50
payed_0 <= 50
payed_1 <= 25
payed_2 <= 50
payed_3 <= 50
sold_local_production_0 <= 350
sold_local_production_1 = 0
sold_local_production_2 = 0
sold_local_production_3 <= 50
End
