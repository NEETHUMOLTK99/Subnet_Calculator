# subnet calculator using tkinter
import re
from tkinter import *
win= Tk()
win.geometry("650x250")
win.config(bg='#808080')


def main_fun():
    ipr = ip.get()
    subnet=int(subnet_add.get())
    sub_net_str=''.join(str("1"*subnet+"0"*(32-subnet))) 
    abc = re.findall('........',sub_net_str)
    jkl = []
    for i in abc:
        jkl.append(int(i,2)) #convert to ip code
    subnet_mask_ipv4 =".".join(map(str, jkl))
    
    #create network address(subnetmask_adr & ip_addres)
    
    network_lst = []
    new = list(ipr.split("."))
    for i in range(len(new)):
        network_lst.append(int(new[i]) & jkl[i])
    network_address = ".".join(map(str, network_lst))
  
    #broad cast address (net.aadr , subnetmask addre) 
    
    str_inverted_subnet=''.join(str("0"*subnet+"1"*(32-subnet)))
    inverted= re.findall('........',str_inverted_subnet)
    inver_lst = []
    
    for i in inverted:
        inver_lst.append(int(i,2)) #conert to decimal
    brodcast_lst = []
    new1 = list(network_address.split("."))
    
    for i in range(len(new)):
        brodcast_lst.append(int(new1[i]) | inver_lst[i]) #decimal version (n/w addres OR inverted_subnetaddr)
        
    brodacast_address = ".".join(map(str, brodcast_lst))
    
    No_of_available_IP_address= pow(2, 32-subnet) # 2^n 
    
    useable_ip_address = No_of_available_IP_address - 2 # 2^n -2

    network_lst_for_range = list(network_address.split("."))
    network_lst_for_range[3] = int(network_lst_for_range[3]) + 1
    start_range = ".".join(map(str, network_lst_for_range))
    brodcast_lst[3] = int(brodcast_lst[3]) - 1
    end_range = ".".join(map(str, brodcast_lst))
    range1 = start_range + " - " + end_range

	# result window
	
    new= Toplevel(win)
    new.geometry("750x400")
    new.config(bg='#808080')
    new.title("Result")
    Label(new, text="ip address : ", font=('Helvetica 17 bold'),bg="green").place(x=10,y=40)
    Label(new, text=ipr, font=('Helvetica 17 bold'),bg="green").place(x=300,y=40)
    Label(new, text="subnet mask : ", font=('Helvetica 17 bold'),bg="green").place(x=10,y=70)
    Label(new, text=subnet_mask_ipv4, font=('Helvetica 17 bold'),bg="green").place(x=300,y=70)
    Label(new, text="Network address : ", font=('Helvetica 17 bold'),bg="green").place(x=10,y=100)
    Label(new, text=network_address, font=('Helvetica 17 bold'),bg="green").place(x=300,y=100)
    Label(new, text="Broadcast address : ", font=('Helvetica 17 bold'),bg="green").place(x=10,y=130)
    Label(new, text=brodacast_address, font=('Helvetica 17 bold'),bg="green").place(x=300,y=130)
    Label(new, text="No.of available IP address:", font=('Helvetica 17 bold'),bg="green").place(x=10,y=160)
    Label(new, text=useable_ip_address, font=('Helvetica 17 bold'),bg="green").place(x=320,y=160)
    Label(new, text="Range : ", font=('Helvetica 17 bold'),bg="green").place(x=10,y=190)
    Label(new, text=range1, font=('Helvetica 17 bold'),bg="green").place(x=300,y=190)
def clear():
	ip.set('')
	subnet_add.set('')
	
	
#main window
win.title('Subnet Calculator')
win.geometry('500x500')
win.config(bg='#808080')
label1 = Label(win, text="enter the ip address : ", bg="violet", fg="white").place(x=10,y=40)
label2 = Label(win, text="enter the subnetmask : ", bg="violet", fg="white").place(x=10,y=80)
ip = StringVar(win)
subnet_add=StringVar(win)

#typing space
ip_addr = Entry(win, bd =5,textvariable=ip).place(x=190,y=40)
sub_net_mask = Entry(win, bd =5,textvariable=subnet_add).place(x=190,y=80)

#button
button1 = Button(win,text="Calculate",command=main_fun).place(x=140,y=150)
button2 = Button(win,text="clear",command=clear).place(x=250,y=150)



win.mainloop()
