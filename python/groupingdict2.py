def main():
        groups=[]
        for i in range(20):
            groups.append(set())
        with open('C:\\Users\\Home-PC\\Desktop\\rajkot data\\happy.txt','r')as f:
            content=f.read()
            words= content.split()
            for word in words:
                word= word.upper()
                size=len(word)
                groups[size].add(word)
                        
            for size,group in enumerate (groups):
                print(size,':',group)
main()       
