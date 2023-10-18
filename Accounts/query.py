# (1): Return customers from customer table
customer = Customer.objects.all()

# (2): Return first customers in table
firstCustomer = Customer.objects.first()

# (3): Return last customers in table
lastCustomer = Customer.objects.last()

# (4): Return single customers by name
customer = Customer.objects.get(name='sreytouch Thor')

# (5): Return single customers by ID
customer = Customer.objects.get(id=1)

# (6): Return all order related to customer
order = customer.order_set.all()

# (7): Return order customer name (query pearent model value)
order = Order.objects.first()
pearentName = order.Customer.name

# (8): Return Product from products table with value or "In door" in categary
products = Product.objects.filter(category='In door')

# (9):  Order/Sort objects by id
leastToGreatest = Product.objects.all().order_by('id')
GreatestToleast = Product.objects.all().order_by('-id')

# (10): Return all products with tag of "Sports": "Query Many to Many field"
productFiltered = Product.objects.filter(tags__name='Gym')


# Related set example
class ParentModel(models.Model):
    name = models.CharField(max_length=200, null= True)

    
class ChildModel(models.Model):
    parent = models.ForeignKey(Customer)
    name = models.CharField(max_length=200, null= True)

parent = ParentModel.objects.first()
# Return all child models related to parent
parent.childmodel_set.all()


