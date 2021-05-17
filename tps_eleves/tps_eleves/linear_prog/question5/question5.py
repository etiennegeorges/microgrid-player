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
    in_use_vars ={}
    turn_on_vars={}
    defaillance={}
    cout_proportionnel_defaillance=3000 #euros/MWh
    for t in pb.time_steps:
        prod_vars[t] = {}
        in_use_vars[t] = {}
        turn_on_vars[t] = {}
        defaillance[t]=pulp.LpVariable("defailance_"+str(t), 0.0,None )

        for thermal_plant in pb.thermal_plants :
            #creation des variables
            ###########################################################
            var_name = "prod_"+str(t)+"_"+str(thermal_plant.name)
            prod_vars[t][thermal_plant] = pulp.LpVariable(var_name, 0.0, thermal_plant.pmax(t) )

            var_name = "inUse_"+str(t)+"_"+str(thermal_plant.name)
            in_use_vars[t][thermal_plant] = pulp.LpVariable(var_name, cat="Binary")

            var_name = "turnon_"+str(t)+"_"+str(thermal_plant.name)
            turn_on_vars[t][thermal_plant] = pulp.LpVariable(var_name, cat="Binary")
           
            #creation des contraintes
            ###########################################################
          
            #a conserver pour bien avoir in_use_var[t]=0 si pmax(t)=0
            if thermal_plant.pmax(t)<=0.001:
                 lp+=in_use_vars[t][thermal_plant]==0,"imposition_arret_"+str(t)+"_"+str(thermal_plant.name)
                 
            #conversion des duree min en nombre de pas de temps
            nb_time_steps_for_min_online_duration = int( (thermal_plant.minimum_online_duration)/pb.time_step_duration)
            if (thermal_plant.minimum_online_duration) % pb.time_step_duration > 0 :
                nb_time_steps_for_min_online_duration += 1
 
            constraint_name = "prod_min_" + str(thermal_plant) + "_" + str(t)
            lp += prod_vars[t][thermal_plant] >= in_use_vars[t][thermal_plant] * thermal_plant.pmin(t), constraint_name
            constraint_name = "prod_max_" + str(thermal_plant) + "_" + str(t)
            lp += prod_vars[t][thermal_plant] <= in_use_vars[t][thermal_plant] * thermal_plant.pmax(t), constraint_name
            if t != 0 :
                constraint_name = "demarrage_" + str(thermal_plant) + "_" + str(t)
                lp += in_use_vars[t][thermal_plant] - in_use_vars[t-1][thermal_plant] <= turn_on_vars[t][thermal_plant], constraint_name
            if t == 0 :
                constraint_name = "demarrage_" + str(thermal_plant) + "_" + str(t)
                lp += turn_on_vars[t][thermal_plant] >= in_use_vars[t][thermal_plant], constraint_name
            for k in range(max(0, t - nb_time_steps_for_min_online_duration + 1), t) :
                constraint_name = "duree_min_fct_"+ str(thermal_plant) + "_" + str(t) + "_" + str(k)
                lp += turn_on_vars[k][thermal_plant] <= in_use_vars[t][thermal_plant], constraint_name

                          
        constraint_name = "balance_"+ str(t)
        lp += pulp.lpSum([ prod_vars[t][thermal_plant] for thermal_plant in pb.thermal_plants ])+defaillance[t] == pb.demand[t], constraint_name


    #creation de la fonction objectif
    ###########################################################

    lp.setObjective( pulp.lpSum([defaillance[t] for t in pb.time_steps])* pb.time_step_duration/60.0*cout_proportionnel_defaillance\
                   +pulp.lpSum([ turn_on_vars[t][thermal_plant]*thermal_plant.startup_cost+prod_vars[t][thermal_plant] * (thermal_plant.proportionnal_cost* pb.time_step_duration/60.0)
        for thermal_plant in pb.thermal_plants for t in pb.time_steps]))
                    
    model=Model(lp,prod_vars)

    return model

# reponse : 509400

def run():
    pb_name = "question5"
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
