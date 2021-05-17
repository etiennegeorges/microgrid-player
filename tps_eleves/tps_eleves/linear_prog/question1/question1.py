import sys
import os
import pulp

sys.path.append(os.getcwd()+'/../../')
from common import parc
from linear_prog.pulp_utils import *
import common.charts




def create_thermal_plant_lp( pb,name):

    lp = pulp.LpProblem(name+".lp", pulp.LpMinimize)
    lp.setSolver()
    prod_vars = {}

    for t in pb.time_steps:
        prod_vars[t] = {}
        for thermal_plant in pb.thermal_plants :
            #creation des variables
            ###########################################################
            var_name = "prod_"+str(t)+"_"+str(thermal_plant.name)
            prod_vars[t][thermal_plant] = pulp.LpVariable(var_name, 0.0, thermal_plant.pmax(t) )
            
        #creation des contraintes (a adapter)
        ###########################################################
        constraint_name = "balance_"+ str(t)
        lp += pulp.lpSum([ prod_vars[t][thermal_plant] for thermal_plant in pb.thermal_plants ]) == pb.demand[t], constraint_name

    #creation de la fonction objectif (a adapter)
    ###########################################################
    lp.setObjective( pulp.lpSum([thermal_plant.proportionnal_cost * prod_vars[t][thermal_plant] *(  pb.time_step_duration/60.0) for thermal_plant in pb.thermal_plants for t in pb.time_steps]))

    model=Model(lp,prod_vars)

    return model




def run():
    pb_name = "question1"
    pb = parc.build_from_data(pb_name+".json")

    print ("Creating Model " + pb_name)
    model = create_thermal_plant_lp(pb, pb_name)

    print ("Solving Model")
    solve(model, pb_name)

    print ("Post Treatment")
    results=getResultsModel(pb,model,pb_name)
    printResults(pb, model, pb_name,[],results)
    
    
if __name__ == '__main__':
    run()




