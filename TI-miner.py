import PyPDF2
import csv

def main():
	# Read one PDF file
	pdfFileObj = open("/home/pawned/Desktop/tags/Lazarus_Under_The_Hood_PDF_final.pdf", "rb")
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	# Read the keyword file
	keywordsObj = open("/home/pawned/Desktop/tags/keywords", "rb")
	keywords = keywordsObj.read().split(",")
	# Goes through all the pages and calls the search function
	i = 0
	while i < pdfReader.numPages:
		pageObj = pdfReader.getPage(i)
		page = pageObj.extractText()
		# The search function is called
		search(page, keywords)
		print("Round: ", i)
		i += 1

def search(page, keywords):	
#	print("subfunc called")
	for word in keywords:
#		print("Word: ", word)
#		print("Word founded: ", page.find(word.strip())
		if page.find(word.strip()) > -1:
			print("FOUNDED: ", word.strip())
			#TODO: create a table with keywords where is a client and related documents


main()


def asd():
  #Print the number of pages
  #print(pdfReader.numPages)
  #print pdfReader.getPage(1)

  

  page = pageObj.extractText()
  for keyword in keywordsFile:
    print("Keyword: ", keyword)
    print page.find(keyword)
#    print(keyword)
#  print(line)

#if "activity" in page.extractText():
#  print("BINGO")
#print page.extractText()
#  if any(word in line for word in keywordsFile):
#    print(line)

# Go through the pages one by one


#i = 0
#while i < 10:  #pdfReader.numPages:
#  page = pdfReader.getPage(i)
  # Go through the page word by word
#  print page.extractText()
#  for line in page.extractText():
#    print(line)
#    for word in line.split():
#      print(word)
#  i =+ 1



# Go through the keywords file
#for line in keywordsFile:
#	print line



# Match keywords to the page

#print(pageObj.extractText())

 
