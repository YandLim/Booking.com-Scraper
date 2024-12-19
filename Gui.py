import tkinter
from tkinter import scrolledtext
from Main import main_function

def main_interface():
    window = tkinter.Tk()
    window.title("Booking.com_Scraping")

    frame = tkinter.Frame(window, bg="gray")
    frame.pack()


    main_frame = tkinter.LabelFrame(frame, padx=10, pady=10, bg="#282c34")
    main_frame.grid(row=0, column=0, padx=20, pady=20)


    title_frame = tkinter.LabelFrame(main_frame, padx=10, pady=10, bg="#000066")
    title_frame.grid(row=0, column=0, padx=10, pady=10)

    title = tkinter.Label(title_frame, text="Booking.com_Scraping", font=("Arial Black", 20))
    title.grid(row=0, column=0, padx=8, pady=5)


    input_frame = tkinter.LabelFrame(main_frame, padx=10, pady=10, bg="#003366")
    input_frame.grid(row=1, column=0, padx=10, pady=20, sticky="news")

    input_frame_content = tkinter.Label(input_frame, text="Where you wanna go?", bg="#003366", font=("Copper Black", 15), fg="white")
    input_frame_content.grid(row=0, column=0, sticky="w")

    input_frame_entry = tkinter.Entry(input_frame, font=("Berlin Sans FB", 15), width=30)
    input_frame_entry.grid(row=1, column=0, pady=20, sticky="w")
    input_frame_entry.bind('<Return>', lambda event: input_frame_button.invoke())

    input_frame_button = tkinter.Button(input_frame, text="SUBMIT", bg="#000066", font=("Arial Black", 15), width=25, fg="white", command=lambda: submit_data())
    input_frame_button.grid(row=2, column=0, sticky="w")


    output_frame = tkinter.LabelFrame(main_frame, padx=10, pady=10, bg="#666699")
    output_frame.grid(row=2, column=0, padx=10, pady=10, sticky="news")

    output_frame_content = tkinter.Label(output_frame, text="OUTPUT", font=("Copper Black", 15), bg="#666699", fg="white")
    output_frame_content.grid(row=0, column=0)

    output_text = scrolledtext.ScrolledText(output_frame, width=25, height=10, wrap=tkinter.WORD, font=("Berlin Sans FB", 17))
    output_text.grid(pady=5)
    output_text.config(state="disabled")


    def contains_digits(value):
        return any(char.isdigit() for char in value)


    def submit_data():
        user_input = input_frame_entry.get()
        if user_input == "" or contains_digits(user_input):
            output_text.config(state="normal")
            output_text.insert(tkinter.END, (f"The input is not valid\nTry again\n"))
            output_text.config(state="disabled")
            input_frame_entry.delete(0, tkinter.END)
            return


        output, saved = main_function(user_input)

        output_text.config(state="normal")
        output_text.insert(tkinter.END, (f"{output}\n{saved}"))
        output_text.config(state="disabled")

        input_frame_entry.delete(0, tkinter.END)


    window.mainloop()

main_interface()

