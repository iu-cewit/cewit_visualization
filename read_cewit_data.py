# we use the 420-people file as the input of cewit current faculty list.

# 1, read in cewit_420.csv and put every record into a tuple of 3 elements, like (fname, lname, email)
# 2, put these tuples into a list, named faculty_list
# 3, readin women_academic_appointees_08-21-2013.csv and put every record into a tuple of 4 elements, like (fname, lname, email, department)
# 4, put these tuples into a list, name iu_women_all_list
# 5, make a list from women_academin_appointees_80_21_2013 that consists of only department, named department_list
# 6, validate names and email between faculty_list and iu_women_list, if 420 in iu_women, put the person into a dict, named dep_fac_dict, like {"african studies":[person-1, person-2,...,persone-n]} 
# 7, if not, put the person in to a list, named, fac_no_dep_list

import csv
import pprint
def get_cewit_420_list():
	with open('cewit_420.csv') as f:
		csv_content = csv.DictReader(f)
		cewit_faculty_list = []
		for row in csv_content:
			# cewit_faculty_list.append((row['First Name'],row['Last Name'],row['Email Address']))
			cewit_faculty_list.append((row['First Name'].lower(),row['Last Name'].lower()))

	cewit_faculty_list = [i for i in set(cewit_faculty_list)] # in case there are duplicate data
	return cewit_faculty_list

# because there are also data from cewit's website, so we need to get a list of department and a dict of dep_factult from those information.
def get_from_cewit_website():
	with open('cewit_faculty_from_website.csv') as f:
		csv_content = csv.DictReader(f)
		# dep_list_website = []
		# dep_fac_dict_website = {}
		cewit_faculty_website_list = []
		cewit_faculty_website_dep_list = []
		for row in csv_content:
			# dep_list_website.append(row['School/Department'])
			cewit_faculty_website_list.append((row['Name'].split(',')[1].strip().lower(), row['Name'].split(',')[0].lower()))
			cewit_faculty_website_dep_list.append((row['Name'].split(',')[1].strip().lower(), row['Name'].split(',')[0].lower(),row['School/Department']))

		# if ('Muhammad'.lower(), 'Abdul-Mageed'.lower()) in cewit_faculty_website_list:
		# 	print 'Muhammad is here'
		cewit_faculty_website_list = [i for i in set(cewit_faculty_website_list)]

	return cewit_faculty_website_list, cewit_faculty_website_dep_list 



def get_department_list():
	with open('Women_academic_appointees_08-21-2013.csv') as f:
		csv_content = csv.DictReader(f)
		dep_list = []
		for row in csv_content:
			dep_list.append(row['Department'])
	dep_list = [i for i in set(dep_list)]
	return dep_list

def get_dep_fac_dict(cewit_faculty_list):
	with open('Women_academic_appointees_08-21-2013.csv') as f:
		csv_content = csv.DictReader(f)
		dep_fac_dict = {}
		all_women_list = []
		remaining_list = cewit_faculty_list
		iu_dep_list = []
		for row in csv_content:
			# all_women_list.append((row['First Name'],row['Last Name'],row['Email'],row['Department']))
			all_women_list.append((row['First Name'].lower(),row['Last Name'].lower(),row['Department']))
			iu_dep_list.append(row['Department'])
		iu_dep_list = [i for i in set(iu_dep_list)]

		for w in all_women_list:
			w_tuple = (w[0],w[1])
			if w_tuple in cewit_faculty_list:
				dep_fac_dict.setdefault(w[2],[]).append(w_tuple)
				remaining_list.remove(w_tuple)


	return dep_fac_dict, remaining_list, all_women_list, iu_dep_list




# def get_dep2cewit_distance_dict():

# 	return dep2cewit_distance_dict

names_420 = get_cewit_420_list()
names_website, names_dep_website = get_from_cewit_website()
# print names_420
# print names_website
names = names_420 + names_website

names = [i for i in set(names)]
print len(names)
# print len(get_department_list())
# cewit_faculty_list=get_cewit_420_list()
dep_fac_dict, remaining_list, all_women_list, iu_dep_list= get_dep_fac_dict(names)

# print remaining_list
# print all_women_list
# for w in all_women_list:
# 	if (w[0],w[1]) in remaining_list:
# 		remaining_filtered_list.append(w)
dep_fac_website_remaining = {}
for w in names_dep_website:
	if (w[0],w[1]) in remaining_list:
		dep_fac_website_remaining.setdefault(w[2],[]).append((w[0],w[1]))

		remaining_list.remove((w[0],w[1]))

print len(remaining_list)
print remaining_list
# pprint.pprint(dep_fac_website_remaining)
# pprint.pprint(dep_fac_dict)
# print dep_fac_website_remaining.keys()
# print iu_dep_list
# print dep_fac_dict.keys()






