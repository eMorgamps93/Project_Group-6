***Financial Institutions: A sneak-peak into companies in the Financial Sector operating across the United States***

***Completed By:***  

- Papa Kofi Arhin (W0865495)
- Timothy Amissah (W0876702)
- Eddie Morgan (W0876534)
- Joshua Kwaku Lary (W0866735)
  
***About***  

Our website was created using Flask to display data about companies in the Financial Sector across the U.S.A. The data is stored in an SQLite database under the table name "Company_Details" in the database "Financial_Companies".  

The dataset is defined by the variables below:  
- <u>CLCODE</u>: identifies each company as a "National Bank",  "State Commercial Bank", "State Industrial Bank", etc. 
- <u>NAME</u>: legal title or name of Financial Company.
- <u>STNAME</u>: U.S. state in which each company is physically located.  
- <u>ACTIVE</u>:  indicates the status of each company as either "active" or "inactive".
- <u>ESTMYD</u>: date each company was established.  
- <u>NETINC</u>: operating Income of each company.
- <u>ASSET</u>: Resources (Assets) owned by each company.
- <u>EQ</u>: owners' interest or claim to each company's assets.
- <u>REPDTE</u>: the last day of the financial reporting period selected.  
- <u>ROA</u>: stands for "Return on Assets". A financial measure of how much a company earns for every unit of asset owned.   
- <u>ROE</u>: stands for "Return on Equity". A financial measure of how effectively a company uses investors' money to generate net income.

***Webpages***  

- <u>Home:</u> an overview of the dataset and its usage. Also has navigation links to the <u>About</u> and <u>Data</u> page.  
- <u>About:</u> displays information about the <u>variables</u> in the dataset.  
- <u>Data:</u> tabulates the dataset by their variable names.
  
***Libraries Used***  

- <u>SQLite</u>: To create database.  
- <u>Flask</u>: To create web appplication.  
- <u>os</u>: for file and directory management, and setting user privileges ("permissions").  
- <u>Pands</u>: used to "tabulate" data (represent observations in "rows" and "columns").  
- <u>csv</u>: to read the data in csv format and iterate over each row to return the observations in a table.
  
***Components of the Project***

- <u>Database_&_Table_SQL.ipynb:</u> a Jupyter notebook containg code to create the database 'Finance_Companies.db', the table 'Company_Details' and insert data from a csv file to the table.  
- <u>Finance_Companies.db:</u> SQLite database where details about financial institutions are stored.  
- <u>Financial_Institutions.csv:</u> csv file containing data about financial institutions to import into SQLite.  
- <u>app_template.py:</u> Flask application containing the route functions for Home, About and Data webpages.  
- <u>requirements.txt:</u>: text file containing a list of libraries used in creating the database, table, and website.
  
***Working***  

- A database called 'Finance_Companies.db' and a table 'Company_Details' is created in SQLite using Database_&_Table_SQL.pynb script.  
- The data from csv file Financial_Institutions.csv is uploaded to the table 'Company_Details', using the same script.  
- app_template.py is the flask application that imports the libraries SQLite, Flask, Pathlib, and os, to design the webpage and make it visible to users who want to interact with it.  

  Three routes are created in app_template.py:  
   - The root route ("/") generates the home.html template.  
   - The /about route renders the about.html template.  
   - The /data route connects to the SQLite database, retrieves data from 'Company_Details', and renders the data_table.html template with the fetched data.
