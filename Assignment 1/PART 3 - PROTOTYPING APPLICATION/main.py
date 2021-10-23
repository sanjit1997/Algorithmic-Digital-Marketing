#!/usr/bin/env python
import snowflake.connector
import pandas as pd
# Gets the version
ctx = snowflake.connector.connect(
    user='sanjit97',
    password='Sas@977164',
    account='aaa01287.us-east-1'
    )
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
    sql = "use database project_database"
    cs.execute(sql)
    sql="use schema project_schema"
    cs.execute(sql)
    sql="create table customer(ID integer,Year_Birth integer,Education varchar(20),Marital_Status varchar(20),Income123 varchar(20),Kidhome integer,Teenhome integer,Dt_Customer varchar(20),Recency integer,MntWines integer,MntFruits integer,MntMeatProducts integer,MntFishProducts integer,MntSweetProducts integer,MntGoldProds integer,NumDealsPurchases integer,NumWebPurchases integer,NumCatalogPurchases integer,NumStorePurchases integer,NumWebVisitsMonth integer,AcceptedCmp3 integer,AcceptedCmp4 integer,AcceptedCmp5 integer,AcceptedCmp1 integer,AcceptedCmp2 integer,Response integer,Complain integer,Country varchar(20))"
    cs.execute(sql)
    df = pd.read_csv(r'C:\Users\raksh\Downloads\new.csv')
    print(df)
    for index, row in df.iterrows():
        cs.execute("INSERT INTO project_schema.customer values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}','{21}','{22}','{23}','{24}','{25}','{26}','{27}')".format(row.ID,row.Year_Birth,row.Education,row.Marital_Status,row.Income,row.Kidhome,row.Teenhome,row.Dt_Customer,row.Recency,row.MntWines,row.MntFruits,row.MntMeatProducts,row.MntFishProducts,row.MntSweetProducts,row.MntGoldProds,row.NumDealsPurchases,row.NumWebPurchases,row.NumCatalogPurchases ,row.NumStorePurchases,row.NumWebVisitsMonth ,row.AcceptedCmp3,row.AcceptedCmp4,row.AcceptedCmp5,row.AcceptedCmp1,row.AcceptedCmp2,row.Response,row.Complain ,row.Country))


finally:
    cs.close()
ctx.close()