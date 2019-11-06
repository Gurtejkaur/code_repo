def main():
        groups={}
        with open('C:\\Users\\Home-PC\\Desktop\\rajkot data\\happy.txt','r')as f:
            content=f.read()
            words= content.split()
            for word in words:
                word= word.upper()
                size=len(word)
                if size in groups:
                    if word not in groups[size]:
                        groups[size]+=[word]
                else:
                    groups[size]=[word]
                        
            for size,group in groups.items():
                print(size,':',group)
main()                
