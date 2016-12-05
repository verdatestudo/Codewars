
'''
Codewars - ATM Money Counter

Last Updated: 2016-Dec-05
First Created: 2016-Dec-05
Python 3.5
Chris

https://www.codewars.com/kata/atm-money-counter/

Description:
Imagine we have ATM with many currencies. User can get money of any currency ATM has.
Our function must analyze currency and value of what users wants and give money to user starting from bigger values to lesser.
This KATA has preloaded dictionary of possible bank note values for different currencies.
VALUES = {'EUR': [5, 10, 20, 50, 100, 200, 500], '...':'...'}
Function must return string containing how many bank notes of each value ATM will give out like this:
8 * 100 USD, 2 * 20 USD, 1 * 2 USD
If it can't do that because it has no notes for this value, it returns See tests.
"Can't do *value* *currency*. Value must be divisible by *something*!"
If it hasn't requested currency at all, it returns
"Sorry, have no *currency*."
See testcases for user input samples. Note that 'EUR 1000' and '1000eur' are the same. Tested on Python 3.5. PS: Sorry for bad English.
'''

import re
def atm(user_value):
    '''
    ATM Money Counter function.
    Takes a user_value containing currency (string) and money value (int) and returns
    quantity and value of notes. (See above description for more details).

    VALUES is a dict provided by problem in the form (Currency : [Values]).

    Returns a string result in the form Quantity * Value, Quantity2 * Value2 etc.
    '''
    VALUES = {'EUR': [5, 10, 20, 50, 100, 200, 500], 'USD':[10, 100]} # very basic testing dict.

    currency = re.search('([a-zA-Z]+)', user_value).group(0).upper()
    money_value = int(re.search('(\d+)', user_value).group(0))

    if currency not in VALUES:
        return 'Sorry, have no %s.' %(currency)

    if money_value % VALUES[currency][0] != 0:
        return 'Can\'t do %d %s. Value must be divisible by %d!' %(money_value, currency, VALUES[currency][0])

    endstuff = []
    while money_value != 0:
        for current_denom in VALUES[currency][-1::-1]:
            quote, mod = divmod(money_value, current_denom)
            if quote != 0:
                endstuff.append('%d * %d %s' %(quote, current_denom, currency))
            money_value = mod

    return ', '.join(endstuff)

def testing():
    '''
    Tests.
    '''
    print(atm('XSF 1000'))
    print(atm('rub 12341'))
    print(atm('10202UAH'))
    print(atm('842 usd'))
    print(atm('euR1000'))
    print(atm('sos100'))

testing()

# Test.assert_equals(atm('XSF 1000'), 'Sorry, have no XSF.')
# Test.assert_equals(atm('rub 12341'), 'Can\'t do 12341 RUB. Value must be divisible by 10!')
# Test.assert_equals(atm('10202UAH'), '20 * 500 UAH, 2 * 100 UAH, 1 * 2 UAH')
# Test.assert_equals(atm('842 usd'), '8 * 100 USD, 2 * 20 USD, 1 * 2 USD')
# Test.assert_equals(atm('euR1000'), '2 * 500 EUR')
# Test.assert_equals(atm('sos100'), 'Can\'t do 100 SOS. Value must be divisible by 1000!')
