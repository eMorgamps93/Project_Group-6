from flask import Flask, render_template
import sqlite3
import pandas as pd
import os


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, '..', "Finance_Companies.db")

def get_data_sample():
    """Fetch a sample of data from the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    query = "SELECT * FROM Company_Details;"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
 
def generate_navbar():
    """Generate a consistent navigation bar for all pages with styling."""
    navbar = (
        "<style>"
        "body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #02968A; color: #E6F0DC; }"
        "nav { background-color: #023D54; padding: 20px; text-align: center; }"
        "nav a { margin: 0 15px; text-decoration: none; color: white; font-weight: bold; }"
        "nav a:hover { color: #FFD700; }"
        "hr { border: 0; height: 1px; background: #ccc; margin: 20px 0; }"
        "h1, h2 { color: #fff; text-align:center;}"
        "p{text-align:center;}"
        "ul { padding-left: 20px; list-style-type: none; padding-left: 30rem}"
        "ul li { margin-bottom: 10px;  }"
        "table { border-collapse: collapse; width: 100%; padding: 0 30px, margin: 20px 0; }"
        "table th, table td { border: 1px solid #ccc; padding: 10px; text-align: left; }"
        "table th { background-color: #007BFF; color: white; }"
        "table tr:nth-child(even) { background-color: #02968A; }"
        "footer { background-color: #333; color: white; text-align: center; padding: 10px 0; position: fixed; width: 100%; bottom: 0; }"
        "</style>"
        "<nav>"
        "<a href='/'>Home</a>"
        "<a href='/about'>About</a>"
        "<a href='/data'>Data</a>"
        "</nav><hr>"
    )
    return navbar
 
@app.route('/')
def home():
    navbar = generate_navbar()
    return navbar + (
        "<h1>Welcome to the U.S. Financial Companies Data Hub</h1>"
        "<p>Explore the dataset via the About and Data pages.</p>"
        "<p>Discover insights about Financial Companies and indicators of each company's financial performance over time.</p>"
    )
 
@app.route('/about')
def about():
    navbar = generate_navbar()
    about_text = (
        "<h1>About the Data</h1>"
        "<p>This dataset comprises of financial institutions operating across the United States and determinants of their success/closure. Some column names which define the dataset include: STNAME, NAME, NETINC, ASSET, and EQ.</p>"
        "<h2>Data Columns:</h2>"
        "<ul>"
        "<li><b>CLCODE</b>: identifies each company as a National Bank,  State Commercial Bank, State Industrial Bank, etc.</li>"
        "<li><b>NAME</b>: legal title or name of Financial Company</li>"
        "<li><b>STNAME</b>: U.S. state in which each company is physically located</li>"
        "<li><b>ACTIVE</b>: indicates the status of each company as either active or inactive</li>"
        "<li><b>ESTMYD</b>: date each company was established</li>"
        "<li><b>NETINC</b>: operating Income of each company</li>"
        "<li><b>ASSET</b>: Resources (Assets) owned by each company</li>"
        "<li><b>EQ</b>: owners' interest or claim to each company's assets</li>"
        "<li><b>REPDTE</b>: the last day of the financial reporting period selected</li>"
        "<li><b>ROA</b>: stands for Return on Assets. A financial measure of how much a company earns for every unit of asset owned.</li>"
        "<li><b>ROE</b>: stands for Return on Equity. A financial measure of how effectively a company uses investors' money to generate net income.</li>"
        "</ul>"
    )
    return navbar + about_text
 
@app.route('/data')
def data():
    navbar = generate_navbar()
    df = get_data_sample()
    return navbar + (
        "<h1>Data</h1>"
        "<p>Here is a view of the dataset and its components:</p>"
        + df.to_html(index=False, border=0, classes='data-table')
    )
 
if __name__ == '__main__':
    app.run(debug=True)

# def get_db():
#     try:
#         connection = sqlite3.connect(DATABASE)
#         connection.row_factory = sqlite3.Row
#         return connection
#     except sqlite3.Error as e:
#         print(f"Error connecting to the database: {e}")
#         return None

# @app.route("/")
# def home():
#     return render_template("home.html") 

# @app.route("/about")
# def about():
#     return render_template("about.html")

# @app.route("/dataset")
# def data():
#     conn = sqlite3.connect(my_path)
#     cursor = conn.cursor()
#     All_Firms = cursor.execute("SELECT * FROM Company_Details").fetchall()
#     conn.close()

#     return render_template("data_table.html", All_Firms=All_Firms)

# if __name__=="__main__":
#     app.run(debug=True)