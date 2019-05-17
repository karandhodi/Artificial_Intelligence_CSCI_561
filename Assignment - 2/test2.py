with open('input2.txt') as inputfile:
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

for i in range(len(park_spaces_used_so_far)):
    for j in range(0,7):
        if park_spaces_used_so_far[i][j] == '1':
            park_space_efficiency += 1
            no_of_park_spaces_each_day[j] -= 1
            
for i in range(len(beds_used_so_far)):
    for j in range(0,7):
        if beds_used_so_far[i][j] == '1':
            no_of_beds_each_day[j] -= 1

applicants_temp = list(applicants)
applicants_temp_1 = list(applicants)

park_space_efficiency_list = []
loop_flag = 0

while(1):

    for i in range(len(applicants_temp)):
        current_applicant_gender = applicants_temp[i][5]
        current_applicant_age = int(applicants_temp[i][6:9])
        current_applicant_pet = applicants_temp[i][9]
        
        if current_applicant_gender == 'M' or current_applicant_pet == 'Y' or current_applicant_age <= 17:
            del applicants_temp[i]
            break
        
    if (i == len(applicants_temp) - 1 or i == len(applicants_temp)) and len(applicants_temp) != 1: 
        break
    else:
        if len(applicants_temp) == 1 and loop_flag == 0:
            loop_flag = 1
        else:
            if loop_flag == 1:
                break
   
loop_flag = 0      
        
def sortApplicants(li):
    countDays = 0
    
    days = li[13:]
    
    for j in range(len(days)):
        if days[j] == '1':
            countDays += 1
            
    return countDays


if len(applicants_temp) != 0:
    
    while(1):

        for i in range(len(applicants_temp)):
            current_applicant_medical = applicants_temp[i][10]
            current_applicant_car = applicants_temp[i][11]
            current_applicant_DL = applicants_temp[i][12]
            
            if current_applicant_medical == 'Y' or current_applicant_car == 'N' or current_applicant_DL == 'N':
                del applicants_temp[i]
                break
            
        if (i == len(applicants_temp) - 1 or i == len(applicants_temp)) and len(applicants_temp) != 1: 
            break
        else:
            if len(applicants_temp) == 1 and loop_flag == 0:
                loop_flag = 1
            else:
                if loop_flag == 1:
                    break
    
    applicants_temp.sort(key = sortApplicants, reverse = True)
    
    for i in range(len(applicants_temp)):
        temp_no_of_park_spaces_each_day = list(no_of_park_spaces_each_day)
        for j in range(0,7):
            if applicants_temp[i][j+13] == '1':
                temp_no_of_park_spaces_each_day[j] -= 1
                
        flag = True
        
        for k in range(0,7):
            if temp_no_of_park_spaces_each_day[k] == -1:
                flag = False
                break
            
        if flag == True:
            no_of_park_spaces_each_day = list(temp_no_of_park_spaces_each_day)
            outputfile = open("output.txt","w+")
            outputfile.write(applicants_temp[i][0:5] + '\n')   
            outputfile.close() 
            break
        
else:
    
    while(1):

        for i in range(len(applicants_temp_1)):
            current_applicant_medical = applicants_temp_1[i][10]
            current_applicant_car = applicants_temp_1[i][11]
            current_applicant_DL = applicants_temp_1[i][12]
            
            if current_applicant_medical == 'Y' or current_applicant_car == 'N' or current_applicant_DL == 'N':
                del applicants_temp_1[i]
                break
            
        if (i == len(applicants_temp) - 1 or i == len(applicants_temp)) and len(applicants_temp) != 1: 
            break
        else:
            if len(applicants_temp) == 1 and loop_flag == 0:
                loop_flag = 1
            else:
                if loop_flag == 1:
                    break
    
    applicants_temp_1.sort(key = sortApplicants, reverse = True)
    
    for i in range(len(applicants_temp_1)):
        temp_no_of_park_spaces_each_day = list(no_of_park_spaces_each_day)
        for j in range(0,7):
            if applicants_temp_1[i][j+13] == '1':
                temp_no_of_park_spaces_each_day[j] -= 1
                
        flag = True
        
        for k in range(0,7):
            if temp_no_of_park_spaces_each_day[k] == -1:
                flag = False
                break
            
        if flag == True:
            no_of_park_spaces_each_day = list(temp_no_of_park_spaces_each_day)
            outputfile = open("output.txt","w+")
            outputfile.write(applicants_temp_1[i][0:5] + '\n')   
            outputfile.close() 
            break
    
    
