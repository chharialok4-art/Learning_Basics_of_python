str001 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since 1966, when designers at Letraset and James Mosley, the librarian at St Bride Printing Library, took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets. It has survived not only many decades, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised thanks to these sheets and more recently with desktop publishing software including versions of Lorem Ipsum.";
get_splited_word_by_word = str001.split(" ");
get_len = int(input("enter the length:"));
get_collected = [];
for item in get_splited_word_by_word:
    if len(item) == get_len:
        get_collected.append(item+",");
join_all = "".join(get_collected);
print(join_all.replace(","," "));
