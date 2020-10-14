from tkinter import *
root = Tk()
root.title('Web Scraper @imtiaz')
openingmsg = Label(root, text = 'Enter a website name down below', fg='red')
openingmsg.pack()



def mainProgram(name):
    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup
    import ssl

    # you can ignor it
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.varify_mode = ssl.CERT_NONE

    url = name
    page = urllib.request.urlopen(url, context=ctx).read()
    tag_tree = BeautifulSoup(page, 'html.parser')
    sites = list()

    ##Retrieve all of the anchor tags
    tags = tag_tree('a')
    for tag in tags:
        n = tag.get('href', None)
        sites.append(n)
    return sites




def myClick():
    #new_sites = list()
    new_sites = mainProgram(entry_widget.get())
    for i in range(len(new_sites)):
        myLabel = Label(root, text=new_sites[i], fg='red', bg='black',borderwidth=5,width=100)
        myLabel.pack()


# Input Box
entry_widget = Entry(root, width=50, borderwidth=5)
entry_widget.pack()

# Button
myButton = Button(root, text='Enter', command=myClick)
myButton.pack()

# Result Massage
result_text = Label(root, text='[ Where are the web-links on that particular webpage ]')
result_text.pack()



root.mainloop()