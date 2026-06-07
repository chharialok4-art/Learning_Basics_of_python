def bi_dict(elements, get_element):
    for kys, vals in elements.items():
        if vals == get_element:
            print(kys)
            return
    print("Not Found")

if __name__ == "__main__":
    elements = {"O":"oxygen", "H":"Hydrogen", "C":"Carbon", "He":"Helium", "P":"Potassium", "Br":"Boron"}
    get_input_element = input("Enter the element Name:-")
    bi_dict(elements, get_input_element)
