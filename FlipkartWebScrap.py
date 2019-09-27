from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

filename="data/laptop.csv"
f= open(filename,"w")
headers="Brand,Product,Display,RAM,DDR/SDR,HardDisk,Processor,OS,Pricing,Customer,Rating\n"
f.write(headers)

for i in range(20):
    j=i+1
    uClient =uReq('https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_3_na_na_pr&otracker1=AS_QueryStore_OrganicAutoSuggest_0_3_na_na_pr&as-pos=0&as-type=RECENT&suggestionId=laptop&requestId=3af7f76b-cfdc-490d-a3cb-3dec368ee49d&as-backfill=on'+'&page='+str(i+1))
    try:
        page_html=uClient.read()
    except httplib.IncompleteRead as e:
        page_html = e.partial
        
    uClient.close()
    page_soup=soup(page_html,"html.parser")
    containers=page_soup.findAll("div",{"class": "_3wU53n"})#t-0M7P _2doH3V  col_2-gKeQ
    containers_prices=page_soup.findAll("div",{"class": "_1vC4OE _2rQ-NK"}) # price
    containers_ratings=page_soup.findAll("div",{"class": "hGSR34"}) # rating
    noOfCust=page_soup.findAll("span",{"class": "_38sUEc"})# customer count
    ul_specs=page_soup.findAll("ul",{"class":"vFw0gD"})
             
    for (c, p, r, s, cst) in zip(containers, containers_prices, containers_ratings, ul_specs, noOfCust):
        brandName=c.text.split(' ')[0].upper()
        product_name =c.text
        product_price =p.text.strip()
        product_rate =r.text.strip()
        trim_price = ''.join(product_price.split(','))
        rm_rupee = trim_price.split("₹")
        add_rs_price=rm_rupee[1]
        custCount = cst.text.split('Ratings')[0].replace(',','').strip()
        proc=""
        disp=""
        ram=""
        ddrsdr=""
        HardDisk=""
        OS=""
        for config in s.findAll("li",{"class":"tVe95H"}):
            conf=config.text
            if ('SSD' in conf and conf.endswith('SSD')) or ('HDD' in conf and conf.endswith('HDD')) :
                HardDisk=conf
            elif 'Operating System' in conf:
                OS=conf.split('Operating System')[0].strip().replace(",", " ")
            elif 'RAM' in conf:
                ram=conf.split('RAM')[0].strip()
                if 'DDR' in conf.split('RAM')[0].strip():
                    ddrsdr= 'DDR'
                elif 'SDR' in conf.split('RAM')[0].strip():
                    ddrsdr= 'SDR'
            elif 'Display' in conf:
                try:
                    disp=conf.split('Display')[0].split('(')[1].split('inch)')[0].strip().replace(",", " ")
                except Exception as e:
                    disp=conf
            elif 'Processor' in conf:
                proc=''.join(conf.split('Processor')).strip()
        f.write(brandName+","+product_name.replace(",", "|")+","+disp+","+ram+","+ddrsdr+","+HardDisk+","+proc+","+OS+","+add_rs_price +","+ custCount +"," + product_rate[0:4] +"\n")
f.close()