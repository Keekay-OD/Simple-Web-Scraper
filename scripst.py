
from urllib.request import urlopen as UReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&browsedCategory=pcmcat333800050003&cp=1&id=pcat17071&iht=n&ks=960&list=y&qp=currentoffers_facet%3DCurrent%20Deals~On%20Sale&sc=Global&st=pcmcat333800050003_categoryid%24abcat0101001&type=page&usc=All%20Categories"

#opening up connectionm, grabbing the page 


uClient = UReq(my_url)
page_html = uClient.read()
uClient.close()



#HTML PARSER 
page_soup = soup(page_html, "html.parser")

#Grabs Each Product
containers = page_soup.findAll("li",{"class":"sku-item"})

## div class sku-item
filename = "products.csv"
f = open(filename, "w")



headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:
        title_container = container.div.h4.a.text
        
        model = container.findAll("span",{"class":"sku-value"})
        product_model = model[0].text

        price = container.findAll("div",{"class":"priceView-hero-price priceView-purchase-price"})
        product_price = price[0].text

        print("Brand: " + title_container)
        print("Model: " + product_model)
        print("Price: " + product_price)
	
f.write(title_container +  "," + product_model + "," +  product_price + "\n")

f.close()
