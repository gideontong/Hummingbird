import csv
import random
import math

instruction = {
    'race' : {
        0: 1.5, # White
        1: .9,   # Black
        2: 1.2, # Asian
        3: 0.8, # Latino
        4: .7,  # Indigenous
        5: .8,  # Pacific
    },
    'gender' : {
        0: 1,    # Male
        1: 0.83, # Female
    },
    'job' : {
        0: .5,  # Janitor
        1: 1,   # Cashier
        2: 1.5, # Engineer
        3: 10   # Executive
    },
    'year' : {
        0: 0.8,  # Janitor
        1: 0.9,   # Cashier
        2: 0.95, # Engineer
        3: 1   # Executive
    }
}

test_instruction = {
    'race' : {
        0: 1, # White
        1: 1,   # Black
        2: 1, # Asian
        3: 1, # Latino
        4: 1,  # Indigenous
        5: 1,  # Pacific
    },
    'gender' : {
        0: 1,    # Male
        1: 1, # Female
    },
    'job' : {
        0: 1,  # Janitor
        1: 1,   # Cashier
        2: 1, # Engineer
        3: 1   # Executive
    },
    'year' : {
        0: 1,  # Janitor
        1: 1.2,   # Cashier
        2: 2, # Engineer
        3: 5   # Executive
    }
}

def parse(file):
    with open(file, 'r') as data:
        csvData = csv.reader(data)
        return csvData

def generateCSV(sample_size, sample_instructions, global_mean, global_std):
    answer = []
    for person in range(sample_size):
        person_attributes = []
        weighed_mean = global_mean
        for discriminating_factor in list(sample_instructions):
            factor_types = sample_instructions[discriminating_factor]
            selected_attribute = random.choice(list(factor_types))
            weighed_mean *= factor_types[selected_attribute]
            person_attributes += [selected_attribute]
        person_attributes += [math.floor(abs(int(100*random.gauss(weighed_mean, global_std))/100))]
        answer.append(person_attributes)
    createCSV(answer)
    return answer

def createCSV(lists):
    with open('rlyunfairsampledata.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(['race', 'gender', 'job', 'salary'])
        for row in lists:
            thewriter.writerow(row)

def main():
    for person in generateCSV(1500, instruction, 100000, 10000):
        print(person)
