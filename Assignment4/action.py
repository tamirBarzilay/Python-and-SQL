from persistence import *

import sys

def add_activities(splittedline : list[str]):
    repo.activities.insert(Activitie(splittedline[0],splittedline[1],splittedline[2],splittedline[3]))


def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            product_id=splittedline[0]
            units=int(splittedline[1])
            curr_product=repo.products.find(id=product_id)[0]
            if units>0 or (int(curr_product.quantity)>=(units*-1) and units<0):
                add_activities(splittedline[0:])
                id=curr_product.id
                description=curr_product.description
                price=curr_product.price
                quantity = curr_product.quantity + units
                repo.products.delete(id=product_id)
                repo.products.insert(Product(id,description,price,quantity))
                
                
            

if __name__ == '__main__':
    main(sys.argv)