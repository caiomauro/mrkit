import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar

class AppointmentScheduler(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("MrkIt")
        self.geometry("600x400")

        # Create frames for the different sections of the app
        self.header_frame = tk.Frame(self)
        self.header_frame.configure(bg='AntiqueWhite1')
        self.header_frame.pack(side=tk.TOP, fill=tk.X)

        self.calendar_frame = tk.Frame(self)
        self.calendar_frame.configure(bg='AntiqueWhite1')
        self.calendar_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.details_frame = tk.Frame(self)
        self.details_frame.configure(bg='AntiqueWhite1')
        self.details_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create the calendar widget
        self.calendar = Calendar(self.calendar_frame)
        self.calendar.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create the widgets for entering appointment details
        self.name_label = tk.Label(self.details_frame, text="Name:")
        self.name_label.pack(side=tk.TOP)
        self.name_entry = tk.Entry(self.details_frame)
        self.name_entry.pack(side=tk.TOP)

        self.phone_label = tk.Label(self.details_frame, text="Phone:")
        self.phone_label.pack(side=tk.TOP)
        self.phone_entry = tk.Entry(self.details_frame)
        self.phone_entry.pack(side=tk.TOP)

        self.email_label = tk.Label(self.details_frame, text="Email:")
        self.email_label.pack(side=tk.TOP)
        self.email_entry = tk.Entry(self.details_frame)
        self.email_entry.pack(side=tk.TOP)

        # Add a notes section for the appointment details
        self.notes_label = tk.Label(self.details_frame, text="Notes:")
        self.notes_label.pack(side=tk.TOP)
        self.notes_text = tk.Text(self.details_frame, height=10, width=30, wrap=tk.WORD)
        self.notes_text.pack(side=tk.TOP)

        # Add a button to create the appointment
        self.create_button = tk.Button(self.details_frame, text="Create Appointment", command=self.create_appointment)
        self.create_button.pack(side=tk.TOP)

        # Add a button to create the appointment
        self.create_button = tk.Button(self.details_frame, text="Show Details", command=lambda: self.show_appointment(self.calendar.selection_get()))
        self.create_button.pack(side=tk.TOP)

        # Create a dictionary to store the appointments
        self.appointments = {}

    # Function to create an appointment
    def create_appointment(self):
        # Get the date for the appointment from the calendar widget
        appointment_date = self.calendar.selection_get()

        # Get the details for the appointment from the text boxes and text area
        appointment_name = self.name_entry.get()
        appointment_phone = self.phone_entry.get()
        appointment_email = self.email_entry.get()
        appointment_notes = self.notes_text.get("1.0", tk.END)

        # Store the appointment information in the appointments dictionary using the date as the key
        self.appointments[appointment_date] = (appointment_name, appointment_phone, appointment_email, appointment_notes)

        # Add an appointment indicator to the calendar
        self.calendar.calevent_create(appointment_date, 'Appointment', 'red')

        # Clear the text boxes and text area
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.notes_text.delete("1.0", tk.END)

        # Update the calendar to show the appointment date
        self.calendar.selection_set(appointment_date)

    def show_appointment(self, appointment_date):
        # Get the details for the appointment from the appointments dictionary
        appointment_name, appointment_phone, appointment_email, appointment_notes = self.appointments[appointment_date]

        # Display the appointment information in a message box
        messagebox.showinfo("Appointment Details", f"Name: {appointment_name}\nPhone: {appointment_phone}\nEmail: {appointment_email}\nNotes: {appointment_notes}")
    
if __name__ == "__main__":
    app = AppointmentScheduler()
    app.mainloop()
