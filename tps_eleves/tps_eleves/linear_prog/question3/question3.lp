\* question3.lp *\
Minimize
OBJ: 6000 defailance_0 + 6000 defailance_1 + 6000 defailance_2
 + 6000 defailance_3 + 20 prod_0_thf1 + 44 prod_0_thf2 + 100 prod_0_thf3
 + 20 prod_1_thf1 + 44 prod_1_thf2 + 100 prod_1_thf3 + 20 prod_2_thf1
 + 44 prod_2_thf2 + 100 prod_2_thf3 + 20 prod_3_thf1 + 44 prod_3_thf2
 + 100 prod_3_thf3
Subject To
balance_0: defailance_0 + prod_0_thf1 + prod_0_thf2 + prod_0_thf3 = 1000
balance_1: defailance_1 + prod_1_thf1 + prod_1_thf2 + prod_1_thf3 = 1600
balance_2: defailance_2 + prod_2_thf1 + prod_2_thf2 + prod_2_thf3 = 800
balance_3: defailance_3 + prod_3_thf1 + prod_3_thf2 + prod_3_thf3 = 900
prod_max_<common.parc.ThermalPlant_object_at_0x0000012F00FFAA00>_0:
 - 200 inUse_0_thf3 + prod_0_thf3 <= 0
prod_max_<common.parc.ThermalPlant_object_at_0x0000012F00FFAA00>_1:
 - 200 inUse_1_thf3 + prod_1_thf3 <= 0
prod_max_<common.parc.ThermalPlant_object_at_0x0000012F00FFAA00>_2:
 - 200 inUse_2_thf3 + prod_2_thf3 <= 0
prod_max_<common.parc.ThermalPlant_object_at_0x0000012F00FFAA00>_3:
 - 200 inUse_3_thf3 + prod_3_thf3 <= 0
prod_max_<common.parc.ThermalPlant_object_at_0x0000012F7F57A460>_0:
 - 1000 inUse_0_thf1 + prod_0_thf1 <= 0
prod_max_<common.parc.ThermalPlant_object_at_0x0000012F7F57A460>_1:
 - 1000 inUse_1_thf1 + prod_1_thf1 <= 0
prod_max_<common.parc.ThermalPlant_object_at_0x0000012F7F57A460>_2:
 prod_2_thf1 <= 0
prod_max_<common.parc.ThermalPlant_object_at_0x0000012F7F57A460>_3:
 - 1000 inUse_3_thf1 + prod_3_thf1 <= 0
prod_max_<common.parc.ThermalPlant_object_at_0x0000012F7F57A7F0>_0:
 - 550 inUse_0_thf2 + prod_0_thf2 <= 0
prod_max_<common.parc.ThermalPlant_object_at_0x0000012F7F57A7F0>_1:
 - 550 inUse_1_thf2 + prod_1_thf2 <= 0
prod_max_<common.parc.ThermalPlant_object_at_0x0000012F7F57A7F0>_2:
 - 550 inUse_2_thf2 + prod_2_thf2 <= 0
prod_max_<common.parc.ThermalPlant_object_at_0x0000012F7F57A7F0>_3:
 - 550 inUse_3_thf2 + prod_3_thf2 <= 0
prod_min_<common.parc.ThermalPlant_object_at_0x0000012F00FFAA00>_0:
 - 100 inUse_0_thf3 + prod_0_thf3 >= 0
prod_min_<common.parc.ThermalPlant_object_at_0x0000012F00FFAA00>_1:
 - 100 inUse_1_thf3 + prod_1_thf3 >= 0
prod_min_<common.parc.ThermalPlant_object_at_0x0000012F00FFAA00>_2:
 - 100 inUse_2_thf3 + prod_2_thf3 >= 0
prod_min_<common.parc.ThermalPlant_object_at_0x0000012F00FFAA00>_3:
 - 100 inUse_3_thf3 + prod_3_thf3 >= 0
prod_min_<common.parc.ThermalPlant_object_at_0x0000012F7F57A460>_0:
 prod_0_thf1 >= 0
prod_min_<common.parc.ThermalPlant_object_at_0x0000012F7F57A460>_1:
 prod_1_thf1 >= 0
prod_min_<common.parc.ThermalPlant_object_at_0x0000012F7F57A460>_2:
 prod_2_thf1 >= 0
prod_min_<common.parc.ThermalPlant_object_at_0x0000012F7F57A460>_3:
 prod_3_thf1 >= 0
prod_min_<common.parc.ThermalPlant_object_at_0x0000012F7F57A7F0>_0:
 prod_0_thf2 >= 0
prod_min_<common.parc.ThermalPlant_object_at_0x0000012F7F57A7F0>_1:
 prod_1_thf2 >= 0
prod_min_<common.parc.ThermalPlant_object_at_0x0000012F7F57A7F0>_2:
 prod_2_thf2 >= 0
prod_min_<common.parc.ThermalPlant_object_at_0x0000012F7F57A7F0>_3:
 prod_3_thf2 >= 0
Bounds
prod_0_thf1 <= 1000
prod_0_thf2 <= 550
prod_0_thf3 <= 200
prod_1_thf1 <= 1000
prod_1_thf2 <= 550
prod_1_thf3 <= 200
prod_2_thf1 = 0
prod_2_thf2 <= 550
prod_2_thf3 <= 200
prod_3_thf1 <= 1000
prod_3_thf2 <= 550
prod_3_thf3 <= 200
Binaries
inUse_0_thf1
inUse_0_thf2
inUse_0_thf3
inUse_1_thf1
inUse_1_thf2
inUse_1_thf3
inUse_2_thf2
inUse_2_thf3
inUse_3_thf1
inUse_3_thf2
inUse_3_thf3
End
