import tkinter as tk
from ImgurScraper import ImgurScraper

def close_app():
    window.destroy()

def run_app():
    user_search_image = str(search_image_entry.get())
    try:
        user_number_of_images = int(number_of_images_entry.get())
    except:
        alert['fg'] = 'red'
        alert['text'] = 'Error: Please input a number'
        number_of_images['fg'] = 'red'
    # Resetting text and boolean fields
    else:
        number_of_images['fg'] = 'black'
        search_image_entry.delete(0, len(search_image_entry.get()))
        number_of_images_entry.delete(0, len(number_of_images_entry.get()))

        if csv_boolean.get() == 'Yes':
            setCsv = True
        else:
            setCsv = False

        csv_boolean.set('Yes')
        bot = ImgurScraper(user_search_image, user_number_of_images, setCsv)
        bot.scrape()
        
        alert['fg'] = 'green'
        if (bot.errorCount > 0):
            alert['text'] = f'New folder saved at {bot.fileLocation}\nThere was a problem with {bot.errorCount} images.'
        else:
            alert['text'] = f'New folder saved at {bot.fileLocation}'
    

window = tk.Tk()

window.title("Image Pool")

#split window into three parts
frame_header = tk.Frame(window, borderwidth=2, pady=2)
alert_frame = tk.Frame(window, borderwidth=2, pady=2)
center_frame = tk.Frame(window, borderwidth=2, pady=5)
bottom_frame = tk.Frame(window, borderwidth=2, pady=5)
frame_header.grid(row=0, column=0)
alert_frame.grid(row=1, column = 0)
center_frame.grid(row=2, column=0)
bottom_frame.grid(row=3, column=0)

#header
header = tk.Label(frame_header, text = "Image Pool", bg='grey', fg='black', height='3', width='50', font=("Helvetica 16 bold"))
header.grid(row=0,column=0)

#alert
alert = tk.Label(alert_frame, text = '', fg='green', height='2', font=("Helvetica 8 "), wraplength=1000, justify='center')
alert.grid(row=1, column=0)



#split body into 3 lines
frame_main_1 = tk.Frame(center_frame, borderwidth=2, relief='sunken')
frame_main_2 = tk.Frame(center_frame, borderwidth=2, relief='sunken')
frame_main_3 = tk.Frame(center_frame, borderwidth=2, relief='sunken')

#Questions in body
search_image = tk.Label(frame_main_1, text="What image do you want:  ")
number_of_images = tk.Label(frame_main_2, text="How many images do you want: ")
csv_option = tk.Label(frame_main_3, text="Do you want to create a CSV: ")

#track user input
search_image1 = tk.StringVar()
number_of_images1 = tk.StringVar()
csv_option1 = tk.StringVar()
csv_boolean = tk.StringVar()
csv_boolean.set('Yes')
csv_boolean_options = {'Yes', 'No'}

#entry boxes
search_image_entry = tk.Entry(frame_main_1, textvariable = search_image1, width=17)
number_of_images_entry = tk.Entry(frame_main_2, textvariable = number_of_images1, width=10)
csv_option_dropdown = tk.OptionMenu(frame_main_3, csv_boolean, *csv_boolean_options)

#start button
button_run = tk.Button(bottom_frame, text="Start", command=run_app, bg='dark green', fg='white', relief='raised', width=10, font=('Helvetica 9 bold'))
button_run.grid(column=0, row=0, sticky='w', padx=100, pady=20)

#exit button
button_run = tk.Button(bottom_frame, text="Exit", command=close_app, bg='dark red', fg='white', relief='raised', width=10, font=('Helvetica 9 bold'))
button_run.grid(column=1, row=0, sticky='e', padx=100, pady=20)

#organize and set widgets
frame_main_1.pack(fill='x', pady=2)
frame_main_2.pack(fill='x', pady=2)
frame_main_3.pack(fill='x', pady=2)
search_image.pack(side='left')
search_image_entry.pack(side='left', padx=1)
number_of_images.pack(side='left', padx=5)
number_of_images_entry.pack(side='left', padx=1)
csv_option.pack(side='left', padx=1)
csv_option_dropdown.pack(side='left', padx=5)

window.mainloop()
