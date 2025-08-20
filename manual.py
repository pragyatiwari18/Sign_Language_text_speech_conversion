import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess

def open_final_pred():
    try:
        subprocess.Popen(["python", "final_pred.py"])
    except Exception as e:
        tk.messagebox.showerror("Error", f"Failed to launch detection script: {e}")


def open_manual():
    manual_window = tk.Toplevel()
    manual_window.title("Guidance Manual")
    manual_window.geometry("900x1200")
    manual_window.configure(bg="#f4f4f4")
    
    canvas = tk.Canvas(manual_window)
    scrollbar = tk.Scrollbar(manual_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f4f4f4")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    title_label = tk.Label(
        scrollable_frame, 
        text="Welcome to the Sign Language Detection Application!", 
        font=("Arial", 24, "bold"), 
        fg="#2E86C1", 
        bg="#f4f4f4"
    )
    title_label.pack(pady=30)

    manual_text = """This application is designed to detect and interpret hand gestures 
to assist in communication through sign language, helping those with hearing 
impairments or language barriers."""
    
    intro_label = tk.Label(
        scrollable_frame, 
        text=manual_text, 
        font=("Arial", 16), 
        justify="left", 
        wraplength=850, 
        bg="#f4f4f4"
    )
    intro_label.pack(pady=20)

    sections = [
        ("How to Use the Application", 
         """1. Connect your webcam or camera device to the computer.
2. Launch the application and ensure the camera is working properly.
3. Position your hand within the camera's frame, with good lighting and minimal background clutter.
4. Adjust your hand's position to align with the gestures recognized by the system.
5. The system will process the image and display the detected sign in real-time."""),

        ("Guidelines for Accurate Detection", 
         """- Ensure your hand is clearly visible and the main focus in the camera frame.
- Avoid wearing accessories like watches or rings that may confuse the detection algorithm.
- Make sure the background is plain, with minimal objects and good lighting to aid detection."""),

        ("Recognized Gestures", 
         """The system recognizes hand gestures from American Sign Language (ASL). Each gesture corresponds 
to a specific sign in the database. Refer to the image below for the complete hand gesture chart."""),

        ("Troubleshooting", 
         """- If gestures are not being detected, ensure the camera is working correctly and restart the application.
- Check that your hand is clearly visible in the frame, and try adjusting the distance or angle of your hand.
- If the application lags or fails to recognize gestures, ensure the lighting is sufficient and the background is simple."""),

        ("Additional Information", 
         """- The system currently supports ASL gestures.
- Future updates may include support for other international sign languages.
- For feedback, bug reports, or technical assistance, please email us at DiyaRathor@gmail.com.""")
    ]

    for section_title, section_content in sections:
        section_title_label = tk.Label(
            scrollable_frame, 
            text=section_title, 
            font=("Arial", 18, "bold"), 
            fg="#2874A6", 
            bg="#f4f4f4"
        )
        section_title_label.pack(pady=(30, 10))

        section_content_label = tk.Label(
            scrollable_frame, 
            text=section_content, 
            font=("Arial", 14), 
            justify="left", 
            wraplength=850, 
            bg="#f4f4f4"
        )
        section_content_label.pack(pady=10)


    open_script_button = ttk.Button(
        manual_window,  
        text="Start Sign Language Detection", 
        command=open_final_pred,
        style="Custom.TButton"
    )
    open_script_button.pack(pady=30)

    open_script_button.place(relx=0.5, rely=0.95, anchor="center")

    manual_window.protocol("WM_DELETE_WINDOW", open_final_pred)


def main():
    root = tk.Tk()
    root.title("Sign Language Detection Application")
    root.geometry("800x600")
    root.configure(bg="#f4f4f4")

    title = tk.Label(root, text="Sign Language Detection Application", font=("Arial", 22, "bold"), bg="#f4f4f4", fg="#2E86C1")
    title.pack(pady=30)

    guidance_button = ttk.Button(root, text="Open Guidance Manual", command=open_manual, style="Custom.TButton")
    guidance_button.pack(pady=20)

    image_path = "signs.png"
    try:
        img = Image.open(image_path)
        img = img.resize((600, 400), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        img_label = tk.Label(root, image=img_tk, bg="#f4f4f4")
        img_label.image = img_tk
        img_label.pack(pady=20)
    except FileNotFoundError:
        error_label = tk.Label(root, text="Error: Hand gestures image not found.", fg="red", bg="#f4f4f4")
        error_label.pack(pady=20)

    style = ttk.Style()
    style.configure("Custom.TButton",
                    font=("Arial", 14, "bold"),
                    padding=10,
                    background="#2E86C1", 
                    foreground="blue", 
                    relief="flat", 
                    anchor="center")

    style.map("Custom.TButton",
              background=[("active", "#2874A6"), ("pressed", "#1C5985")],
              foreground=[("active", "red"), ("pressed", "white")])

    root.mainloop()#tkinter application ruka hai mere liye button dbane ko


if __name__ == "__main__":
    main()
#python idiom bolte hai ise vese,joh check krta hai file is bring run in main program or not