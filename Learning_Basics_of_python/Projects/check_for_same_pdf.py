import hashlib;
if __name__=="__main__":
    h1=hashlib.sha1();
    h2=hashlib.sha1();
    with open("xyz001.pdf","rb") as fl001:
        chunks=0;
        while chunks!=b"":
            chunks=fl001.read(1024);
            h1.update(chunks);
    with open("abc001.pdf","rb") as fl002:
        chunks=0;
        while chunks!=b"":
            chunks=fl002.read(1024);
            h2.update(chunks);
    if h1.hexdigest()==h2.hexdigest():
        print("Same");
    else:
        print("Not Same");