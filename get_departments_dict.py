# we use the 420-people file as the input of cewit current faculty list.

# 1, read in cewit_420.csv and put every record into a tuple of 3 elements, like (fname, lname, email)
# 2, put these tuples into a list, named faculty_list
# 3, readin women_academic_appointees_08-21-2013.csv and put every record into a tuple of 4 elements, like (fname, lname, email, department)
# 4, put these tuples into a list, name iu_women_all_list
# 5, make a list from women_academin_appointees_80_21_2013 that consists of only department, named department_list
# 6, validate names and email between faculty_list and iu_women_list, if 420 in iu_women, put the person into a dict, named dep_fac_dict, like {"african studies":[person-1, person-2,...,persone-n]} 
# 7, if not, put the person in to a list, named, fac_no_dep_list

import csv
def get_cewit_420_list():
	with open('cewit_420.csv') as f:
		csv_content = csv.DictReader(f)
		cewit_faculty_list = []
		for row in csv_content:
			cewit_faculty_list.append((row['First Name'],row['Last Name'],row['Email Address']))
	
	return cewit_faculty_list

def get_department_list():
	with open() as f:

	return department_list

def get_dep_fac_dict():

	return dep_fac_dict

def get_dep2cewit_distance_dict():

	return dep2cewit_distance_dict

print get_cewit_420_list()