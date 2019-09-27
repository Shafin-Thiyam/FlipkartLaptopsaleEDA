#webscrapping 

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url ='https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_pr&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_pr&as-pos=1&as-type=RECENT&suggestionId=mobiles&requestId=1f63d1ba-fe08-4298-8fb3-7a0dbb867dbb&as-searchtext=mobilr'

uClient =uReq(my_url)
try:
    page_html=uClient.read()
except httplib.IncompleteRead as e:
    page_html = e.partial
    
uClient.close()
page_soup=soup(page_html,"html.parser")

containers=page_soup.findAll("div",{"class": "_3wU53n"})#t-0M7P _2doH3V  col_2-gKeQ
print("length:",len(containers))

containers_prices=page_soup.findAll("div",{"class": "_1vC4OE _2rQ-NK"}) # price
print("length of price:",len(containers_prices))

containers_ratings=page_soup.findAll("div",{"class": "niH0FQ"}) # price
print("length of ratings:",len(containers_ratings))



#print(BeautifulSoup.prettify(containers[0]))

container=containers[0]
containers_rating=containers_ratings[0]
print(container)
print(containers_rating)
#print(container.div.img["alt"])

#productname=container.search("div")
#productname=container.findAll("div",{"class":"_3wU53n"})

#for container in containers:
    #print(container.text)


#price=container.findAll("div",{"class:col col-5-12_2o7WAb"})
#print(price[0].text)

#ratings=container.findAll("div",{"class":"niH0FQ"})
#print(ratings[0].text)

filename="products.csv"
f= open(filename,"w")


headers="Product_Name,Pricing,Rating\n"
f.write(headers)

for container in containers:
    i=0
    product_name =container.text
    product_price =containers_prices[i].text.strip()
    #print(product_price)
    product_rate =containers_ratings[i].text.strip()
    print(product_rate[0:4])
    i=i+1
    #price_container = container.findAll("div", {"class": "col col-5-12_2o7WAb"})
    #price=price_container[0].text.strip()
    
    #rating_container = container.findAll("div", {"class": "niH0FQ"})
    #rating = rating_container[0].text
    
    #print("product_name:" + product_name)
    #print("price:"+price)
    #print("ratings:"+rating)
    
    #string parsing
    trim_price = ''.join(product_price.split(','))
    rm_rupee = trim_price.split("₹")
    add_rs_price="Rs." + rm_rupee[1]
    #split_price=add_rs_price.split('E')
    #final_price=split_price[0]
    
    
   # split_rating = rating.split(" ")
   # final_rating = split_rating[0]
    
   # print(product_name.replace(",", "|") + "," + final_price + "," + final_rating +"\n")
   # f.write(product_name.replace(",", "|") +"," + final_price + "," + final_rating +"\n")
    
    print(product_name.replace(",", "|")+"," + add_rs_price +"," + product_rate[0:4] +"\n")
    f.write(product_name.replace(",", "|")+"," + add_rs_price +"," + product_rate[0:4] +"\n")

f.close()
