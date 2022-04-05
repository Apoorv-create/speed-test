from tkinter import *
import speedtest 

root = Tk()
root.config(bg = "#dee8f1")
root.title("Internet Speed Checker")
root.geometry("500x500")

label = Label(root, text = "Internet Speed Check", font=("Lucida Sans Unicode", 20, "bold", "italic"), fg = "#5D6D7E", bg = "#dee8f1")
label.place(relx = 0.5, rely = 0.1, anchor=CENTER)

label_download = Label(root, text = "Download Speed below", font=("Segoe Print", 13,"italic"), fg = "#5D6D7E", bg = "#dee8f1")
label_download.place(relx =0.25, rely =0.5, anchor=CENTER)

label_upload = Label(root, text = "Upload Speed below", font=("Segoe Print", 13,"italic"), fg = "#9B59B6", bg = "#dee8f1")
label_upload.place(relx =0.75, rely =0.5, anchor=CENTER)

label_download_speed = Label(root, font=("Yu Gothic Light", 12, "italic"), bg ="#dee8f1")
label_download_speed.place(relx =0.25, rely =0.6, anchor=CENTER)

label_upload_speed = Label(root, font=("Yu Gothic Light", 12, "italic"), bg = "#dee8f1")
label_upload_speed.place(relx = 0.75, rely = 0.6, anchor=CENTER)

def speed():
    st = speedtest.Speedtest()
    download_speed = round(st.download()/1000000,2)
    label_download_speed["text"] = str(download_speed) + "mbps"
    upload_speed = round(st.upload()/1000000, 2)
    label_upload_speed["text"] = str(upload_speed) + "mbps"
    
btn_final = Button(root, text = "Check speed", command=speed, bg = "#218796", fg = "white", relief = FLAT)
btn_final.place(relx = 0.5, rely = 0.3, anchor=CENTER)

root.mainloop()