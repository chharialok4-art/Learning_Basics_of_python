str001 = "Alokchhari";
for_alpha = None;
for_digit = None;
for item in str001:
    if item.isalpha():
        for_alpha = True;
    elif item.isdigit():
        for_digit = True;
print("AlphaBate:",for_alpha);
print("Digit:",for_digit);