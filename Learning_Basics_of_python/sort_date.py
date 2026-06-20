dates = ["24 Jul 2017", "25 Jul 2017", "11 Jun 1996", "01 Jan 2019", "12 Aug 2005", "01 Jan 1997"];
year_wise = sorted(dates , key  = lambda x : int(x[7:11]) , reverse=False)
get_sorted = sorted(year_wise , key  = lambda x : int(x[0:2]) , reverse=False);
print(get_sorted);
