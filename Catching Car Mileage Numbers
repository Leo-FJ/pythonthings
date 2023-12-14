#My solution to the problem: Catching Car Mileage Numbers on codewars (4 kyu)
#https://www.codewars.com/kata/52c4dd683bfd3b434c000292/python

def is_interesting(number, awesome_phrases):
    #if less than 100
    if number+2 < 100:
        return 0


    L_numbers = [int(i) for i in str(number)]
    #if number is monotone
    if number > 99:
        if all(i == j for i, j in zip(L_numbers, L_numbers[1:])):
            return 2
    #if number is monotone in next 2
    for n in range(number, number+3):
        L_numbers = [int(i) for i in str(n)]
        if all(i == j for i, j in zip(L_numbers, L_numbers[1:])):
            return 1


    #if trailed by 0
    if len(str(number).rstrip('0')) == len('p'):
        return 2
    #if trailed by 0 in the next 2
    for n in range(number, number+3):
        if len(str(n).rstrip('0')) == len('p'):
            return 1


    #if number is increasing or decreasing
    if str(number) in '1234567890' or str(number) in '9876543210':
        return 2

    for n in range(number, number+3):
        #if increasing in next 2
        if str(n) in '1234567890':
            return 1
        #if decreasing in next 2
        if str(n) in '9876543210':
            return 1


    #if number is pallindrome
    pallindrome_n = str(number)
    for n in range(len(pallindrome_n)):
        if len(pallindrome_n) > 1 and pallindrome_n[0] == pallindrome_n[-1]:
            pallindrome_n = pallindrome_n[1:-1]
        else:
            break
        if len(pallindrome_n) == 1:
            return 2
    #if number is pallindrome in the next 2
    for n in range(number+1, number+3):
        n_pallindrome_n = str(n)
        pallindrome_in_two = True

        for i in range(len(n_pallindrome_n) // 2):
            if n_pallindrome_n[i] != n_pallindrome_n[-i-1]:
                pallindrome_in_two = False
                break
        
        if pallindrome_in_two:
            return 1


    #if number is in awesome_phrases
    for n in awesome_phrases:
        #if awesome_phrases = number
        if number == n:
            return 2
        #if awesome_phrases = number in the next 2
        if n in range(number, number+3):
            return 1

    #if not awesome
    return 0
