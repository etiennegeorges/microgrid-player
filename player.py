# python 3
# this class combines all basic features of a generic player
import numpy as np
import pandas
import os
import pulp
import sys

sys.path.append(os.getcwd()+'/../../')
# from common import parc
# from linear_prog.pulp_utils import *
# import common.charts

random_lambda = np.random.rand(48)
rho = 0.95


class Player:

    def __init__(self):
        # some player might not have parameters
        self.parameters = 0
        self.horizon = 48
        self.capa = 60
        self.Pmax = 10
        self.rho_c = 0.95
        self.rho_d = 0.95
        self.delta_t = 0.5

    def set_scenario(self, scenario_data):
        self.data = scenario_data

    def set_prices(self, prices):
        self.prices = prices

    def compute_all_load(self):
        load = np.zeros(self.horizon)
        batterie = np.zeros(self.horizon)
        # moyenne = self.moyenne()
        # for time in range(self.horizon):
        # load[time] = self.compute_load(time)

        # Version 1
        # load[time] = self.data[time]

        # Version 2
        # 		time = 0
        # 		while self.data[time] >= moyenne:
        # 			load[time] = self.data[time]
        # 			time+= 1
        # 		for time1 in range(time, self.horizon):
        # 			if moyenne + batterie[time1 - 1] < self.data[time1]:
        # 				load[time1] = self.data[time1] - rho * batterie[time1 - 1]
        # 			else:
        # 				load[time1] = moyenne
        # 				batterie[time1] = rho * (moyenne - self.data[time1])
        # version 3
        lp = pulp.LpProblem("lp", pulp.LpMinimize)
        lp.setSolver()
        variable0 = {}
        variable1 = {}
        variable2 = {}
        variable3 = {}
        for t in range(self.horizon):
            var_name = "battery_loadcharge" + str(t)
            variable0[t] = pulp.LpVariable(var_name, 0, self.Pmax)

            var_name = "battery_loaddecharge" + str(t)
            variable1[t] = pulp.LpVariable(var_name, 0, self.Pmax)

            var_name = "demande_totale" + str(t)
            variable2[t] = pulp.LpVariable(var_name, 0, None)

            constraint_name = "stock positif" + str(t)
            lp += pulp.lpSum(
                [self.rho_c * variable0[k] - self.rho_d * variable1[k] for k in range(t)]) >= 0, constraint_name

            constraint_name = "puissance < capacite" + str(t)
            lp += pulp.lpSum(
                [self.rho_c * variable0[s] - (variable1[s] * (1/self.rho_d)) for s in range(t)]) <= self.capa, constraint_name

            constraint_name = "egalite offre demande" + str(t)
            lp += self.data[t] + variable0[t] + variable1[t] == variable2[t], constraint_name

            var_name = "reste_batterie" + str(t)
            variable3[t] = pulp.LpVariable(var_name, 0, None)

        constraint_name = "stock initial nul"
        lp += variable3[0]==0, constraint_name

        constraint_name = "reste dans la batterie"
        lp += variable3[self.horizon - 1] == self.delta_t * pulp.lpSum([variable0[t] * self.rho_c - variable1[s] *  (1/self.rho_d) for s in range(self.horizon)]), constraint_name

        lp.setObjective(
            pulp.lpSum([self.prices[s] * variable2[s] for s in range(self.horizon)]) - self.prices[self.horizon - 1] * variable3[self.horizon - 1])

        lp.solve()
        print(lp)
        # variable2[0].value()
        # model = Model(lp, variable0, variable1, variable2, variable3)
        #
        # solve(model)
        # print(lp)
        # results = getResultsModel(pb, model)

        for i in range(0, self.horizon):
            load[i] = variable2[i].value()
        # load = variable2
        print(load)
        return load

    def take_decision(self, time):
        # TO BE COMPLETED
        return 0

    def compute_load(self, time):
        load = self.take_decision(time)
        # do stuff ?
        return load

    def reset(self):
        # reset all observed data
        pass

    def moyenne(self):
        m = 0
        for time in range(self.horizon):
            m += self.data[time]
        m /= self.horizon
        return m

## Essai test fesabilité
# my_df = pandas.read_csv("indus_cons_scenarios.csv", sep=";", decimal=".")
# scenario_data1 = np.array(my_df)
# scenario_data = np.zeros(48)
# for i in range(1, 49):
#     scenario_data[i - 1] = scenario_data1[i][3]
#
# p = Player()
# p.set_scenario(scenario_data)
#
# prices_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7,
#                8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
# p.set_prices(prices_test)
#
# load = p.compute_all_load()
# print(load)





## Essai classique
# my_df = pandas.read_csv(os.path.join(os.getcwd(), 'indus_cons_scenarios.csv'), sep=";", decimal=".")
# scenario_data1 = np.array(my_df)
# scenario_data = np.zeros(48)
# for i in range(1, 49):
#     scenario_data[i - 1] = scenario_data1[i][3]
# print("Demande :")
# print(scenario_data)
#
# P = Player()
# P.set_scenario(scenario_data)
# P.set_prices(random_lambda)
#
# load = P.compute_all_load()
# print("Sortie :")
# print(load)

if __name__=="__main_":
	myplayer = Player()
	myload = myplayer.compute_all_load()
