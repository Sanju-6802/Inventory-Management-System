#!/usr/bin/env python
# coding: utf-8

# # INVENTORY MANAGEMENT SYSTEM

# In[48]:


#Product id,Product name,Supplier,Inventory Value,Quantity on hand,Customer order,Quantity Available
dct={1234:{'Product name':'Tyres','Supplier':'Michelin','Inventory Value':'Rs.5000','Quantity on hand':'100','Customer orders':'75','Quantity Available':'25'},
    1324:{'Product name':'Tyres','Supplier':'Bridgestone','Inventory Value':'Rs.1000','Quantity on hand':'150','Customer orders':'90','Quantity Available':'60'},
    1423:{'Product name':'Tyres','Supplier':'Goodyear','Inventory Value':'Rs.4500','Quantity on hand':'180','Customer orders':'90','Quantity Available':'90'},
    1432:{'Product name':'Tyres','Supplier':'Pirelli','Inventory Value':'Rs.3000','Quantity on hand':'150','Customer orders':'80','Quantity Available':'70'},
    1243:{'Product name':'Tyres','Supplier':'Continental AG','Inventory Value':'Rs.6000','Quantity on hand':'165','Customer orders':'75','Quantity Available':'90'},
    2134:{'Product name':'Tyres','Supplier':'Dunlop','Inventory Value':'Rs.7000','Quantity on hand':'170','Customer orders':'100','Quantity Available':'70'},
    2341:{'Product name':'Tyres','Supplier':'Apollo','Inventory Value':'Rs.3500','Quantity on hand':'160','Customer orders':'75','Quantity Available':'85'},
    3421:{'Product name':'Tyres','Supplier':'CEAT','Inventory Value':'Rs.8000','Quantity on hand':'185','Customer orders':'75','Quantity Available':'110'},
    4321:{'Product name':'Tyres','Supplier':'MRF','Inventory Value':'Rs.7000','Quantity on hand':'200','Customer orders':'175','Quantity Available':'25'},
    4213:{'Product name':'Tyres','Supplier':'JK','Inventory Value':'Rs.4000','Quantity on hand':'210','Customer orders':'190','Quantity Available':'20'}}


# In[49]:


dct[1432]


# ## Product Details based on their Product id

# In[51]:


product_id=int(input("Enter the product id:"))
print('-'*25)
print('Product name:',dct[product_id]['Product name'])
print('Supplier:',dct[product_id]['Supplier'])
print('Inventory Value:',dct[product_id]['Inventory Value'])
print('Quantity on hand:',dct[product_id]['Quantity on hand'])
print('Customer orders:',dct[product_id]['Customer orders'])
print('Quantity Available:',dct[product_id]['Quantity Available'])
print('-'*25)



# ## Product Details based on their name

# In[53]:


name=input("Enter the name:")
for key in dct.keys():
    if(dct[key]['Supplier'].lower()== name.lower()):   
       print('-'*25)
       print('Product name:',dct[key]['Product name'])
       print('Inventory Value:',dct[key]['Inventory Value'])
       print('Quantity on hand:',dct[key]['Quantity on hand'])
       print('Customer orders:',dct[key]['Customer orders'])
       print('Quantity Available:',dct[key]['Quantity Available'])
       print('-'*25)
       
     


# ## Finding Costliest Product

# In[40]:


value=[]
for key in dct.keys():
    value.append(dct[key]['Inventory Value'])
price=max(value)
for key in dct.keys():
    if(dct[key]['Inventory Value']==price):
        print(dct[key]['Supplier'])


# ## Finding Cheapest Product

# In[41]:


value=[]
for key in dct.keys():
    value.append(dct[key]['Inventory Value'])
price=min(value)
for key in dct.keys():
    if(dct[key]['Inventory Value']==price):
        print(dct[key]['Supplier'])

