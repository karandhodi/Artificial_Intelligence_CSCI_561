import copy

with open('input.txt') as inputfile:
    data = inputfile.readlines()
inputfile.close()

scooter_positions = data[3:]

count_scooter_positions = dict()

for i in scooter_positions:
  count_scooter_positions[i] = count_scooter_positions.get(i, 0) + 1
  
max_scooter_key = max(count_scooter_positions, key=count_scooter_positions.get)
max_scooter_key_value = count_scooter_positions[max_scooter_key]

max_scooter_key_list = []
max_scooter_key_X = []
max_scooter_key_Y = []

for i in count_scooter_positions:
    if count_scooter_positions[i] == max_scooter_key_value:
        max_scooter_key_list.append(i)
        
n = int(data[0])
p = int(data[1])
#p = 1
police_placed = p

s = int(data[2])

def give_city_grid():
    city = [0] * n
    for row in range(n):
        city[row] = [0] * n
    return city

def add_result(city):
    result_city = copy.deepcopy(city)
    results.append(result_city)

def print_results(results, n):
    for res in results:
        for row in res:
            print(row)
        print()
        
def place_police_officers(city, column, n):
    
    if column >= n:
        return
    
    for i in range(n):
        if placement_possible(city, i, column, n):
            city[i][column] = 1
            if column == n - 1:
                add_result(city)
                city[i][column] = 0
                return
            place_police_officers(city, column + 1, n)
            city[i][column] = 0
            
def placement_possible(city, row, column, n):
    
    for icolumn in range(column):
        if city[row][icolumn] == 1:
            return False
        
    irow, icolumn = row, column
    while irow >= 0 and icolumn >= 0:
        if city[irow][icolumn] == 1:
            return False
        irow = irow - 1
        icolumn = icolumn - 1
    
    jrow, jcolumn = row, column
    while jrow < n and jcolumn >= 0:
        if city[jrow][jcolumn] == 1:
            return False
        jrow = jrow + 1
        jcolumn = jcolumn - 1
    
    return True

city = give_city_grid()
results = []

if ( p == n ):
    place_police_officers(city, 0, n)
     
else:
    for i in range (len(max_scooter_key_list)):
        del count_scooter_positions[max_scooter_key_list[i]]
        max_scooter_key_X.append(int(max_scooter_key_list[i][2:]))
        max_scooter_key_Y.append(int(max_scooter_key_list[i][0]))
        
        #city[max_scooter_key_X[0]][max_scooter_key_Y[0]] = 1
        #city[max_scooter_key_X[1]][max_scooter_key_Y[1]] = 1
    
    for i in range (len(max_scooter_key_X)):
        city[max_scooter_key_X[i]][max_scooter_key_Y[i]] = 1
        police_placed -= 1
        if police_placed == 0:
            add_result(city)
            city = give_city_grid()
            police_placed = p
        else:
            while (police_placed > 0 and len(count_scooter_positions) > 0):
                other_scooter_key = max(count_scooter_positions, key=count_scooter_positions.get)
                other_scooter_key_X = int(other_scooter_key[2:])
                other_scooter_key_Y = int(other_scooter_key[0])
                
                place_flag = True
                
                for icolumn in range(other_scooter_key_Y):
                    if city[other_scooter_key_X][icolumn] == 1:
                        place_flag = False
                        
                for icolumn in range(other_scooter_key_Y, n):
                    if city[other_scooter_key_X][icolumn] == 1:
                        place_flag = False
                        
                for irow in range(other_scooter_key_X):
                    if city[irow][other_scooter_key_Y] == 1:
                        place_flag = False
                        
                for irow in range(other_scooter_key_X, n):
                    if city[irow][other_scooter_key_Y] == 1:
                        place_flag = False
            
                irow, icolumn = other_scooter_key_X, other_scooter_key_Y
                while irow >= 0 and icolumn >= 0:
                    if city[irow][icolumn] == 1:
                        place_flag = False
                    irow = irow - 1
                    icolumn = icolumn - 1
                    
                irow, icolumn = other_scooter_key_X, other_scooter_key_Y
                while irow < n and icolumn < n:
                    if city[irow][icolumn] == 1:
                        place_flag = False
                    irow = irow + 1
                    icolumn = icolumn + 1
        
                jrow, jcolumn = other_scooter_key_X, other_scooter_key_Y
                while jrow < n and jcolumn >= 0:
                    if city[jrow][jcolumn] == 1:
                        place_flag = False
                    jrow = jrow + 1
                    jcolumn = jcolumn - 1
                    
                jrow, jcolumn = other_scooter_key_X, other_scooter_key_Y
                while jrow >= 0 and jcolumn < n:
                    if city[jrow][jcolumn] == 1:
                        place_flag = False
                    jrow = jrow - 1
                    jcolumn = jcolumn + 1
                
                if place_flag:
                    city[other_scooter_key_X][other_scooter_key_Y] = 1
                    del count_scooter_positions[other_scooter_key]
                    police_placed -= 1
                else:
                    del count_scooter_positions[other_scooter_key]
                    
            add_result(city)
            city = give_city_grid()
            police_placed = p
            
            count_scooter_positions = dict()
            
            for j in scooter_positions:
                count_scooter_positions[j] = count_scooter_positions.get(j, 0) + 1
      
            max_scooter_key = max(count_scooter_positions, key=count_scooter_positions.get)
            
            max_scooter_key_list = []
            for k in count_scooter_positions:
                if count_scooter_positions[k] == max_scooter_key_value:
                    max_scooter_key_list.append(k)
                    
            for m in range (len(max_scooter_key_list)):
                del count_scooter_positions[max_scooter_key_list[m]]
                
    count_scooter_positions = dict()
    
    for j in scooter_positions:
                count_scooter_positions[j] = count_scooter_positions.get(j, 0) + 1
  
result_values = [0] * len(results)   

count_scooter_positions_X = []
count_scooter_positions_Y = []  

for i in count_scooter_positions:
    count_scooter_positions_X.append(i[2:])
    count_scooter_positions_Y.append(i[0])

value = 0  


for result in results:
    for r in range(n):
        for c in range(n):
            for i in range (len(count_scooter_positions_X)):
                if int(count_scooter_positions_X[i]) == r and int(count_scooter_positions_Y[i]) == c and result[r][c] == 1:
                    result_values[value]+=count_scooter_positions[''+str(count_scooter_positions_Y[i]).rstrip()+','+str(count_scooter_positions_X[i])]
    value+=1                
            
        
outputfile = open("output.txt","w+")
outputfile.write(str(max(result_values))+'\n')   
outputfile.close()  
        
#print_results(results, n)
