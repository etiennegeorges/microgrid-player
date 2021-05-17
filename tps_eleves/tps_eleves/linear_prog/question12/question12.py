import sys
import os
import pulp

sys.path.append(os.getcwd()+'/../../')
from common import parc
from linear_prog.pulp_utils import *
import common.charts

def build_local_problem_lp( pb,name):
    lp = pulp.LpProblem(name+".lp", pulp.LpMinimize)
    lp.setSolver()
    prod_vars = {}
    in_use_vars ={}
    defaillance={}
    cout_proportionnel_defaillance=3000 #euros/MWh
    #demande = demande-auto_conso
    #auto_conso<=Enr
    #Enr=Enr-auto_conso
    #inject=
    
    for t in pb.time_steps:
        prod_vars[t] = {}
        in_use_vars[t] = {}
        
        var_name = "battery_stock"+str(t)
        prod_vars[t]["battery_stock"] = pulp.LpVariable(var_name, 0.0, pb.battery.energy_max)
        
        var_name = "battery_store"+str(t)
        prod_vars[t]["battery_store"] = pulp.LpVariable(var_name, -pb.battery.power_max_store,0.0)
        
        var_name = "battery_prod"+str(t)
        prod_vars[t]["battery_prod"] = pulp.LpVariable(var_name, 0.0,pb.battery.power_max_prod)
        
        cnt_name="cnt_storage_evolution_"+str(t)
        if t==pb.time_steps[0]:
            #initial stock=0
             lp+=prod_vars[t]["battery_stock"]==pb.time_step_duration/60.0*(-pb.battery.efficiency*prod_vars[t]["battery_store"]-prod_vars[t]["battery_prod"]),cnt_name
        else:
             lp+=prod_vars[t]["battery_stock"]==prod_vars[t-1]["battery_stock"]+pb.time_step_duration/60.0*(-pb.battery.efficiency*prod_vars[t]["battery_store"]-prod_vars[t]["battery_prod"]),cnt_name

        var_name = "auto_conso_"+str(t)
        prod_vars[t]["auto_conso"] = pulp.LpVariable(var_name, 0.0, pb.local_demand[t] )
        var_name = "payed_"+str(t)
        prod_vars[t]["payed_conso"] = pulp.LpVariable(var_name, 0.0, pb.local_demand[t] )
        var_name = "sold_local_production"+str(t)
        prod_vars[t]["sold_local_production"] = pulp.LpVariable(var_name, 0.0, pb.local_solar_power[t]+pb.battery.power_max_prod)
        
        lp+=prod_vars[t]["auto_conso"] +prod_vars[t]["payed_conso"]==pb.local_demand[t],"cnt_local_conso_"+str(t)
        
        lp+=prod_vars[t]["sold_local_production"]==pb.local_solar_power[t] - prod_vars[t]["auto_conso"] + prod_vars[t]["battery_prod"] + prod_vars[t]["battery_store"],"cnt_local_solar_"+str(t)


    lp.setObjective( pb.electricity_tariff*pulp.lpSum([prod_vars[t]["payed_conso"]  for t in pb.time_steps])* pb.time_step_duration/60.0\
                   -pulp.lpSum([pb.solar_power_selling_price_chronicle[t]*prod_vars[t]["sold_local_production"] for t in pb.time_steps]) * pb.time_step_duration/60.0)

    
                    
    model=Model(lp,prod_vars)
    return model
    
def create_thermal_plant_lp( pb,name):

    lp = pulp.LpProblem(name+".lp", pulp.LpMinimize)
    lp.setSolver()
    prod_vars = {}
    in_use_vars ={}
    defaillance={}
    cout_proportionnel_defaillance=3000 #euros/MWh
    #demande = demande-auto_conso
    #auto_conso<=Enr
    #Enr=Enr-auto_conso
    #inject=
    
    for t in pb.time_steps:
        prod_vars[t] = {}
        in_use_vars[t] = {}
        defaillance[t]=pulp.LpVariable("defailance_"+str(t), 0.0,None )
        for thermal_plant in pb.thermal_plants :
            #creation des variables
            ###########################################################
            var_name = "prod_"+str(t)+"_"+str(thermal_plant.name)
            prod_vars[t][thermal_plant] = pulp.LpVariable(var_name, 0.0, thermal_plant.pmax(t) )

            var_name = "inUse_"+str(t)+"_"+str(thermal_plant.name)
            in_use_vars[t][thermal_plant] = pulp.LpVariable(var_name, cat="Binary")

            #creation des contraintes
            ###########################################################
            constraint_name="pmin_"+str(t)+" "+str(thermal_plant.name)
            lp+=in_use_vars[t][thermal_plant]*thermal_plant.pmin(t)<=prod_vars[t][thermal_plant],constraint_name

            constraint_name="pmax_"+str(t)+" "+str(thermal_plant.name)
            lp+=in_use_vars[t][thermal_plant]*thermal_plant.pmax(t)>=prod_vars[t][thermal_plant],constraint_name


        constraint_name = "balance_"+ str(t)
        #a adapter
        #pb.auto_conso[t]
        #pb.sold_local_production[t]
        lp += pulp.lpSum([ prod_vars[t][thermal_plant] for thermal_plant in pb.thermal_plants ])+defaillance[t]== pb.demand[t] - pb.auto_conso[t] - pb.sold_local_production[t], constraint_name



    lp.setObjective( pulp.lpSum([defaillance[t] for t in pb.time_steps])* pb.time_step_duration/60.0*cout_proportionnel_defaillance\
                   +pulp.lpSum([ prod_vars[t][thermal_plant] * (thermal_plant.proportionnal_cost* pb.time_step_duration/60.0)
        for thermal_plant in pb.thermal_plants for t in pb.time_steps]))

    model=Model(lp,prod_vars)

    return model



def run():
    pb_name = "question12"
    pb = parc.build_from_data(pb_name+".json")

    print ("Creating Model " + pb_name)
    pb_name_local=pb_name+"_local"
    model = build_local_problem_lp(pb, pb_name_local)
    
    solve(model, pb_name_local)
    results=getResultsLocalModel(pb,model,pb_name)
        
    
    model = create_thermal_plant_lp(pb, pb_name)

    print ("Solving Model")
    solve(model, pb_name)

    print ("Post Treatment")
    results=getResultsModel(pb,model,pb_name)
    printResults(pb, model, pb_name,[],results)

if __name__ == '__main__':
    run()

