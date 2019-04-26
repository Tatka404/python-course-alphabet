from typing import List


def task_1_add_new_record_to_db(con) -> None:


    #with con.cursor() as cur:
    #    cur.execute ("""INSERT INTO customers
    #    (customername, contactname, address, city, postalcode, country)
    #    VALUES ('Thomas', 'David', 'Some Address', 'London', '774','Singapore');""")

    with con.cursor() as cur:

        customername = "Thomas"
        contactname = "David"
        address = "Some Address"
        city = "London"
        postalcode = "774"
        country = "Singapore"

        cur.execute(f"INSERT INTO customers (customername, contactname, address, city, postalcode, country)"
                    f" VALUES ('{customername}', '{contactname}', '{address}', '{city}', {postalcode}, '{country}')")


def task_2_list_all_customers(cur) -> list:

    cur.execute("""select * from Customers;""")
    return cur.fetchall()


def task_3_list_customers_in_germany(cur) -> list:

    cur.execute(""" select * from customers
                    where country = 'Germany';""")
    return cur.fetchall()


def task_4_update_customer(con):

    with con.cursor() as cur:
        cur.execute ("""update customers
                        set customername = 'Johnny Depp'
                        where customerid = 1 ;""")


def task_5_delete_the_last_customer(con) -> None:

    with con.cursor() as cur:
        cur.execute ("""delete from customers
                        where customerid in (select max(customerid) 
                                             from customers);""")


def task_6_list_all_supplier_countries(cur) -> list:

    cur.execute("""select country from suppliers;""")
    return cur.fetchall()


def task_7_list_supplier_countries_in_desc_order(cur) -> list:

    cur.execute("""select country from suppliers
                   order by country desc;""")
    return cur.fetchall()


def task_8_count_customers_by_city(cur):

    cur.execute("""select COUNT (city), city 
                   from customers
                   group by city 
                   order by count(city) desc;""")
    return cur.fetchall()


def task_9_count_customers_by_country_with_than_10_customers(cur):

    cur.execute("""select country, count(country)
                   from Customers
                   group by country
                   having count(country) >= 10;""")
    return cur.fetchall()


def task_10_list_first_10_customers(cur):

    cur.execute("""select * from Customers limit 10;""")
    return cur.fetchall()


def task_11_list_customers_starting_from_11th(cur):

    cur.execute("""select * from Customers offset 11;""")
    return cur.fetchall()


def task_12_list_suppliers_from_specified_countries(cur):

    cur.execute("""select supplierid, suppliername, contactname, city, country 
                   from suppliers
                   where country in ('USA', 'UK', 'Japan');""")
    return cur.fetchall()


def task_13_list_products_from_sweden_suppliers(cur):

    cur.execute("""select p.productname  from products p
                   inner join suppliers s
                   on s.supplierid = p.supplierid
                   and s.country = 'Sweden';""")
    return cur.fetchall()


def task_14_list_products_with_supplier_information(cur):

    cur.execute("""select productid, productname, unit, price, country, city, suppliername 
                   from products left join suppliers on
                   suppliers.supplierid = products.supplierid;""")
    return cur.fetchall()


def task_15_list_customers_with_any_order_or_not(cur):

    cur.execute("""select c.customername, c.contactname, c.country, o.orderid
                   from Customers c
                   left join Orders o
                   on o.customerid = c.customerid;""")
    return cur.fetchall()


def task_16_match_all_customers_and_suppliers_by_country(cur):

    cur.execute("""select c.customername as customername , c.address as address, c.country as customercountry,
                   s.country as suppliercountry, s.suppliername as suppliername 
                   from Customers c
                   full outer join suppliers s
                    on c.country = s.country
                    order by c.country, s.country;""")
    return cur.fetchall()
