from datetime import datetime
import time
import feedparser
import tkinter as tk

feed_url = "https://rss.aishort.top/?type=baidu"

def show_news():
    text.delete(1.0, tk.END)
    i =1
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        news = f"{i}. {entry.title}\n{entry.link}\n{entry.published}\n"
        text.insert(tk.END, news)
        i +=1

# Create the main window
root = tk.Tk()
root.title("RSSnews")
root.geometry("512x720")
root.config(bg="gray")
root.resizable(False, False)

#设置图标
#root.iconbitmap("")

# Create a button widget
button = tk.Button(root, text="Refrush", command=show_news)
button.config(font=("Arial", 14))
button.pack(pady=2)

#创建滚动文本框
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text = tk.Text(root, yscrollcommand=scrollbar.set)
text.pack(side=tk.LEFT, fill=tk.BOTH)
text.config(font=("Arial", 13))
text.config(bg="white")
scrollbar.config(command=text.yview)

# Start the Tkinter event loop
root.mainloop()