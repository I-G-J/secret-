import tkinter as tk
from tkinter import messagebox
import string
import random


def generate_random_characters(length=3):
    """Generate random letters of a specified length."""
    return ''.join(random.choices(string.ascii_letters, k=length))


def copy_to_clipboard(message):
    """Copy the given message to the clipboard."""
    root.clipboard_clear()
    root.clipboard_append(message)
    root.update()
    messagebox.showinfo("Copied", "Message copied to clipboard!")


def coding():
    """Encode a given message."""
    def encode_message():
        message = entry.get().strip()
        if not message:
            messagebox.showerror("Error", "Message cannot be empty!")
            return

        if len(message) > 3:
            reversed_message = message[::-1]
            prefix = generate_random_characters()
            suffix = generate_random_characters()
            coded_message = prefix + reversed_message + suffix
        else:
            coded_message = (message[1:] + message[0])[::-1]

        result_label.config(text=f"Encoded Message: {coded_message}")
        copy_button.config(command=lambda: copy_to_clipboard(coded_message))
        copy_button.pack(pady=10)

    # Create a new window for encoding
    coding_window = tk.Toplevel(root)
    coding_window.title("Code a Message")
    coding_window.geometry("400x300")
    coding_window.configure(bg="#ADD8E6")

    tk.Label(coding_window, text="Enter the message to encode:", bg="#ADD8E6", font=("Arial", 12)).pack(pady=10)
    entry = tk.Entry(coding_window, width=40)
    entry.pack(pady=10)

    encode_button = tk.Button(coding_window, text="Encode", command=encode_message)
    encode_button.pack(pady=10)

    result_label = tk.Label(coding_window, text="", bg="#ADD8E6", font=("Arial", 12))
    result_label.pack(pady=10)

    copy_button = tk.Button(coding_window, text="Copy")
    copy_button.pack_forget()


def decoding():
    """Decode a given message."""
    def decode_message():
        message = entry.get().strip()
        if not message:
            messagebox.showerror("Error", "Message cannot be empty!")
            return

        if len(message) > 6:  # Minimum length for random chars + reversed string
            stripped_message = message[3:-3]
            decoded_message = stripped_message[::-1]
        elif len(message) > 1:
            reversed_message = message[::-1]
            decoded_message = reversed_message[-1] + reversed_message[:-1]
        else:
            messagebox.showerror("Error", "Invalid message for decoding!")
            return

        result_label.config(text=f"Decoded Message: {decoded_message}")
        copy_button.config(command=lambda: copy_to_clipboard(decoded_message))
        copy_button.pack(pady=10)

    # Create a new window for decoding
    decoding_window = tk.Toplevel(root)
    decoding_window.title("Decode a Message")
    decoding_window.geometry("400x300")
    decoding_window.configure(bg="#ADD8E6")

    tk.Label(decoding_window, text="Enter the message to decode:", bg="#ADD8E6", font=("Arial", 12)).pack(pady=10)
    entry = tk.Entry(decoding_window, width=40)
    entry.pack(pady=10)

    decode_button = tk.Button(decoding_window, text="Decode", command=decode_message)
    decode_button.pack(pady=10)

    result_label = tk.Label(decoding_window, text="", bg="#ADD8E6", font=("Arial", 12))
    result_label.pack(pady=10)

    copy_button = tk.Button(decoding_window, text="Copy")
    copy_button.pack_forget()


# Main GUI window
root = tk.Tk()
root.title("Message Coder & Decoder")
root.geometry("350x250")
root.configure(bg="#ADD8E6")

tk.Label(root, text="Message Coder & Decoder", font=("Arial", 16), bg="#ADD8E6").pack(pady=15)

# Buttons for the main options
code_button = tk.Button(root, text="Code a Message", width=20, command=coding)
code_button.pack(pady=10)

decode_button = tk.Button(root, text="Decode a Message", width=20, command=decoding)
decode_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", width=20, command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
