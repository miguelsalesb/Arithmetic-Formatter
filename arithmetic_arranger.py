import re

def arithmetic_arranger(problems, display=False):

    count_problems = len(problems)

    # check if the list submited has more than 5 problems
    if count_problems > 5:
        return "Error: Too many problems."

    problems_str = " ".join(problems)

    problems_string = problems_str.replace(" ", "")

    # find if the nested lists have the operators "*" or "/"
    if len(re.findall("[*/]+", problems_string)) == 1:
        return "Error: Operator must be '+' or '-'."

        # find if the nested lists only contain digits
    if len(re.findall("[^0-9+-]+", problems_string)) > 0:
        return "Error: Numbers must only contain digits."

    if len(re.findall("[0-9]{5}", problems_str)) > 0:
        return "Error: Numbers cannot be more than four digits."

    li = list()
    
    for v in range(len(problems)):

        l = list()
        # add blanks, paragraphs and nothing accordingly with the display value 
        # and the number of the list values
        val = problems[v].replace(" ", "")
        if display == True:
            if v < (count_problems - 1):
                four_spaces = " " * 4
                four_spaces_dash = " " * 4
                four_spaces_last = " " * 4
            else :
                four_spaces = "\n"
                four_spaces_dash = "\n"
                four_spaces_last = ""
        else:
            if v < (count_problems - 1):
                four_spaces = " " * 4
                four_spaces_dash = " " * 4
                four_spaces_last = ""
            else :
                four_spaces = "\n"
                four_spaces_dash = ""

        if "+" in val:
            # divide the list values
            sum = val.split("+")

            # get the values to find out the operation result
            first_value = int(sum[0])
            second_value = int(sum[1])

            # get the biggest value from the two
            max_value = str(max(first_value, second_value))
            
            # get the sizse of the biggest value
            len_max_value = len(max_value)
            # print(max_value, len_max_value)

            total = str(first_value + second_value)
            len_total = len(str(first_value + second_value))

            if first_value + second_value > 0:
                spaces = 2
            else:
                spaces = 1

            l.append(" " * (len_max_value + 2 - len(sum[0])) + sum[0] + four_spaces)
            l.append("+" + " " * (len_max_value + 1 - len(sum[1])) + sum[1] + four_spaces)
            l.append("-" * (len_max_value + 2) + four_spaces_dash)
            if display == True:
                l.append((" " * (2 + len_max_value - len_total)) + str(total) + four_spaces_last)
            
            li.append(l.copy())

        else:
            min = val.split("-")

            first_value = int(min[0])
            second_value = int(min[1])

            max_value = str(max(first_value, second_value))
            len_max_value = len(max_value)

            total = first_value - second_value
            len_total = len(str(first_value + second_value))
            if total > 0:
                spaces = 2
            else:
                spaces = 1
 
            l.append(" " * (len_max_value + 2 - len(min[0])) + min[0] + four_spaces)
            l.append("-" + " " * (len_max_value + 1 - len(min[1])) + min[1] + four_spaces)
            l.append("-" * (len_max_value + 2) + four_spaces_dash)
            if display == True:
                l.append((" " * (spaces + len_max_value - len_total)) + str(total) + four_spaces_last)
            
            li.append(l.copy())

    ll = list()

    if display == False:
        range1 = len(l)
        range2 = len(li)
    else:
        range1 = len(li)
        range2 = len(l)


    for v in range(range1):
        for val in range(range2):
            ll.append(li[val][v])
      
    arranged_problems = "".join(ll)
    return arranged_problems