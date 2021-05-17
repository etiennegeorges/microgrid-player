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
    volume_res ={}
    surproduction_vars={}
    wind_power=pb.wind_power #list with wind power for all time steps
    solar_power=pb.solar_power #list with solara power for all time steps
    
    for t in pb.time_steps:
        prod_vars[t] = {}
        volume_res[t] ={}
        
        #creation des variables
        ###########################################################
        
        surproduction_vars[t]=pulp.LpVariable("surproduction_"+str(t),0.0,None)

        for reservoir in pb.reservoirs :
            var_name="reservoir_"+str(t)+"_"+str(reservoir.id)
            volume_res[t][reservoir]=pulp.LpVariable(var_name,reservoir.minimum_volume,reservoir.maximum_volume)
        for hydro_plant in pb.hydro_plants :
            var_name ="prod_"+str(t)+"_"+str(hydro_plant.name)
            prod_vars[t][hydro_plant]=pulp.LpVariable(var_name,0.0,hydro_plant.operating_levels[0].power)
        #creation des contraintes
        ###########################################################
        for reservoir in pb.reservoirs:
            hydro_plants_down=[pb.hydro_plants[id] for id in reservoir.downstream_hydro_plants_ids]
            const_name="maj_stock"+str(t)
            rendement=hydro_plant.operating_levels[0].flow/hydro_plant.operating_levels[0].power
            if t>0:
               lp+=volume_res[t][reservoir]==volume_res[t-1][reservoir]-rendement*pb.time_step_duration*60*pulp.lpSum(([prod_vars[t][hydro_plant] for hydro_plant in hydro_plants_down])),const_name
            else :
               lp+=volume_res[t][reservoir]==reservoir.initial_volume-rendement*pb.time_step_duration*60*pulp.lpSum(([prod_vars[t][hydro_plant] for hydro_plant in hydro_plants_down])),const_name
        for thermal_plant in pb.thermal_plants :
            var_name = "prod_"+str(t)+"_"+str(thermal_plant.name)
            prod_vars[t][thermal_plant] = pulp.LpVariable(var_name, 0.0, thermal_plant.pmax(t) )
        constraint_name = "balance_"+ str(t)
        lp += pulp.lpSum([ prod_vars[t][thermal_plant] for thermal_plant in pb.thermal_plants ])+ pulp.lpSum([ prod_vars[t][hydro_plant] for hydro_plant in pb.hydro_plants ]) == pb.demand[t]-pb.solar_power[t]-pb.wind_power[t]+surproduction_vars[t], constraint_name
        
    #creation de la fonction objectif
    ###########################################################
    lp.setObjective( pulp.lpSum([ prod_vars[t][thermal_plant] *( thermal_plant.proportionnal_cost* pb.time_step_duration/60.0)
        for thermal_plant in pb.thermal_plants for t in pb.time_steps]\
        +pulp.lpSum([pb.over_production_penalty*surproduction_vars[t] * pb.time_step_duration/60.0 for t in pb.time_steps])))

    model=Model(lp,prod_vars,volume_res)

    return model



def run():
    pb_name = "question8"
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
