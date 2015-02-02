import sys

def check(week,str):
	if len(str)>3:
		if str.lower() in week:
			print "yes"
		else:
			print "no"
	else:
		new_str=str.lower()
		if new_str in week:
			print "yes"
		else:
			print "no"

week=["sat","sun","mon","tue","wed","thr","fri","saturday","sunday","monday","tuesday","wednesday","thrusday","friday"]

check(week,sys.argv[1])