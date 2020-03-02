import csv
def classifier(gp):
    with open('result.csv','a',newline='\n') as file:
        writer=csv.writer(file)
        for i in gp:
            writer.writerow([i,gp[i],0])
        file.close()    
