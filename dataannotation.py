import urllib.request
from bs4 import NavigableString, BeautifulSoup

def main(url):
    with urllib.request.urlopen(url) as fp:
        soup = BeautifulSoup(fp)
        souparray = soup.find_all("tr")
        souparray.pop(0)
        tupdict = dict()
        max_x_coord = 0;
        max_y_coord = 0
        for i in souparray:
            x_coord = -1
            y_coord = -1
            charact = "a" 
            for child in i.descendants:
                if isinstance(child, NavigableString):
                    if x_coord == -1:
                        x_coord = int(child.string)
                        if int(str(child)) > max_x_coord:
                            max_x_coord = int(str(child))
                    elif charact == "a":
                        charact = child.string
                    else:
                        y_coord = int(child.string)
                        if int(str(child)) > max_y_coord:
                            max_y_coord = int(str(child))
            #print(x_coord, charact, y_coord)
            tupdict[(x_coord,y_coord)] = charact
            #print(tupdict)
            #print(max_x_coord)
    for row in range(max_y_coord + 1, -1, -1):
        for col in range(max_x_coord + 1):
            if (col, row) in tupdict:
                print(tupdict.get((col,row)), end="")
            else:
                print(" ", end="")
        print()    

main("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")