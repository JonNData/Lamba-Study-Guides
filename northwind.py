# PART 2

import sqlite3
# Make a function to query
def make_query(lite3_query, db='northwind_small.sqlite3'):
    """
    Connect to a DB, make a query, and return results
    """
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    results = curs.execute(lite3_query).fetchall()
    conn.commit()
    return print(results)




# What are the ten most expensive items (per unit price) in the database?
top_price = """
    SELECT UnitPrice, ProductName
    FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10
"""
print('top_price')
make_query(top_price)
# Côte de Blaye
# Thüringer Rostbratwurst
# Mishi Kobe Niku
# "Sir Rodney's Marmalade"
# Carnarvon Tigers
# Raclette Courdavault
# Manjimup Dried Apples
# Tarte au sucre
# Ipoh Coffee
# Rössle Sauerkraut

# What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)
average_age_at_hire ="""
    SELECT Round(AVG(HireDate-BirthDate),1) as AVGAgeAtHire
    FROM Employee
"""
print('average_age_at_hire')
make_query(average_age_at_hire)
# 37.2 yrs old

# (Stretch) How does the average age of employee at hire vary by city?
Age_by_city= """
SELECT Round(AVG(HireDate-BirthDate),1) as AVGAgeAtHire, City
FROM Employee
GROUP BY City
"""
print('Age_by_city')
make_query(Age_by_city)
# Mean:	39.5
# Median:	40
# Mode:	40


# PART 3

# What are the ten most expensive items (per unit price) in the database and their suppliers?
pricey_supplier = """
    SELECT UnitPrice, SupplierId, ProductName, Supplier.CompanyName
    FROM Product
    JOIN Supplier ON SupplierId = Supplier.Id
    GROUP BY ProductName
    ORDER BY UnitPrice DESC
    LIMIT 10
"""
print('pricey_supplier')
make_query(pricey_supplier)
# Well now it's getting wordy

# What is the largest category (by number of unique products in it)?
largest_category= """
    SELECT CategoryId, Count(ProductName), Category.Id, Category.CategoryName
    FROM Product
    JOIN Category ON CategoryId = Category.Id
    Group BY CategoryId
    Order by Count(ProductName) DESC
    Limit 1
"""
print('largest_category')
make_query(largest_category)
# Confections

# (Stretch) Who’s the employee with the most territories? Use TerritoryId (not name, region, or other fields) as the unique identifier for territories.
most_territory = """
    SELECT EmployeeId, Count(TerritoryId), EE.FirstName, EE.LastName
    FROM EmployeeTerritory as ET
    JOIN Employee as EE ON EE.Id = ET.EmployeeId
    Group BY FirstName
    Order BY Count(TerritoryId) DESC
    LIMIT 1
"""
print('most_territory')
make_query(most_territory)
# Robert King, that greedy son of a gun

# Part 4 - Questions (and your Answers)
# Answer the following questions, baseline ~3-5 sentences each, as if they were interview screening questions (a form you fill when applying for a job):

# In the Northwind database, what is the type of relationship between the Employee and Territory tables?
#     Employees have a 'One to many' relationship with Territories. One employee may be in charge of many territories. Each territory is only occupied by one Employee.

# What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?
#     A NoSQL document store is appropriate when dealing with big data that is impractical to deal with otherwise. This can be determined by long query and loading times.
#      It's also appropriate when a database is newly developing and the relations between the objects in it are in flux and yet to be defined. 
#      Mongo would not be appropriate for a relational database where the desired outcome is easily updated tables depending on other tables

# What is "NewSQL", and what is it trying to achieve?
#     NewSQL is yet another flavor of the SQL family. One goal of NewSQL is to approach the scalability of NoSQL while maintaining the ACID attributes of SQL. 
#     NewSQL can utilize independent nodes and optimized datastores to restore functionality to querying big data.