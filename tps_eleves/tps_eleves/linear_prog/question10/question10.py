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
        var_name = "auto_conso_"+str(t)
        prod_vars[t]["auto_conso"] = pulp.LpVariable(var_name, 0.0, pb.local_demand[t] )
        var_name = "payed_"+str(t)
        prod_vars[t]["payed_conso"] = pulp.LpVariable(var_name, 0.0, pb.local_demand[t] )
        var_name = "sold_local_production_"+str(t)
        prod_vars[t]["sold_local_production"] = pulp.LpVariable(var_name, 0.0, pb.local_solar_power[t] )
        
        lp+=prod_vars[t]["auto_conso"] +prod_vars[t]["payed_conso"]==pb.local_demand[t],"cnt_local_conso_"+str(t)
        lp+=prod_vars[t]["auto_conso"] +prod_vars[t]["sold_local_production"]==pb.local_solar_power[t],"cnt_local_solar_"+str(t)

    #a adapter
    lp.setObjective(pulp.lpSum([pb.time_step_duration/60.0 * prod_vars[t]["payed_conso"] * pb.electricity_tariff - pb.time_step_duration/60.0 * prod_vars[t]["sold_local_production"] * pb.solar_power_selling_price for t in pb.time_steps]))

    
                    
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

        #a adapter pour integrer l'autoconso
        constraint_name = "balance_"+ str(t)
        #pb.auto_conso[t]
        #pb.sold_local_production[t]
        lp += pulp.lpSum([ prod_vars[t][thermal_plant] for thermal_plant in pb.thermal_plants ])+defaillance[t] == pb.demand[t] - pb.auto_conso[t] - pb.sold_local_production[t], constraint_name


   #creation de la fonction objectif
   ###########################################################

    lp.setObjective( pulp.lpSum([defaillance[t] for t in pb.time_steps])* pb.time_step_duration/60.0*cout_proportionnel_defaillance\
                   +pulp.lpSum([ prod_vars[t][thermal_plant] * (thermal_plant.proportionnal_cost* pb.time_step_duration/60.0)
        for thermal_plant in pb.thermal_plants for t in pb.time_steps]))

    model=Model(lp,prod_vars)

    return model



def run():
    pb_name = "question10"
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

