import sqlite3
conn = sqlite3.connect('fountain9.db')
c = conn.cursor()
# c.execute("""CREATE TABLE supplier(
#     supplier_id INTEGER PRIMARY KEY,
#     supplier_name TEXT)
# """)
# c.execute("""CREATE TABLE PRODUCTMASTER(
#     product_id INTEGER PRIMARY KEY,
#     product_name TEXT,
#     category TEXT)
# """)
# c.execute("""CREATE TABLE BRANCHMASTER(
#     branch_id INTEGER PRIMARY KEY,
#     branch_name TEXT,
#     branch_city TEXT)
# """)
# c.execute("""CREATE TABLE Sales (
#     sales_id  INTEGER PRIMARY KEY,
#     date      DATE,
#     product_id INTEGER REFERENCES PRODUCTMASTER (product_id),
#     branch_id  INTEGER REFERENCES BRANCHMASTER (branch_id),
#     price     INTEGER,
#     quantity  INTEGER
# );

# """)
c.execute("""CREATE TABLE PurchaseOrders (
    PurchaseOrderId  INTEGER PRIMARY KEY
                             NOT NULL,
    date             DATE,
    product_id       INTEGER REFERENCES PRODUCTMASTER (product_id),
    branch_id        INTEGER REFERENCES BRANCHMASTER (branch_id),
    supplier_id      INTEGER REFERENCES supplier (supplier_id),
    OrderedQuantity  INTEGER,
    ReceivedQuantity INTEGER,
    OrderedDate      DATE,
    ReceivedDate     DATE
);
    
""")
