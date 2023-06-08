import customtkinter


class Cele_Xetass(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        self.title("Xetass")
        self.minsize(376, 421)
        self.maxsize(376, 421)
        self.attributes('-topmost', 'true')
        self.attributes("-alpha", 0.7)


        self.grid_rowconfigure((0,1), weight=1)
        self.grid_columnconfigure((0,1), weight=1)

        self.cards_Frame = Cards_Frame(self)
        self.cards_Frame.grid(row=0, column=0, pady=0.2, sticky="N")

        self.reset_button = customtkinter.CTkButton(self, text="Reset", command=self.reset)
        self.reset_button.grid(row=1, column=0)

    def reset(self):
        for button in self.cards_Frame.buttons:
            button.configure(fg_color="transparent")








class Cards_Frame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(width=368)
        self.configure(height=368)
        self.configure(bg_color="transparent")
        self.configure(fg_color="transparent")

        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        self.buttons = [Card_Button(self) for i in range(25)]
        row = 0
        column = 0
        for button in self.buttons:
            button.grid(row=row, column=column, padx=7.4, pady=7.4)
            if column == 4:
                row += 1
                column = 0
            else:
                column += 1





class Card_Button(customtkinter.CTkButton):
    def __init__(self, master):
        super().__init__(master)

        self.configure(width=58.5)
        self.configure(height=58.5)
        self.configure(text="")
        self.configure(fg_color="transparent")
        self.configure(command= self.check_button_card)
        self.configure(border_width=1)
        self.configure(border_color="red")


    def check_button_card(self):
        if self._fg_color == "transparent":
            self.configure(fg_color="green")
        else:
            self.configure(fg_color="transparent")



if __name__ == "__main__":

    cele_xetass = Cele_Xetass()
    cele_xetass.mainloop()

