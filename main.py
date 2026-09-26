score=float(input("Enter your exam    persentage score (0-100):"))
if score > 100 or score < 0:
	        print("invalid score ! Please enter between 0.aor 100.")
elif score>=90:
		    print("Result: Pass| A grade ")
elif score >= 80 :
			print("Result : Pass | B grade ")
elif score >= 70 :
	        print("Result : Pass | C grade ")
elif score >= 60 :
	    	print("Result : Pass | D grade ")
else :
	    	print("Result : Fail | F grade , please Try again for best")