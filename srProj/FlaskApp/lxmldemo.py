import lxml.html as lh
from urllib.request import urlopen
import requests
# print(lh.parse("artificial_intelligenceWikipedia.html"))

url="https://en.wikipedia.org/wiki/Machine"
url2="https://en.wikipedia.org/wiki/Artificial_intelligence"
# print(fromstring(url))
# doc=lh.parse(urlopen(url2))
def parsePage(url):
	page = requests.get(url)
	tree = lh.fromstring(page.content)	
	# intro = tree.xpath("//*[@id=\"mw-content-text\"]/div/p/text()")
	intro = tree.xpath("//*[@id=\"mw-content-text\"]/div//p")
	print("intro")
	print("-------------------")
	for i in range(len(intro)):
		print(intro[i].xpath("string()"))
		# print(tree.xpath("//*[@id=\"mw-content-text\"]/div//p["+str(i+1)+"]/text()"))
		print("----")
		if intro[i].xpath("string()")=="":
			# print("'"+str(intro[i].xpath("string()"))+"'")
			print("intro end ---------------")
			print()
			print("body")
			print("----------------")
	print("body end -------------------")
	toc = tree.xpath("//*[@id=\"toc\"]/ul/li//a/@href")
	firstHeader = tree.xpath("//*[@id=\"mw-content-text\"]/div/h2")
	tocRel = firstHeader[0].xpath("/self::*/preceding-sibling::*//li")
	print("toc attempt")
	print(tocRel[0])
	print("firstHeader")
	print(firstHeader[0].xpath("string()"))
# //*[@id="mw-content-text"]/div/div[3]
# //*[@id="mw-content-text"]/div/div[3]
# //*[@id="toc"]
# print(intro)	


# print("contents")
# print("-------------------")
# print(toc)
# print()
# print("references")
# print("------------------------")
# references= tree.xpath("//*[@id=\"References\"]/parent::*/following-sibling::*//li")
# for i in range(len(references)):
# 	print(references[i].xpath("string()"))


# print(intro[1].xpath("string()"))
