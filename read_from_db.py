import pandas as pd
from db_connection import engine

# Reading the SQL into pandas
# df = pd.read_sql("Select * from orders", con=engine)
# print(df.head())

# query = """
#     select Category, round(Sum(Net_Amount),2) AS Total_Revenue
#     from orders
#     group by Category
#     order by Total_Revenue desc
# """

# Parameter Passing 
# query = """
#   select Category, round(Sum(Net_Amount), 2) as Total_Revenue
#   from orders
#   where Category = %(Category)s
#   group by Category;
# """
# category = "Electronics"

# params = {
#     "Category": "Accessories"
# }

# Parameterized Revenue Query
# category = "Accessories"
# query = """
# select Category, round(sum(Net_Amount), 2) as Total_Revenue
# from orders
# where Category = %(Category)s
# group by Category
# """
# params  = {"Category":category}

# df = pd.read_sql(query, con=engine, params=params)
# print(df)


# Create a dataframe into the table 
# te
# st_data = pd.DataFrame({
#     "Product":["Test-Laptop", "Test-Mouse", "Test-Keyboard"],
#     "Quantity":[2,5,3],
#     "Price":[50000, 1000, 2500]
# })

# test_data.to_sql(
#     "Test_orders", 
#     con=engine,
#     if_exists="replace",
#     index = False
# )

# print("Data Loaded brother")


# Read the new db table back into python
# df = pd.read_sql(
#     "select * from test_orders", con=engine
# )
# print(df)

# df = pd.read_sql("Select * from orders", con=engine)
# print(df.head())
# print(df.shape)

# Read data from MySQL
def read_data(query, params = None):
    df = pd.read_sql(
        query,
        con=engine,
        params=params
    )

    return df


# Get revenue by category
def get_category_revenue(category):

    query = """
    SELECT
        Category,
        ROUND(SUM(Net_Amount), 2) AS Total_Revenue
    FROM orders
    WHERE Category = %(category)s
    GROUP BY Category
    """
    params = {"category": category}

    return read_data(query, params)

if __name__ == "__main__":

    df = get_category_revenue("Electronics")

    print(df)