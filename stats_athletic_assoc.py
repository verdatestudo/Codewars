'''
Codewars - Increasing Numbers

Last Updated: 2016-Dec-08
First Created: 2016-Dec-08
Python 3.5
Chris

https://www.codewars.com/kata/statistics-for-an-athletic-association

'''

def stat(strg):
    '''
    Each time you get a string of all race results of every team who has run. For example here is a string showing the individual results of a team of 5:
    "01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"
    Each part of the string is of the form: h|m|s where h, m, s are positive or null integer (represented as strings) with one or two digits. There are no traps in this format.

    To compare the results of the teams you are asked for giving three statistics; range, average and median.
    Range : difference between the lowest and highest values. In {4, 6, 9, 3, 7} the lowest value is 3, and the highest is 9, so the range is 9 − 3 = 6.
    Mean or Average : To calculate mean, add together all of the numbers in a set and then divide the sum by the total count of numbers.
    Median : In statistics, the median is the number separating the higher half of a data sample from the lower half.
    The median of a finite list of numbers can be found by arranging all the observations from lowest value to highest value and picking the middle one
    (e.g., the median of {3, 3, 5, 9, 11} is 5) when there is an odd number of observations. If there is an even number of observations,
    then there is no single middle value; the median is then defined to be the mean of the two middle values (the median of {3, 5, 6, 9} is (5 + 6) / 2 = 5.5).

    Your task is to return a string giving these 3 values. For the example given above, the string result will be

    "Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"

    of the form:

    "Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"

    where hh, mm, ss are integers (represented by strings) with each 2 digits.

    Remarks:

        if a result in seconds is ab.xy... it will be given truncated as ab.

        if the given string is "" you will return ""

    # split into a list
    # convert all to seconds
    # calc range mean median
    # convert to hh mm ss and secds
    '''
    if strg == '':
        return strg

    times = [item.split('|') for item in strg.split(', ')]
    times = [int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2]) for time in times]
    times_range = max(times) - min(times)
    times_mean = int(sum(times) / len(times))
    times_median = median(times)

    return "Range: %s Average: %s Median: %s" %(convert_secs_to_hms(times_range), convert_secs_to_hms(times_mean), convert_secs_to_hms(times_median))

def median(lst):
    '''
    Median
    '''
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0

def convert_secs_to_hms(seconds):
    '''
    Convert
    '''
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%02d|%02d|%02d" % (h, m, s)


def testing():
    print('Testing ...')
    print(stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17") == \
    "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34")
    print(stat("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41") == \
    "Range: 00|31|17 Average: 02|26|18 Median: 02|22|00")

testing()
