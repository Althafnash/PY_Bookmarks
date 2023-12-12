# This is a simple program in which the 
# chrome bookmarks wil display 
# Made by althafnash 


import chrome_bookmarks
for url in chrome_bookmarks.urls:
    print("==================Name==============================")
    print(url.name)
    print("===================URL=============================")
    print(url.url)
    print("================================================ \n")