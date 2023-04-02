from persistence import *

def main():
    print("Activities")
    for i in repo.activities.find_all() :
        print(i.__str__())
    print("Branches")
    for i in repo.branches.find_all() :
        print(i.__str__())
    print("Employees")
    for i in repo.employees.find_all() :
        print(i.__str__())
    print("Products")
    for i in repo.products.find_all() :
        print(i.__str__())
    print("Suppliers")
    for i in repo.suppliers.find_all() :
        print(i.__str__())
    print("")
    print("Employees report")
    output= """SELECT employees.name,employees.salary,branches.location, SUM(-1*activities.quantity*products.price)
              as income FROM employees LEFT JOIN activities ON employees.id=activities.activator_id LEFT JOIN products
              ON products.id=activities.product_id LEFT JOIN branches ON employees.branche=branches.id GROUP BY employees.id
              ORDER BY employees.name ASC"""

    for i in repo.execute_command(output) :
        x=i[3]
        if i[3]==None:
            x=0
        print(i[0].decode()+" "+str(i[1])+" "+ str(i[2].decode())+" "+str(x))
    
    print("")
    print("Activities report")
    output= """SELECT activities.date,products.description,activities.quantity,employees.name,suppliers.name FROM activities
               JOIN products ON activities.product_id=products.id LEFT JOIN suppliers ON suppliers.id =activities.activator_id LEFT JOIN 
               employees ON employees.id =activities.activator_id ORDER BY activities.date"""
    for i in repo.execute_command(output) :
        x=i[3]
        y=i[4]
        if i[3]!=None:
            x="'"+str(x.decode())+"'"
        if i[4]!=None:
           y="'"+y.decode()+"'"

        print("('"+str(i[0].decode())+"', '"+str(i[1].decode())+"', "+ str(i[2])+", "+str(x)+", "+str(y)+")")

if __name__ == '__main__':
    main()