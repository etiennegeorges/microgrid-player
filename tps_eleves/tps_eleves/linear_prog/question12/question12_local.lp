\* question12_local.lp *\
Minimize
OBJ: 320 payed_0 + 320 payed_1 + 320 payed_2 + 320 payed_3
 - 160 sold_local_production0 - 160 sold_local_production1
 - 213.34 sold_local_production2 - 160 sold_local_production3
Subject To
cnt_local_conso_0: auto_conso_0 + payed_0 = 50
cnt_local_conso_1: auto_conso_1 + payed_1 = 25
cnt_local_conso_2: auto_conso_2 + payed_2 = 25
cnt_local_conso_3: auto_conso_3 + payed_3 = 50
cnt_local_solar_0: auto_conso_0 - battery_prod0 - battery_store0
 + sold_local_production0 = 350
cnt_local_solar_1: auto_conso_1 - battery_prod1 - battery_store1
 + sold_local_production1 = 0
cnt_local_solar_2: auto_conso_2 - battery_prod2 - battery_store2
 + sold_local_production2 = 0
cnt_local_solar_3: auto_conso_3 - battery_prod3 - battery_store3
 + sold_local_production3 = 50
cnt_storage_evolution_0: 2 battery_prod0 + battery_stock0 + 1.5 battery_store0
 = 0
cnt_storage_evolution_1: 2 battery_prod1 - battery_stock0 + battery_stock1
 + 1.5 battery_store1 = 0
cnt_storage_evolution_2: 2 battery_prod2 - battery_stock1 + battery_stock2
 + 1.5 battery_store2 = 0
cnt_storage_evolution_3: 2 battery_prod3 - battery_stock2 + battery_stock3
 + 1.5 battery_store3 = 0
Bounds
auto_conso_0 <= 50
auto_conso_1 <= 25
auto_conso_2 <= 25
auto_conso_3 <= 50
battery_prod0 <= 200
battery_prod1 <= 200
battery_prod2 <= 200
battery_prod3 <= 200
battery_stock0 <= 300
battery_stock1 <= 300
battery_stock2 <= 300
battery_stock3 <= 300
-200 <= battery_store0 <= 0
-200 <= battery_store1 <= 0
-200 <= battery_store2 <= 0
-200 <= battery_store3 <= 0
payed_0 <= 50
payed_1 <= 25
payed_2 <= 25
payed_3 <= 50
sold_local_production0 <= 550
sold_local_production1 <= 200
sold_local_production2 <= 200
sold_local_production3 <= 250
End
