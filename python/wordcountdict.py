
def main():
        counters={}
        with open('C:\\Users\\Home-PC\\Documents\\myfile.txt','r')as f:
            content=f.read()
            words= content.split()
            for word in words:
                word= word.upper()
                if word not in counters:
                    counters[word]=1
                else:
                    counters[word]+=1
            for word,count in counters.items():
                print(word,count)
main()                
