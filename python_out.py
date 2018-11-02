#!/usr/bin/python

def main ():
    with open("\\\\kunx0014\\compot\\Assyst_Auftraege\\XREF_S100\\5_prod\\s100-24\\R113147-host.select_2018.07.26_16.10.46.csv", 'r') as outfile:
        for csvline in outfile:
            print (csvline)
    f.close()
	
if __name__== "main":
	main()