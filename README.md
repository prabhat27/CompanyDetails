# CompanyDetails


Python code to get company details from wikipedia page.

To run the code, follow the steps given:-

STEP 1: Download wiki sample dump.
         URL: https://dumps.wikimedia.org/other/static_html_dumps/November_2006/en/wikipedia-en-html-1.7z

STEP 2: Unzip the downloaded file.

STEP 3: Install following python libraries.
        a) bs4 (sudo apt-get install python-bs4 (Ubuntu))
        b) pymongo (sudo apt-get install python-pymongo (Ubuntu))

STEP 4: Run file extract_cmpny_info.py using command
        python extract_cmpny_info.py {Wiki file path unzipped in step 2} 
        Example:- python extract_cmpny_info.py /home/prabhat/Downloads/en

STEP 5: Result will be stored in Mongodb database with following details.
        Host: localhost
        DB: test
        Collection: company_details 

