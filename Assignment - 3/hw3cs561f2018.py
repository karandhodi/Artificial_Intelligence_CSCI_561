import numpy as np
import copy
import operator
import collections
import math

with open('input.txt') as inputfile:
    data = inputfile.readlines()
inputfile.close()

n = int(data[0])

def give_city_grid():
    city = [-1] * n
    for row in range(n):
        city[row] = [-1] * n
    return city

cities = []

def add_city(city):
    result_city = copy.deepcopy(city)
    cities.append(result_city) 
    
def add_policy(policy):
    result_policy = copy.deepcopy(policy)
    policies.append(result_policy)  

no_of_cars = int(data[1])
no_of_obstacles = int(data[2])

obstacle_locations = []

for i in range(0, no_of_obstacles):
    obstacle_locations.append(data[3 + i])
    
car_start_locations = []

for i in range(0, no_of_cars):
    car_start_locations.append(data[3 + no_of_obstacles + i])
    
car_stop_locations =[]
car_stop_locations_reverse =[]
    
for i in range(0, no_of_cars):
    car_stop_locations.append(data[3 + no_of_obstacles + no_of_cars + i])
    
car_stop_final = []
   
for c in range(no_of_cars):
    
    
    city = give_city_grid()
    city1 = give_city_grid()
    
    car_stop_locations_reverse = []
    
    for i in range(0, no_of_obstacles):
        separator_index = obstacle_locations[i].find(",")
        obstacle_location_X = int(obstacle_locations[i][separator_index + 1:])
        obstacle_location_Y = int(obstacle_locations[i][0:separator_index])
        city[obstacle_location_X][obstacle_location_Y] = -101
        
    separator_index = car_stop_locations[c].find(",")
    car_stop_location_X = int(car_stop_locations[c][separator_index + 1:])
    car_stop_location_Y = int(car_stop_locations[c][0:separator_index])
    city[car_stop_location_X][car_stop_location_Y] = 99
    
    for i in range(n):
        for j in range(n):
           city1[i][j] = city[i][j] 
    
    add_city(city)
    city1.reverse()
    
    car_stop_locations_reverse.append([(index, row.index(99)) for index, row in enumerate(city1) if 99 in row])
    
    for i in car_stop_locations_reverse:
        x = i[0][1]
        y = i[0][0]
    
    car_stop_final.append([tuple([x,y])])
    
    
    
policies = []

def func_get_direction_left ( current_direction ):
    if current_direction == 'N':
        return 'W'
    else:
        if current_direction == 'W':
            return 'S'
        else:
            if current_direction == 'S':
                return 'E'
            else:
                if current_direction == 'E':
                    return 'N'
                
def func_get_direction_right ( current_direction ):
    if current_direction == 'N':
        return 'E'
    else:
        if current_direction == 'W':
            return 'N'
        else:
            if current_direction == 'S':
                return 'W'
            else:
                if current_direction == 'E':
                    return 'S'  

def func_get_direction_around ( current_direction ):
    if current_direction == 'N':
        return 'S'
    else:
        if current_direction == 'W':
            return 'E'
        else:
            if current_direction == 'S':
                return 'N'
            else:
                if current_direction == 'E':
                    return 'W'  
                
directions = [(1,0), (0, 1), (-1, 0), (0, -1)]

def metaphysical():
    return
                
def turn_right(direction):
    if directions.index(direction)-1 == -1:
        return directions[len(directions) - 1]
    else:
        return directions[directions.index(direction)-1]

def turn_left(direction):
    return directions[(directions.index(direction)+1) % len(directions)]

def turn_around(direction):
    return directions[(directions.index(direction)+2) % len(directions)]
    
class Markov:
    def _init_(self, init, endStates, operationDirectory, gamma = 0.9):
        modernize(self, init = init, endStates = endStates, operationDirectory = operationDirectory, gamma = gamma, prize = {}, positions = set())
    
    def Transition(position, operation):
        metaphysical()
        
    def P(self, position):
        return self.prize[position]
    
    def operations(self, position):
        if position in self.endStates:
            return [None]
        else: 
            return self.operationDirectory

def modernize(a, **records):
    if isinstance(a, dict):
        a.modernize(records)
    else:
        a.__dict__.update(records)
    return a

class GMarkov(Markov):
    def __init__(self, matrix, endStates, init = (0,0), gamma = 0.9):
        matrix.reverse()
        Markov._init_(self, init, endStates = endStates, operationDirectory = directions, gamma = gamma)
        modernize(self, matrix=matrix, r = len(matrix), c = len(matrix[0]))
        for a in range(self.c):
            for b in range(self.r):
                self.prize[a, b] = matrix[b][a]
                if matrix[b][a] is not None:
                    self.positions.add((a, b))
                    
    def Transition(self, position, operation):
        if operation == None:
            return [(0.0, position)]
        else:
            return [(0.7, self.advance(position, operation)),
                    (0.1, self.advance(position, turn_right(operation))),
                    (0.1, self.advance(position, turn_left(operation))),
                    (0.1, self.advance(position, turn_around(operation)))]
            
    def advance(self, position, dr):
        position1 = concatenate(position, dr)
        return case(position1 in self.positions, position1, position)

def case(trial, output, alt):
    if trial:
        if callable(output): return output()
        return output
    else:
        if callable(alt): return alt()
        return alt

def concatenate(x, y):
    return tuple(map(operator.add, x, y))

def finding_utilities (markov, epsilon = 0.1):
    T, P, gamma = markov.Transition, markov.P, markov.gamma  
    utility1 = dict([(p, 0) for p in markov.positions])
    while 1:
        utility = utility1.copy()
        d = 0
        for p in markov.positions:
            sum_lst = []
            for o in markov.operations(p):
                lst = []
                for (p1, o1) in T(p, o):
                    lst.append(p1 * utility[o1])
                sum_lst.append(sum(lst))
            max_lst = max(sum_lst)
            utility1[p] = P(p) + gamma * max_lst
           
            d = max(d, abs(utility1[p] - utility[p]))
        if d < epsilon * (1 - gamma) / gamma:
             return utility

def finding_best_utility (markov, utility):
    list1 = {}
    for p in markov.positions:
        list1[p] = function_maximum(markov.operations(p), lambda o:predicted(o, p, markov, utility))
    return list1

def predicted(o, p, markov, utility):
    listt = []
    for (x, p1) in markov.Transition(p, o):
        listt.append(x * utility[p1])
    sum_list = sum(listt)
    return sum_list
    
def function_maximum(lst, rel):
    best = lst[0] 
    best_score = rel(best)
    for x in lst:
        x_score = rel(x)
        
        if x_score > best_score:
            best = x
            best_score = x_score
        else:    
            if x_score == best_score:
                if x == (0,1):
                    #print("hello")
                    best = x
                    best_score = x_score
                else:
                    
                    if x == (0,-1) and best == (0,1):
                        metaphysical()
                    else:
                        if x == (1,0) and best == (0,1):
                            metaphysical()
                        else:
                            if x == (-1,0) and best == (0,1):
                                metaphysical()
                            else:
                                if x == (0,-1) and (best == (-1,0) or best == (1,0)):
                                   best = x
                                   best_score = x_score 
                                else:
                                    if x == (1,0) and best == (-1,0):
                                        best = x
                                        best_score = x_score 
                                    else:
                                        if (x == (1,0) or x == (-1,0)) and best == (0,-1):
                                            metaphysical()
                                        else:
                                            if (x == (-1,0) and best == (1,0)):
                                                metaphysical()
    return best
    
A = {}

for c in range (no_of_cars):

    A[c] = GMarkov(cities[c],
                   endStates=car_stop_final[c])  
    
    X = finding_utilities(A[c],0.1)
    
    B = finding_best_utility(A[c], X)  
    
    
    
    policy = give_city_grid()

    od = collections.OrderedDict(sorted(B.items()))
    
    x = 0
    y = 0
    
    for j in range(n):
        y = 0
        for i in range(n-1,-1,-1):
           policy[i][j] = od[x,y] 
           y = y + 1
        x = x + 1
            
    for i in range(n):
        for j in range(n):
            if policy[i][j] == (1,0):
                policy[i][j] = 'E'
            else:
                if policy[i][j] == (0,1):
                    policy[i][j] = 'N'
                else:
                    if policy[i][j] == (-1,0):
                        policy[i][j] = 'W'
                    else:
                        if policy[i][j] == (0,-1):
                            policy[i][j] = 'S'
                        else:
                            policy[i][j] = 0
                            
    add_policy(policy)
    
for city in cities:
    city.reverse()
    
final_val_list = []
    
for i in range(no_of_cars):
    
    utility = 10 * [0] 
    
    for j in range(10):
        
        separator_index = car_start_locations[i].find(",")
        p = int(car_start_locations[i][separator_index + 1:])
        q = int(car_start_locations[i][0:separator_index])
        
        separator_index_1 = car_stop_locations[i].find(",")
        car_stop_location_X = int(car_stop_locations[i][separator_index_1 + 1:])
        car_stop_location_Y = int(car_stop_locations[i][0:separator_index_1])
        
        np.random.seed(j)
        swerve = np.random.random_sample(1000000)
        k = 0
        np.finfo(type(swerve[k]))
        policy = policies[i]
        city = cities[i]
        
        if p == car_stop_location_X and q == car_stop_location_Y:
            utility[j] += 100
        else:
            while True:
                
                move = policy[p][q]
                
                if swerve[k] > 0.7:
                    if swerve[k] > 0.8:
                        if swerve[k] > 0.9:
                            move = func_get_direction_right( func_get_direction_right ( move ) )
                        else:
                             move = func_get_direction_right ( move )
                    else:
                       
                        move = func_get_direction_left( move )
                        
                k = k + 1
                
               
                
                if move == 'N':
                    
                    if p == 0:
                        utility[j] += city[p][q]
                        move = policy[p][q]
                    else:
                        p = p - 1
                        utility[j] += city[p][q]
                        move = policy[p][q]
                else:   
                    if move == 'S':
                        
                        if p == n - 1:
                            utility[j] += city[p][q]
                            move = policy[p][q]
                        else:
                            p = p + 1
                            utility[j] += city[p][q]
                            move = policy[p][q]
                    else:
                        
                        if move == 'E':
                            if q == n - 1:
                                utility[j] += city[p][q]
                                move = policy[p][q]
                            else:
                                q = q + 1
                                utility[j] += city[p][q]
                                move = policy[p][q]
                                
                        else:
                            
                            if move == 'W':
                                if q == 0:
                                    utility[j] += city[p][q]
                                    move = policy[p][q]
                                else:
                                    q = q - 1
                                    utility[j] += city[p][q]
                                    move = policy[p][q]
                            
                            
                if move == 0:
                    break
                    
    final_val = int(math.floor(sum(utility) / float(len(utility))))
    final_val_list.append(final_val)
    
    
outputfile = open("output.txt", "w+")

for item in final_val_list:
    outputfile.write(str(item) + '\n')
outputfile.close()
        
            