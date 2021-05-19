# python 3
# this class combines all basic features of a generic player
import numpy as np
import pandas
import os
import pulp

random_lambda = np.random.rand(48)
rho = 0.95

class Player:

	def __init__(self):
		# some player might not have parameters
		self.parameters = 0
		self.horizon = 48

	def set_scenario(self, scenario_data):
		self.data = scenario_data

	def set_prices(self, prices):
		self.prices = prices

	def compute_all_load(self):
		load = np.zeros(self.horizon)
		batterie = np.zeros(self.horizon)
		moyenne = self.moyenne()
		# for time in range(self.horizon):
			# load[time] = self.compute_load(time)

			# Version 1
			# load[time] = self.data[time]

		# Version 2
		time = 0
		while self.data[time] >= moyenne:
			load[time] = self.data[time]
			time+= 1
		for time1 in range(time, self.horizon):
			if moyenne + batterie[time1 - 1] < self.data[time1]:
				load[time1] = self.data[time1] - rho * batterie[time1 - 1]
			else:
				load[time1] = moyenne
				batterie[time1] = rho * (moyenne - self.data[time1])
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
			m+= self.data[time]
		m/= self.horizon
		return m



my_df = pandas.read_csv(os.path.join(os.getcwd(), 'indus_cons_scenarios.csv'), sep=";", decimal=".")
scenario_data1 = np.array(my_df)
scenario_data = np.zeros(48)
for i in range(1, 49):
	scenario_data[i-1] = scenario_data1[i][3]
print("Demande :")
print(scenario_data)

P = Player()
P.set_scenario(scenario_data)
P.set_prices(random_lambda)
load = P.compute_all_load()
print("Sortie :")
print(load)


# if __name__=="__main__":
# 	myplayer = Player()
# 	myload = myplayer.compute_all_load()