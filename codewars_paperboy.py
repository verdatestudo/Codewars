'''
Codewars - PaperBoy
http://www.codewars.com/kata/paperboy
2016-Mar-26
Python 2.7
Chris

Description:

You and your best friend Stripes have just landed your first high school jobs!
You'll be delivering newspapers to your neighbourhood on weekends.
For your services you'll be charging a set price depending on the quantity of the newspaper bundles.

The cost of deliveries is:

    $3.85 for 40 newspapers
    $1.93 for 20
    $0.97 for 10
    $0.49 for 5
    $0.10 for 1

Stripes is taking care of the footwork doing door-to-door drops and your job is to take care of the finances. What you'll be doing is providing the cheapest possible quotes for your services.
Write a function that's passed an integer representing the amount of newspapers and returns the cheapest price. The returned number must be rounded to two decimal places.
'''

def cheapest_quote(num_newspapers):
    count = -1
    for item in delivery_cost:
        # divmod returns (division, modulo)
        if divmod(num_newspapers, item[0])[0] != 0:
            count += 1

    if num_newspapers == 0 or count == 0:
        return round(num_newspapers * delivery_cost[0][1], 2)

    div, mod = divmod(num_newspapers, delivery_cost[count][0])
    return round((div * delivery_cost[count][1]) + cheapest_quote(mod), 2)

delivery_cost = [[1, 0.1], [5, 0.49], [10, 0.97], [20, 1.93], [40, 3.85]]

def test_cases():
    print cheapest_quote(1), 0.10
    print cheapest_quote(5), 0.49
    print cheapest_quote(10), 0.97
    print cheapest_quote(20), 1.93
    print cheapest_quote(40), 3.85
    print cheapest_quote(41), 3.95
    print cheapest_quote(80), 7.70
    print cheapest_quote(26), 2.52
    print cheapest_quote(0), 0.0
    print cheapest_quote(499), 48.06
    print cheapest_quote(52968)

test_cases()
