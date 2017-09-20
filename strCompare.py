######################################################################################
#    Seth challange 9/19                                                             #
# Compare two strings, treat numberics within the string as numbers.                 #
# Return -1 , 0 , +1 if first greater, equal, second greater.                        #
# Numbers before letters                                                             #  
######################################################################################

# add a main
def getLeadNum(myStr):
    for i in range(len(myStr)):
        if not myStr[i].isnumeric:
            return i-1
    
def compare(str1, str2):
    if str1 == str2:
        return 0
    
    #take leading char:
    s1 = str1[0]
    s2 = str2[0]

    #if str1 starts with a number, grab as big of a number as possible.
    if s1.isnumeric():        
        s1Num = str1[:getLeadNum(str1)]

        if s2.isnumeric():
            s2Num = str2[:getLeadNum(str2)]

            if s1Num > s2Num:
                return -1
            elif s1Num < s2Num:
                return +1
            else:
                a =  ( str1[len(str(s1Num))-1:])
                b =  ( str2[len(str(s2Num))-1:])
        
                return compare(a,b)
        else:
           return -1
       
    #if str1 is not numeric:
    else:        
        if s2.isnumeric():
            return +1
        else:
            if s1>s2:
                return -1
            elif s1<s2:
                return +1
            else:
                return compare(str1[1:],str2[1:])

print(compare('a2b','a10b'))

