from bs4 import BeautifulSoup as Soup
import os, sys
import re
import db_handler
import traceback

class WikiExtract:
    def __init__(self, path = '/home/prabhat/Downloads/en', db_host = 'localhost', db_collection = 'company_details'):
        self.PATH = path
        self.HOST = db_host
        self.COLLECTION = db_collection
        self.DB = db_handler.DB()

    def get_files(self):
        """
        Returns path of all wiki files
        """
        file_list = []
        for root, directories, filenames in os.walk(self.PATH):
            for filename in filenames:
                file_list.append(os.path.join(root,filename))
        return file_list
    
    def is_valid(self, string):
        return "Website" in string

    def parse_div(self, string):
        nstr = ''
        for i in string:
            try:
                if ord(i)<128:
                    nstr = nstr + i
                else:
                    nstr = nstr + ' '
            except:
                nstr = nstr + ' '

        string = re.sub('[ ]{2,}',' ', nstr)
        lst = re.split('[/\n]{2,}', string)[:-1]

        lst.remove('')
        data = {}
        for (i, each) in enumerate(lst):
            try:
                nlst = each.split('\n')
                if(i == 0):
                    data['name'] = nlst[0].lower()
                else:
                    key = nlst[0].lower()
                    values = nlst[1:]
                    if(len(values) > 1):
                        data[key] = [ value.lower() for value in values]
                    else:
                        data[key] = values[0].lower()
            except:
                pass
        if(' ' in data.get('website', ' ')):  # Invalid url
            return None

        return data

    def parse_page(self):
        """
        Extract relevant information from each file and insert in the database.
        """
        print "Please wait, reading files ....."
        file_list = self.get_files()
        print "Total file count is: " + str(len(file_list))

        for file_path in file_list:
            try:
                print "Processing file " + file_path 
                fp = open(file_path, "r")
                source = fp.read()
                soup = Soup(source,"html.parser")
                div = soup.find("table", attrs = {"class":"infobox"})
                div_text = div.text.encode('utf-8')
                if(self.is_valid(div_text)):
                    data = self.parse_div(div_text)
                    if(data):
                        data['file_path'] = file_path
                        self.DB.insert_details(data)
            except:
                pass


if __name__ == '__main__':

    PATH = '/home/prabhat/Downloads/een' # File path 
    PATH = list(sys.argv)[1]
    # print PATH
    wiki = WikiExtract(PATH)
    wiki.parse_page()
    

