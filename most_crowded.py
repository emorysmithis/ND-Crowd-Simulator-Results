#!/usr/bin/env python3

import pprint
from os import walk

# Filename path information
path = '600_students/speeds_batch/'
_, _, filenames = next(walk(path))

# Dictionary with most and least crowded conditions
max_dict = {'num_late': 0,\
            'num_late_cond': '',\
            'max_sidewalk': 0,\
            'max_sidewalk_cond': '',\
            'max_average': 0,\
            'max_average_cond': ''}

min_dict = {'min_sidewalk': float('inf'),\
            'min_sidewalk_cond': '',\
            'min_average': float('inf'),\
            'min_average_cond': ''}


# Iterate through each output file
for filename in filenames:
    should_read = False
    with open(path+filename, 'r') as f:
        temp = 0

        # Find percentages
        a = int(filename.split('_')[2])
        b = int(filename.split('_')[3].split('.')[0])
        c = 100 - a - b
        percentages = [str(a), str(b), str(c)]

        # Iterate through each line
        for line in f:

            # Add min/max_sidewalk information
            if 'CROWDED EDGES' in line:
                sidewalk = int(f.readline().strip().split(' ')[1])
                if sidewalk > max_dict['max_sidewalk']:
                    max_dict['max_sidewalk'] = sidewalk
                    max_dict['max_sidewalk_cond'] = '-'.join(percentages)
                if sidewalk < min_dict['min_sidewalk']:
                    min_dict['min_sidewalk'] = sidewalk
                    min_dict['min_sidewalk_cond'] = '-'.join(percentages)

                temp = sidewalk
                should_read = True
                continue

            elif 'LATE PERCENTAGE' in line:

                # Add min/max_average information
                average = temp / 50.0
                if average > max_dict['max_average']:
                    max_dict['max_average'] = average
                    max_dict['max_average_cond'] = '-'.join(percentages)
                if average < min_dict['min_average']:
                    min_dict['min_average'] = average
                    min_dict['min_average_cond'] = '-'.join(percentages)


                # Add num_late information
                line = f.readline()
                line = f.readline()
                num_late = int(line.strip().split(':')[1].split(' ')[1])
                if num_late > max_dict['num_late']:
                    max_dict['num_late'] = num_late
                    max_dict['num_late_cond'] = '-'.join(percentages)
                break

            # Increment temp
            if should_read:
                temp += int(line.strip().split(' ')[1])

# Prints the nicely formatted dictionary
pprint.pprint(max_dict)
pprint.pprint(min_dict)
