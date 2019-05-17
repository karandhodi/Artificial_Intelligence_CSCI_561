with open('input.txt') as inputfile:
    data = inputfile.readlines()
inputfile.close()

no_of_beds = int(data[0])
no_of_park_spaces = int(data[1])
no_of_LAHSA_so_far = int(data[2])

LAHSA_applicant_ID = []

for i in range(0, no_of_LAHSA_so_far):
    LAHSA_applicant_ID.append(data[3+i])
    
no_of_SPLA_so_far = int(data[ 2 + no_of_LAHSA_so_far + 1 ])

SPLA_applicant_ID = []

for i in range(0, no_of_SPLA_so_far):
    SPLA_applicant_ID.append(data[ 2 + no_of_LAHSA_so_far + 2 + i ])
    
no_of_applicants = int(data[ 2 + no_of_LAHSA_so_far + 1 + no_of_SPLA_so_far + 1])

applicants = []

for i in range(0, no_of_applicants):
    applicants.append(data[ 2 + no_of_LAHSA_so_far + 1 + no_of_SPLA_so_far + 2 + i])
    
no_of_beds_each_day = []

for i in range(0,7):
    no_of_beds_each_day.append(no_of_beds)
    
no_of_park_spaces_each_day = []

for i in range(0,7):
    no_of_park_spaces_each_day.append(no_of_park_spaces)
    
park_spaces_used_so_far = []
    
for i in range(len(SPLA_applicant_ID)):
    test_applicant_ID = SPLA_applicant_ID[i]
    for j in range(len(applicants)):
        test_applicant = applicants[j][0:5]
        if int(test_applicant_ID) == int(test_applicant):
            park_spaces_used_so_far.append(applicants[j][13:])
            del applicants[j]
            break
        
beds_used_so_far = []
    
for i in range(len(LAHSA_applicant_ID)):
    test_applicant_ID = LAHSA_applicant_ID[i]
    for j in range(len(applicants)):
        test_applicant = applicants[j][0:5]
        if int(test_applicant_ID) == int(test_applicant):
            beds_used_so_far.append(applicants[j][13:])
            del applicants[j]
            break
        
park_space_efficiency = 0
shelter_efficiency = 0

for i in range(len(park_spaces_used_so_far)):
    for j in range(0,7):
        if park_spaces_used_so_far[i][j] == '1':
            park_space_efficiency += 1
            no_of_park_spaces_each_day[j] -= 1
            
for i in range(len(beds_used_so_far)):
    for j in range(0,7):
        if beds_used_so_far[i][j] == '1':
            shelter_efficiency += 1
            no_of_beds_each_day[j] -= 1

applicants_temp = list(applicants)

applicants_SPLA_temp = list(applicants)
applicants_LAHSA_temp = list(applicants)

applicants_LAHSA = []
applicants_SPLA = []

park_space_efficiency_list = dict()
shelter_efficiency_list = dict()

park_space_efficiency_list_common = dict()
shelter_efficiency_list_common = dict()

loop_flag = 0

def sortApplicants(li):
    countDays = 0
    
    days = li[13:]
    
    for j in range(len(days)):
        if days[j] == '1':
            countDays += 1
            
    return countDays



for i in range(len(applicants_LAHSA_temp)):
    current_applicant_gender = applicants_LAHSA_temp[i][5]
    current_applicant_age = int(applicants_LAHSA_temp[i][6:9])
    current_applicant_pet = applicants_LAHSA_temp[i][9]
    
    if current_applicant_gender == 'M' or current_applicant_gender == 'O' or current_applicant_pet == 'Y' or current_applicant_age <= 17:
        t = 0
    else:
        applicants_LAHSA.append(applicants_LAHSA_temp[i])
        
      
for i in range(len(applicants_SPLA_temp)):
    current_applicant_medical = applicants_SPLA_temp[i][10]
    current_applicant_car = applicants_SPLA_temp[i][11]
    current_applicant_DL = applicants_SPLA_temp[i][12]
    
    if current_applicant_medical == 'Y' or current_applicant_car == 'N' or current_applicant_DL == 'N':
        t = 0
    else:
        applicants_SPLA.append(applicants_SPLA_temp[i])
        
            
for i in range(len(applicants_SPLA)):
    park_space_efficiency_list[applicants_SPLA[i][0:5]] = park_space_efficiency
    
for i in range(len(applicants_LAHSA)):
    shelter_efficiency_list[applicants_LAHSA[i][0:5]] = shelter_efficiency
    
for i in range(len(applicants_SPLA)):
    park_space_efficiency_list_common[applicants_SPLA[i][0:5]] = park_space_efficiency
    
for i in range(len(applicants_LAHSA)):
    shelter_efficiency_list_common[applicants_LAHSA[i][0:5]] = shelter_efficiency
    
park_spaces_string = dict()
shelter_string = dict()

for i in range(len(applicants_SPLA)):
    park_spaces_string[applicants_SPLA[i][0:5]] = applicants_SPLA[i][13:]
    
for i in range(len(applicants_LAHSA)):
    shelter_string[applicants_LAHSA[i][0:5]] = applicants_LAHSA[i][13:]
    
def func_SPLA (applicants_SPLA_list, applicants_LAHSA_list, next_SPLA_ID, next_LAHSA_ID, current_SPLA_ID, no_of_park_spaces_each_day_, no_of_beds_each_day_):
    
    if len(applicants_SPLA_list) == 0:
        return
    
    temp_no_of_park_spaces_each_day = list(no_of_park_spaces_each_day_)
    temp_efficiency = 0
    
    for j in range(0,7):
        if park_spaces_string[current_SPLA_ID][j] == '1':
            temp_efficiency += 1
            temp_no_of_park_spaces_each_day[j] -= 1
            
    flag = True
    
    for k in range(0,7):
        if temp_no_of_park_spaces_each_day[k] == -1:
            flag = False
            break
        
    if flag == True:
        park_space_efficiency_list[next_SPLA_ID] += temp_efficiency
        
        remaining_list_SPLA = [x for x in applicants_SPLA_list if x[0:5] != current_SPLA_ID]
       
        remaining_list_LAHSA = [x for x in applicants_LAHSA_list if x[0:5] != current_SPLA_ID]
        
        #print ("HELLO_SPLA")
        
        #remaining_list_SPLA.sort(key = sortApplicants, reverse = True)
        #remaining_list_LAHSA.sort(key = sortApplicants, reverse = True)
        
        if(len(remaining_list_SPLA) != 0 and len(remaining_list_LAHSA) != 0):
            
            func_LAHSA (remaining_list_SPLA, remaining_list_LAHSA, next_SPLA_ID, remaining_list_LAHSA[0][0:5], remaining_list_LAHSA[0][0:5], temp_no_of_park_spaces_each_day, no_of_beds_each_day_)
        else:
            if(len(remaining_list_SPLA) != 0 and len(remaining_list_LAHSA) == 0):
              
              func_SPLA (remaining_list_SPLA, [], next_SPLA_ID, "", remaining_list_SPLA[0][0:5], temp_no_of_park_spaces_each_day, no_of_beds_each_day_)  
            else:
                return
            
    else:
        
        remaining_list_SPLA = [x for x in applicants_SPLA_list if x[0:5] != current_SPLA_ID]
       
        remaining_list_LAHSA = applicants_LAHSA_list
        
        #print ("HELLO_SPLA")
        
        #remaining_list_SPLA.sort(key = sortApplicants, reverse = True)
        #remaining_list_LAHSA.sort(key = sortApplicants, reverse = True)
        
        if(len(remaining_list_SPLA) != 0 and len(remaining_list_LAHSA) != 0):
            
            func_LAHSA (remaining_list_SPLA, remaining_list_LAHSA, next_SPLA_ID, remaining_list_LAHSA[0][0:5], remaining_list_LAHSA[0][0:5], no_of_park_spaces_each_day_, no_of_beds_each_day_)
        else:
            if(len(remaining_list_SPLA) != 0 and len(remaining_list_LAHSA) == 0):
              
              func_SPLA (remaining_list_SPLA, [], next_SPLA_ID, "", remaining_list_SPLA[0][0:5], no_of_park_spaces_each_day_, no_of_beds_each_day_)  
            else:
                return
        
        
        
def func_LAHSA (applicants_SPLA_list, applicants_LAHSA_list, next_SPLA_ID, next_LAHSA_ID, current_LAHSA_ID, no_of_park_spaces_each_day_, no_of_beds_each_day_):
    
    if len(applicants_LAHSA_list) == 0:
        return
    
    temp_no_of_beds_each_day = list(no_of_beds_each_day_)
    temp_efficiency = 0
    
    for j in range(0,7):
        if shelter_string[current_LAHSA_ID][j] == '1':
            temp_efficiency += 1
            temp_no_of_beds_each_day[j] -= 1
            
    flag = True
    
    for k in range(0,7):
        if temp_no_of_beds_each_day[k] == -1:
            flag = False
            break
        
    if flag == True:
        shelter_efficiency_list[next_LAHSA_ID] += temp_efficiency
        
        
        remaining_list_SPLA = [x for x in applicants_SPLA_list if x[0:5] != current_LAHSA_ID]
         
        remaining_list_LAHSA = [x for x in applicants_LAHSA_list if x[0:5] != current_LAHSA_ID]
        
        #remaining_list_SPLA.sort(key = sortApplicants, reverse = True)
        #remaining_list_LAHSA.sort(key = sortApplicants, reverse = True)
        
        #print ("HELLO_LAHSA")
        
        if(len(remaining_list_SPLA) != 0 and len(remaining_list_LAHSA) != 0):
            
            func_SPLA (remaining_list_SPLA, remaining_list_LAHSA, next_SPLA_ID, next_LAHSA_ID, remaining_list_SPLA[0][0:5], no_of_park_spaces_each_day_, temp_no_of_beds_each_day)
        else:
            if(len(remaining_list_SPLA) == 0 and len(remaining_list_LAHSA) != 0):
                func_LAHSA ([], remaining_list_LAHSA, "", next_LAHSA_ID, remaining_list_LAHSA[0][0:5], no_of_park_spaces_each_day_, temp_no_of_beds_each_day)
            else:
                return
            
    else:
        
        remaining_list_SPLA = applicants_SPLA_list
         
        remaining_list_LAHSA = [x for x in applicants_LAHSA_list if x[0:5] != current_LAHSA_ID]
        
        #remaining_list_SPLA.sort(key = sortApplicants, reverse = True)
        #remaining_list_LAHSA.sort(key = sortApplicants, reverse = True)
        
        #print ("HELLO_LAHSA")
        
        if(len(remaining_list_SPLA) != 0 and len(remaining_list_LAHSA) != 0):
            
            func_SPLA (remaining_list_SPLA, remaining_list_LAHSA, next_SPLA_ID, next_LAHSA_ID, remaining_list_SPLA[0][0:5], no_of_park_spaces_each_day_, no_of_beds_each_day_)
        else:
            if(len(remaining_list_SPLA) == 0 and len(remaining_list_LAHSA) != 0):
                func_LAHSA ([], remaining_list_LAHSA, "", next_LAHSA_ID, remaining_list_LAHSA[0][0:5], no_of_park_spaces_each_day_, no_of_beds_each_day_)
            else:
                return
        
            
def func_SPLA_common (applicants_SPLA_list, applicants_LAHSA_list, next_SPLA_ID, next_LAHSA_ID, current_SPLA_ID, no_of_park_spaces_each_day_, no_of_beds_each_day_):
    
    if len(applicants_SPLA_list) == 0:
        return
    
    temp_no_of_park_spaces_each_day = list(no_of_park_spaces_each_day_)
    temp_efficiency = 0
    
    for j in range(0,7):
        if park_spaces_string[current_SPLA_ID][j] == '1':
            temp_efficiency += 1
            temp_no_of_park_spaces_each_day[j] -= 1
            
    flag = True
    
    for k in range(0,7):
        if temp_no_of_park_spaces_each_day[k] == -1:
            flag = False
            break
        
    if flag == True:
        park_space_efficiency_list_common[next_SPLA_ID] += temp_efficiency
        
        remaining_list_SPLA = [x for x in applicants_SPLA_list if x[0:5] != current_SPLA_ID]
       
        remaining_list_LAHSA = [x for x in applicants_LAHSA_list if x[0:5] != current_SPLA_ID]
        
        #print ("HELLO_SPLA")
        
        #remaining_list_SPLA.sort(key = sortApplicants, reverse = True)
        #remaining_list_LAHSA.sort(key = sortApplicants, reverse = True)
        
        if(len(remaining_list_SPLA) != 0 and len(remaining_list_LAHSA) != 0):
            
            func_LAHSA_common (remaining_list_SPLA, remaining_list_LAHSA, next_SPLA_ID, remaining_list_LAHSA[0][0:5], remaining_list_LAHSA[0][0:5], temp_no_of_park_spaces_each_day, no_of_beds_each_day_)
        else:
            if(len(remaining_list_SPLA) != 0 and len(remaining_list_LAHSA) == 0):
              
              func_SPLA_common (remaining_list_SPLA, [], next_SPLA_ID, "", remaining_list_SPLA[0][0:5], temp_no_of_park_spaces_each_day, no_of_beds_each_day_)  
            else:
                return
    else:
        
        
        remaining_list_SPLA = [x for x in applicants_SPLA_list if x[0:5] != current_SPLA_ID]
       
        remaining_list_LAHSA = applicants_LAHSA_list
        
        #print ("HELLO_SPLA")
        
        #remaining_list_SPLA.sort(key = sortApplicants, reverse = True)
        #remaining_list_LAHSA.sort(key = sortApplicants, reverse = True)
        
        if(len(remaining_list_SPLA) != 0 and len(remaining_list_LAHSA) != 0):
            
            func_LAHSA_common (remaining_list_SPLA, remaining_list_LAHSA, next_SPLA_ID, remaining_list_LAHSA[0][0:5], remaining_list_LAHSA[0][0:5], no_of_park_spaces_each_day_, no_of_beds_each_day_)
        else:
            if(len(remaining_list_SPLA) != 0 and len(remaining_list_LAHSA) == 0):
              
              func_SPLA_common (remaining_list_SPLA, [], next_SPLA_ID, "", remaining_list_SPLA[0][0:5], no_of_park_spaces_each_day_, no_of_beds_each_day_)  
            else:
                return
            
    
            
        
def func_LAHSA_common (applicants_SPLA_list, applicants_LAHSA_list, next_SPLA_ID, next_LAHSA_ID, current_LAHSA_ID, no_of_park_spaces_each_day_, no_of_beds_each_day_):
    
    if len(applicants_LAHSA_list) == 0:
        return
    
    temp_no_of_beds_each_day = list(no_of_beds_each_day_)
    temp_efficiency = 0
    
    for j in range(0,7):
        if shelter_string[current_LAHSA_ID][j] == '1':
            temp_efficiency += 1
            temp_no_of_beds_each_day[j] -= 1
            
    flag = True
    
    for k in range(0,7):
        if temp_no_of_beds_each_day[k] == -1:
            flag = False
            break
        
    if flag == True:
        shelter_efficiency_list_common[next_LAHSA_ID] += temp_efficiency
        
        
        remaining_list_SPLA = [x for x in applicants_SPLA_list if x[0:5] != current_LAHSA_ID]
         
        remaining_list_LAHSA = [x for x in applicants_LAHSA_list if x[0:5] != current_LAHSA_ID]
        
        #remaining_list_SPLA.sort(key = sortApplicants, reverse = True)
        #remaining_list_LAHSA.sort(key = sortApplicants, reverse = True)
        
        #print ("HELLO_LAHSA")
        
        if(len(remaining_list_SPLA) != 0 and len(remaining_list_LAHSA) != 0):
            
            func_SPLA_common (remaining_list_SPLA, remaining_list_LAHSA, next_SPLA_ID, next_LAHSA_ID, remaining_list_SPLA[0][0:5], no_of_park_spaces_each_day_, temp_no_of_beds_each_day)
        else:
            if(len(remaining_list_SPLA) == 0 and len(remaining_list_LAHSA) != 0):
                func_LAHSA_common ([], remaining_list_LAHSA, "", next_LAHSA_ID, remaining_list_LAHSA[0][0:5], no_of_park_spaces_each_day_, temp_no_of_beds_each_day)
            else:
                return
    else:
        remaining_list_SPLA = applicants_SPLA_list
         
        remaining_list_LAHSA = [x for x in applicants_LAHSA_list if x[0:5] != current_LAHSA_ID]
        
        #remaining_list_SPLA.sort(key = sortApplicants, reverse = True)
        #remaining_list_LAHSA.sort(key = sortApplicants, reverse = True)
        
        #print ("HELLO_LAHSA")
        
        if(len(remaining_list_SPLA) != 0 and len(remaining_list_LAHSA) != 0):
            
            func_SPLA_common (remaining_list_SPLA, remaining_list_LAHSA, next_SPLA_ID, next_LAHSA_ID, remaining_list_SPLA[0][0:5], no_of_park_spaces_each_day_, no_of_beds_each_day_)
        else:
            if(len(remaining_list_SPLA) == 0 and len(remaining_list_LAHSA) != 0):
                func_LAHSA_common ([], remaining_list_LAHSA, "", next_LAHSA_ID, remaining_list_LAHSA[0][0:5], no_of_park_spaces_each_day_, no_of_beds_each_day_)
            else:
                return
            
            
applicants_SPLA.sort(key = sortApplicants, reverse = True)
applicants_LAHSA.sort(key = sortApplicants, reverse = True)

applicants_SPLA_LAHSA_common = []
applicants_LAHSA_SPLA_common = []

for i in range(len(applicants_SPLA)):
    for j in range(len(applicants_LAHSA)):
        if applicants_SPLA[i][0:5] == applicants_LAHSA[j][0:5]:
            applicants_SPLA_LAHSA_common.append(applicants_SPLA[i])
            
for i in range(len(applicants_SPLA)):
    test_flag = 0
    for j in range(len(applicants_SPLA_LAHSA_common)):
        if applicants_SPLA[i][0:5] != applicants_SPLA_LAHSA_common[j][0:5]:
            t = 0 
        else:
            test_flag = 1
            break
    if j == len(applicants_SPLA_LAHSA_common) - 1 and test_flag == 0:
        applicants_SPLA_LAHSA_common.append(applicants_SPLA[i])
        
for i in range(len(applicants_LAHSA)):
    for j in range(len(applicants_SPLA)):
        if applicants_LAHSA[i][0:5] == applicants_SPLA[j][0:5]:
            applicants_LAHSA_SPLA_common.append(applicants_LAHSA[i])
            
for i in range(len(applicants_LAHSA)):
    test_flag = 0
    for j in range(len(applicants_LAHSA_SPLA_common)):
        if applicants_LAHSA[i][0:5] != applicants_LAHSA_SPLA_common[j][0:5]:
            t = 0 
        else:
            test_flag = 1
            break
    if j == len(applicants_LAHSA_SPLA_common) - 1 and test_flag == 0:
        applicants_LAHSA_SPLA_common.append(applicants_LAHSA[i])
        
        
for i in range(len(applicants_SPLA)):
    func_SPLA(applicants_SPLA, applicants_LAHSA, applicants_SPLA[i][0:5], "", applicants_SPLA[i][0:5], no_of_park_spaces_each_day, no_of_beds_each_day)
 
for i in range(len(applicants_SPLA_LAHSA_common)):
    func_SPLA_common(applicants_SPLA_LAHSA_common, applicants_LAHSA_SPLA_common, applicants_SPLA_LAHSA_common[i][0:5], "", applicants_SPLA_LAHSA_common[i][0:5], no_of_park_spaces_each_day, no_of_beds_each_day)
    
final_eff = dict()

for i in park_space_efficiency_list:
    for j in park_space_efficiency_list_common:
        if i == j:
            final_eff[i] = max(park_space_efficiency_list[i], park_space_efficiency_list_common[j])
               
outputfile = open("output.txt","w+")
outputfile.write(max(final_eff, key=final_eff.get) + '\n')   
outputfile.close()
                
        
                
    
    
