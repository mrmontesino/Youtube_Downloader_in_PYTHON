
import requests
import sys
import tkinter
from tkinter import ttk
from tkinter import messagebox, filedialog
from Downloads_Youtube_1 import download_videos, get_playlist_info


def main():
    def exit_program():
        messagebox.showinfo("Message", "Exiting program")
        window.quit()

    def validate_number(new_value):
        if new_value == "":
            return True
        try:
            int(new_value)
            return True
        except ValueError:
            return False


    def redirect_output(output__text):
        class StdoutRedirector:
            def __init__(self, text_widget):
                self.text_widget = text_widget

            def write(self, text):
                self.text_widget.insert(tkinter.END, text)

            def flush(self):
                pass

        stdout_redirector = StdoutRedirector(output__text)

        sys.stdout = stdout_redirector
        sys.stderr = stdout_redirector

    def check_url():
        url = url_entry.get()
        try:
            response = requests.get(url)
            if response.status_code == 200:
                messagebox.showinfo("Message", "URL is valid")
                return True
            else:
                messagebox.showwarning("Warning", "URL is not valid")
                return False

        except Exception as e:
            messagebox.showwarning("Warning", f"URL is not valid: {e}")

            return False

    def brow_folder():
        folder_path = filedialog.askdirectory()
        folder_label.config(text=folder_path)
        return folder_path


    def start_download():
        if check_url():
            initiate_var = messagebox.askyesno('Initiate downloads', 'Do you want to initiate the Downloads')
            url = url_entry.get()
            playlist, num_videos, download_dir, title = get_playlist_info(url)
            output_text.yview(tkinter.END)

            if initiate_var:
                messagebox.showinfo("Message", 'Starting downloads')
                if start_entry.get() == "" or end_entry.get() == "":
                    messagebox.showwarning("Warning", "Start or end entry is blank")
                    return
                else:
                    start = int(start_entry.get())
                    end = int(end_entry.get())
                    if fold_path == "":
                        pass
                    else:
                        download_dir = str(fold_path.get()) + "/" + title

                    # Call the download_videos() function here
                    download_videos(start, end, enum_entry.get(), playlist, num_videos, download_dir)
                    print(download_dir)
                    print('download task finished')
                    output_text.yview(tkinter.END)
            else:
                messagebox.showinfo("Message", 'Downloads cancelled')



    window = tkinter.Tk()
    window.iconbitmap('ico_youtube.ico')
    window.title('YouTube Downloader')
    window.geometry("550x480")
    window.resizable(width=False, height=False)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(0, weight=7)
    # Window configurations



    # labels


    url_label = ttk.Label(window, text='Playlist Url')
    url_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

    start_label = ttk.Label(window, text='Enter the starting video number')
    start_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

    end_label = ttk.Label(window, text='Enter the ending video number: ')
    end_label.grid(column=0, row=2, sticky=tkinter.W, padx=5, pady=5)

    enum_label = ttk.Label(window, text='Enumerate the videos: ')
    enum_label.grid(column=0, row=3, sticky=tkinter.W, padx=5, pady=5)

    fold_path = tkinter.StringVar()
    folder_label = tkinter.Label(window, text="")
    folder_label.grid(column=0, columnspan=2, row=6, sticky=tkinter.W, padx=5, pady=5)



    # entries

    url_entry = ttk.Entry(window, width=40)
    url_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

    validate_cmd = window.register(validate_number)

    start_entry = ttk.Entry(window, validate="key", validatecommand=(validate_cmd, '%P'), width=10)
    start_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

    end_entry = ttk.Entry(window, validate="key", validatecommand=(validate_cmd, '%P'), width=10)
    end_entry.grid(column=1, row=2, sticky=tkinter.E, padx=5, pady=5)

    enum_entry = tkinter.BooleanVar()
    enum_checkbox = ttk.Checkbutton(window, text='Yes', variable=enum_entry)
    enum_checkbox.grid(column=1, row=3, sticky=tkinter.E, padx=30, pady=5)

    output_text = tkinter.Text(window, width=65, height=15)
    output_text.grid(column=0, columnspan=2, row=7, sticky=tkinter.W, padx=5, pady=5)

    scrollbar = tkinter.Scrollbar(window)
    scrollbar.grid(column=2, row=7, sticky=tkinter.NS)
    output_text.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=output_text.yview)

    output_text.yview(tkinter.END)
    redirect_output(output_text)



    # buttons
    check_url_button = ttk.Button(window, text='Check Url', width=20, command=check_url)
    check_url_button.grid(column=0, row=4, sticky=tkinter.W, padx=5, pady=5)

    start_download_button = ttk.Button(window, text='Download', width=20, command=start_download)
    start_download_button.grid(column=1, row=4, sticky=tkinter.E, padx=5, pady=5)

    exit_button = ttk.Button(window, text='Exit program', width=20, command=exit_program)
    exit_button.grid(column=1, row=5, sticky=tkinter.E, padx=5, pady=5)

    dir_button = tkinter.Button(window, text="Browse Folder", width=15, command=lambda: fold_path.set(brow_folder()))
    dir_button.grid(column=0, row=5, sticky=tkinter.W, padx=5, pady=5)


    window.mainloop()


if __name__ == '__main__':
    main()
