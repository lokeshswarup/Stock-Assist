from bs4 import BeautifulSoup
import requests
import time
import csv
file=open(file="ccp.csv",mode="w")
csvw=csv.writer(file)
csvrow=["S.No.","Name","Market Cap","Current Price","High/Low","Stock P/E","Book Value","Dividend Yield","ROCE","ROE","Face Value"]
csvw.writerow(csvrow)
count=0
for i in range(1,4):
        
    url=f"https://www.screener.in/screens/57601/coffee-can-portfolio/?limit=25&page={i}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"html.parser")
    data = soup.find('table')
    tabledata = data.find_all('a')
    for ln in tabledata:
        
        x=ln.get('href')
        y=x.split('/')
        if "company" in y:
            datarow=[]
            print(y[2])
            link=requests.get("https://www.screener.in/"+x)
            stocklink=BeautifulSoup(link.content,"html.parser")
            completedata=stocklink.find_all(class_="number")
            count+=1
            datarow.append(str(count))
            datarow.append(str(y[2]))
            datarow.append(completedata[0].get_text())
            datarow.append(completedata[1].get_text())
            datarow.append(completedata[2].get_text()+"/"+completedata[3].get_text())
            datarow.append(completedata[4].get_text())
            datarow.append(completedata[5].get_text())
            datarow.append(completedata[6].get_text())
            datarow.append(completedata[7].get_text())
            datarow.append(completedata[8].get_text())
            datarow.append(completedata[9].get_text())
            csvw.writerow(datarow)
            time.sleep(2)
