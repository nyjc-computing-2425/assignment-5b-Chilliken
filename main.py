# Part 1
def read_csv(filename):
    # Type your code below
    
    full_data = open(filename,'r')
    x = full_data.readline()
    headers = x.split(",")
    
    data = []
    for i in full_data:
        i = i.strip()
        line = i.split(",")
        for j in range(len(line)):
            if line[j].isnumeric():
                line[j] = int(line[j])
            else:
                line[j] = str(line[j])
        data.append(line)
      
            
    
    return data 
    pass

# Part 2
def filter_gender(enrolment_by_age, sex):
    # Type your code below
    filter = []
    for i in enrolment_by_age:
        if i[2] == sex:
            del i[2]
            filter.append(i)
    return filter

    
    pass
    


# Part 3
def sum_by_year(enrolment):
    # Type your code below
    enrolment_by_year = []
    for i in range(1984,2018):
        sum = 0
        for j in enrolment:
            if j[0] == i:
                sum += j[-1]
        enrolment_by_year.append([i,sum])
    return enrolment_by_year
   

# Part 4
def write_csv(filename, header, data):
    # Type your code below
    sum = 0


    f = open(filename, 'w')
    f.write(",".join(header))
    for line in data:
        f.write(str(line))
        f.write('\n')
    f.close()
    for i in filename:
        sum +=1
    
    return sum
    pass


# TESTING
# You can write code below to call the above functions
# and test the output
# data = read_csv('pre-u-enrolment-by-age.csv')
# filter = filter_gender(data,"MF")
# enrolment_by_year = sum_by_year(filter)
# write_csv('total-enrolment-by-year.csv', ["year", "total_enrolment"], enrolment_by_year)
