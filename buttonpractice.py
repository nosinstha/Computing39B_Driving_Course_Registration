from tkinter import *
from PIL import Image, ImageTk


# -------------------- PAGE CLASSES --------------------

class HomePage:
    def __init__(self, parent):
        Label(parent, text="HOME PAGE",
              font=("Inter", 24, "bold"),
              bg="white").pack(pady=50)


class ReservationRecordPage:
    def __init__(self, parent):
        Label(parent, text="RESERVATION RECORD PAGE",
              font=("Inter", 24, "bold"),
              bg="white").pack(pady=50)


class TrainerDetailPage:
    def __init__(self, parent):
        Label(parent, text="TRAINER DETAIL PAGE",
              font=("Inter", 24, "bold"),
              bg="white").pack(pady=50)


class ProfilePage:
    def __init__(self, parent):
        Label(parent, text="PROFILE PAGE",
              font=("Inter", 24, "bold"),
              bg="white").pack(pady=50)


# -------------------- ADMIN SYSTEM --------------------

class AdminSystem:

    def __init__(self, root):
        self.root = root
        self.root.title("Admin Home Page")
        self.root.geometry("900x900")

        self.create_header()
        self.create_sidebar()
        self.create_filter()
        self.create_content()

        self.show_home()   # default page after login

    # ---------------- HEADER ----------------
    def create_header(self):
        header = Frame(self.root, bg="#0f1b4c")
        header.pack(fill="x")

        Label(header,
              text="Hi Admin, Welcome !",
              font=("Josefins Sans", 22, "bold"),
              fg="white",
              bg="#0f1b4c").pack(pady=20)

    # ---------------- SIDEBAR ----------------
    def create_sidebar(self):
        self.sidebar = Frame(self.root, bg="#ffffff", bd=1, relief="solid", width=140)
        self.sidebar.pack(side=LEFT, fill="y")

        self.buttons = {}

        self.buttons["home"] = self.create_sidebar_button(
            "home.ico", 100, "Home", self.show_home)

        self.buttons["record"] = self.create_sidebar_button(
            "report.ico", 200, "Reservation\nRecord", self.show_record)

        self.buttons["trainer"] = self.create_sidebar_button(
            "table.ico", 317, "Trainer\nDetail", self.show_trainer)

        self.buttons["profile"] = self.create_sidebar_button(
            "profile.ico", 440, "Profile", self.show_profile)

    def create_sidebar_button(self, icon, y, text, command):
        img = ImageTk.PhotoImage(Image.open(icon).resize((30, 30)))
        btn = Button(self.sidebar, image=img, command=command, bg="white")
        btn.image = img
        btn.place(x=50, y=y)

        Label(self.sidebar, text=text,
              font=("Inder", 10, "bold"),
              bg="white").place(x=40, y=y + 40)

        return btn

    def reset_sidebar_colors(self):
        for btn in self.buttons.values():
            btn.config(bg="white")

    # ---------------- FILTER ----------------
    def create_filter(self):
        filter_frame = Frame(self.root, bg="#9aa728", height=100)
        filter_frame.pack(fill="x")

        Label(filter_frame, text="Filter :",
              font=("Inter", 16, "bold"),
              bg="#9aa728").pack(side=LEFT, padx=20, pady=30)

        Button(filter_frame, text="Search",
               bg="black", fg="white",
               activebackground="#AA2800").pack(side=LEFT, padx=10)

    # ---------------- CONTENT ----------------
    def create_content(self):
        self.content = Frame(self.root, bg="white", bd=1, relief="solid")
        self.content.pack(fill=BOTH, expand=True, padx=10, pady=10)

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    # ---------------- PAGE SWITCHING ----------------
    def show_home(self):
        self.reset_sidebar_colors()
        self.buttons["home"].config(bg="#6a88ff")
        self.clear_content()
        HomePage(self.content)

    def show_record(self):
        self.reset_sidebar_colors()
        self.buttons["record"].config(bg="#6a88ff")
        self.clear_content()
        ReservationRecordPage(self.content)

    def show_trainer(self):
        self.reset_sidebar_colors()
        self.buttons["trainer"].config(bg="#6a88ff")
        self.clear_content()
        TrainerDetailPage(self.content)

    def show_profile(self):
        self.reset_sidebar_colors()
        self.buttons["profile"].config(bg="#6a88ff")
        self.clear_content()
        ProfilePage(self.content)


# -------------------- RUN (AFTER LOGIN) --------------------

if __name__ == "__main__":
    root = Tk()
    AdminSystem(root)   # ← called after admin login success
    root.mainloop()
