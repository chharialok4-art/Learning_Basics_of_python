li = ["Hello   world", "   Python  is   great  ", "   Extra  spaces    here  "];
get_all = [" ".join(item.split()) for item in li];
print(get_all);