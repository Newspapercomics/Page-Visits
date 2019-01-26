import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

visits_cart = pd.merge(visits, cart, how='left')

denom=(len(visits_cart))

numer=(len(visits_cart[visits_cart.cart_time.isnull()]))

print(float(numer)/denom)

cart_checkout = pd.merge(cart, checkout, how='left')

denom2=(len(cart_checkout))

numer2=(len(cart_checkout[cart_checkout.checkout_time.isnull()]))

print(float(numer2)/denom)

all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')

print(all_data.head())

checkout_purchase = pd.merge(checkout, purchase, how='left')

denom3 =(len(checkout_purchase))

numer3 =(len(checkout_purchase[checkout_purchase.purchase_time.isnull()]))

print(float(numer3)/denom3)

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
print all_data.time_to_purchase
print all_data.time_to_purchase.mean()