str_list = ["george", "lennon", "soup", "pilaf", "gogo"]
str_list1 = ["{i} - {string}".format(i=str(str_list.index(st) + 1), string=st) for st in str_list]