number  = 57;
temp = None;
get_digit =[];
while (number != 0) :
    temp = number % 2;
    get_digit.append(str(temp))
    number = int(number/2);
get_digit.reverse();
print("".join(get_digit));