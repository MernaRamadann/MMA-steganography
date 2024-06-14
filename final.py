import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import base64
from io import BytesIO
import os

DEFAULT_SAVE_DIR = os.path.join(os.path.expanduser("~"), "MMASteganographyImages")
if not os.path.exists(DEFAULT_SAVE_DIR):
    os.makedirs(DEFAULT_SAVE_DIR)

logo_base64 = "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"
# Add other base64 strings here if needed

class ImageSteganography:
    MAX_COLOR_VALUE = 256
    MAX_BIT_VALUE = 8

    def __init__(self, n_bits):
        self.n_bits = n_bits

    def make_image(self, data, resolution, mode="RGB"):
        image = Image.new(mode, resolution)
        image.putdata(data)
        return image

    def get_n_least_significant_bits(self, value, n):
        return value & ((1 << n) - 1)

    def shift_n_bits_to_8(self, value, n):
        return value << (self.MAX_BIT_VALUE - n)

    def remove_n_least_significant_bits(self, value, n):
        return value & ~((1 << n) - 1)

    def get_n_most_significant_bits(self, value, n):
        return value >> (self.MAX_BIT_VALUE - n)

    def encode_image(self, image_to_hide_path, image_to_hide_in_path, encoded_image_path):
        print(f"Encoding image: {image_to_hide_path} into {image_to_hide_in_path}")
        image_to_hide = Image.open(image_to_hide_path)
        image_to_hide_in = Image.open(image_to_hide_in_path)

        if image_to_hide.mode != 'RGB':
            image_to_hide = image_to_hide.convert('RGB')
        if image_to_hide_in.mode != 'RGB':
            image_to_hide_in = image_to_hide_in.convert('RGB')

        if image_to_hide.size != image_to_hide_in.size:
            image_to_hide = image_to_hide.resize(image_to_hide_in.size, Image.Resampling.LANCZOS)

        width, height = image_to_hide_in.size
        hide_image = image_to_hide.load()
        hide_in_image = image_to_hide_in.load()

        data = []

        for y in range(height):
            for x in range(width):
                r_hide, g_hide, b_hide = hide_image[x, y]
                r_hide_in, g_hide_in, b_hide_in = hide_in_image[x, y]

                r_new = self.remove_n_least_significant_bits(r_hide_in, self.n_bits) | self.get_n_most_significant_bits(r_hide, self.n_bits)
                g_new = self.remove_n_least_significant_bits(g_hide_in, self.n_bits) | self.get_n_most_significant_bits(g_hide, self.n_bits)
                b_new = self.remove_n_least_significant_bits(b_hide_in, self.n_bits) | self.get_n_most_significant_bits(b_hide, self.n_bits)

                data.append((r_new, g_new, b_new))

        encoded_image = self.make_image(data, (width, height), 'RGB')
        encoded_image.save(encoded_image_path, "PNG")
        print(f"Encoded image saved at: {encoded_image_path}")

    def decode_image(self, encoded_image_path, decoded_image_path):
        print(f"Decoding image: {encoded_image_path}")
        image_to_decode = Image.open(encoded_image_path)
        width, height = image_to_decode.size
        encoded_image = image_to_decode.load()

        data = []

        for y in range(height):
            for x in range(width):
                r, g, b = encoded_image[x, y]

                r_decoded = self.shift_n_bits_to_8(self.get_n_least_significant_bits(r, self.n_bits), self.n_bits)
                g_decoded = self.shift_n_bits_to_8(self.get_n_least_significant_bits(g, self.n_bits), self.n_bits)
                b_decoded = self.shift_n_bits_to_8(self.get_n_least_significant_bits(b, self.n_bits), self.n_bits)

                data.append((r_decoded, g_decoded, b_decoded))

        decoded_image = self.make_image(data, image_to_decode.size, image_to_decode.mode)
        decoded_image.save(decoded_image_path, "PNG")
        print(f"Decoded image saved at: {decoded_image_path}")
        return decoded_image

class TextSteganography:
    def __init__(self):
        self.image = None
        self.img_arr = None
        self.height = None
        self.width = None
        self.channels = None

    def load_image(self, image_path):
        self.image = Image.open(image_path)
        if self.image.mode != 'RGB':
            self.image = self.image.convert('RGB')
        self.img_arr = np.array(self.image)
        self.height, self.width, self.channels = self.img_arr.shape

    def encode_message(self, image_path, message, encoded_image_path='encoded.png', stop_indicator="$NEURAL"):
        self.load_image(image_path)
        message_to_hide = message + stop_indicator  # Append the stop indicator to the message
        byte_message = ''.join([f"{ord(c):08b}" for c in message_to_hide])  # Convert message to binary
        bits = len(byte_message)

        # Check if the image can hold the message
        pixels = self.width * self.height
        if bits > pixels:
            print("Not enough space in the image.")
            return

        index = 0
        for i in range(self.height):
            for j in range(self.width):
                if index < bits:
                    self.img_arr[i, j, 0] = self.img_arr[i, j, 0] & ~1 | int(byte_message[index])
                    index += 1
                if index == bits:
                    break
            if index == bits:
                break

        result = Image.fromarray(self.img_arr.astype('uint8'), 'RGB')
        result.save(encoded_image_path)
        print(f"Message encoded and saved to {encoded_image_path}")

    def decode_message(self, encoded_image_path, stop_indicator="$NEURAL"):
        self.load_image(encoded_image_path)
        secret_bits = [bin(pixel[0])[-1] for row in self.img_arr for pixel in row]

        message_bits = ''.join(secret_bits)
        secret_message = ''.join([chr(int(message_bits[i:i + 8], 2)) for i in range(0, len(message_bits), 8)])

        end_index = secret_message.find(stop_indicator)

        if end_index != -1:
            return secret_message[:end_index]
        else:
            return "Could not find the secret message."

def base64_to_image(base64_string):
    image_data = base64.b64decode(base64_string)
    image = Image.open(BytesIO(image_data))
    return image


steg = ImageSteganography(2)
text_steg = TextSteganography()

source_image_path = None
hide_image_path = None
encoded_image_path = "encoded.png"  # Define this variable globally
decoded_image_path = None
decoded_image_result_path = None

encoding_text_area_ref = None
decoding_text_area_ref = None

def encode():
    open_encode_page()

def open_encode_page():
    global encoding_text_area_ref
    encode_window = tk.Toplevel(root)
    encode_window.title("Encode")
    encode_window.geometry("800x800")
    encode_window.configure(bg="#0d1b2a")

    back_button = tk.Button(encode_window, text="←", command=encode_window.destroy, bg="#00bfff", fg="white",
                            font=("Arial", 12, "bold"), width=2, height=1)
    back_button.place(x=10, y=10)

    encode_label = tk.Label(encode_window, text="ENCODE", bg="#0d1b2a", fg="#00bfff", font=("Arial", 18, "bold"))
    encode_label.pack(pady=20)

    # Assuming logo_base64 is defined elsewhere
    logo_image = base64_to_image(logo_base64)
    logo_image = logo_image.resize((50, 50), Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(encode_window, image=logo_photo, bg="#0d1b2a")
    logo_label.image = logo_photo
    logo_label.place(relx=0.92, y=10)

    image_frame = tk.Frame(encode_window, width=220, height=220, bg="#1a2b3c", relief="ridge", borderwidth=2)
    image_frame.pack(pady=10)
    image_frame.pack_propagate(False)

    hidden_frame = tk.Frame(encode_window, width=220, height=220, bg="#1a2b3c", relief="ridge", borderwidth=2)
    hidden_frame.pack(pady=10)
    hidden_frame.pack_propagate(False)

    hidden_image_placeholder = tk.Label(hidden_frame, text="No image", bg="#1a2b3c", fg="white")
    hidden_image_placeholder.pack(expand=True)

    image_placeholder = tk.Label(image_frame, text="No image", bg="#1a2b3c", fg="white")
    image_placeholder.pack(expand=True)

    def upload_photo():
        global source_image_path
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            uploaded_image = Image.open(file_path)
            source_image_path = file_path
            uploaded_image = uploaded_image.resize((200, 200), Image.LANCZOS)
            uploaded_photo = ImageTk.PhotoImage(uploaded_image)
            image_placeholder.configure(image=uploaded_photo, text="")
            image_placeholder.image = uploaded_photo

    def upload_hidden_photo():
        global hide_image_path
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            uploaded_image = Image.open(file_path)
            hide_image_path = file_path
            uploaded_image = uploaded_image.resize((200, 200), Image.LANCZOS)
            uploaded_photo = ImageTk.PhotoImage(uploaded_image)
            hidden_image_placeholder.configure(image=uploaded_photo, text="")
            hidden_image_placeholder.image = uploaded_photo

    upload_button = tk.Button(encode_window, text="Upload photo", command=upload_photo, bg="#00bfff", fg="white",
                              font=("Arial", 12), width=12)
    upload_button.pack(pady=5)

    def save_encoded_image():
        default_save_path = os.path.join(DEFAULT_SAVE_DIR, "encoded_image.png")
        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 initialdir=DEFAULT_SAVE_DIR,
                                                 initialfile="encoded_image.png",
                                                 filetypes=[("PNG files", ".png"), ("All files", ".*")])
        if save_path:
            encoded_image = Image.open(encoded_image_path)
            encoded_image.save(save_path)
        else:
            # Save to default path if no path is chosen
            encoded_image = Image.open(encoded_image_path)
            encoded_image.save(default_save_path)
            print(f"Encoded image saved to default location: {default_save_path}")

    text_area = tk.Text(encode_window, height=5, width=40)
    text_area.pack(pady=10)
    encoding_text_area_ref = text_area

    button_frame = tk.Frame(encode_window, bg="#0d1b2a")
    button_frame.pack(pady=10)

    add_file_button = tk.Button(button_frame, text="Add image", command=upload_hidden_photo, bg="#00bfff", fg="white",
                                font=("Arial", 12), width=12)
    add_file_button.pack(side=tk.LEFT, padx=10)

    save_button = tk.Button(button_frame, text="Save image", command=save_encoded_image, bg="#00bfff", fg="white",
                            font=("Arial", 12), width=12)
    save_button.pack(side=tk.LEFT, padx=10)

    process_button = tk.Button(button_frame, text="PROCESS", command=process_encode, bg="#00bfff", fg="white",
                               font=("Arial", 12, "bold"), width=12)
    process_button.pack(side=tk.LEFT, padx=10)


def process_encode():
    global steg, encoding_text_area_ref, encoded_image_path
    text = encoding_text_area_ref.get("1.0", tk.END)
    if text.strip() != "":
        text_steg.encode_message(source_image_path, text, encoded_image_path)
    else:
        steg.encode_image(hide_image_path, source_image_path, encoded_image_path)

def process_decode():
    global steg, decoded_image_result_path
    text = text_steg.decode_message("encoded.png")
    if text != "Could not find the secret message.":
        decoding_text_area_ref.delete("1.0", tk.END)
        decoding_text_area_ref.insert(tk.END, text)
    else:
        decoded_image_result_path = "decoded.png"
        steg.decode_image(decoded_image_path, decoded_image_result_path)

def open_decode_page():
    global decoding_text_area_ref
    decode_window = tk.Toplevel(root)
    decode_window.title("Decode")
    decode_window.geometry("800x800")
    decode_window.configure(bg="#0d1b2a")

    back_button = tk.Button(decode_window, text="←", command=decode_window.destroy, bg="#ff4500", fg="white", font=("Arial", 12, "bold"), width=2, height=1)
    back_button.place(x=10, y=10)

    decode_label = tk.Label(decode_window, text="DECODE", bg="#0d1b2a", fg="#ff4500", font=("Arial", 18, "bold"))
    decode_label.pack(pady=20)

    logo_image = base64_to_image(logo_base64)
    logo_image = logo_image.resize((50, 50), Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(decode_window, image=logo_photo, bg="#0d1b2a")
    logo_label.image = logo_photo
    logo_label.place(relx=0.92, y=10)

    image_frame = tk.Frame(decode_window, width=220, height=220, bg="#800000", relief="ridge", borderwidth=2)
    image_frame.pack(pady=10)
    image_frame.pack_propagate(False)

    image_placeholder = tk.Label(image_frame, text="No image", bg="#800000", fg="white")
    image_placeholder.pack(expand=True)

    def upload_photo():
        global decoded_image_path
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            uploaded_image = Image.open(file_path)
            decoded_image_path = file_path
            uploaded_image = uploaded_image.resize((200, 200), Image.LANCZOS)
            uploaded_photo = ImageTk.PhotoImage(uploaded_image)
            image_placeholder.configure(image=uploaded_photo, text="")
            image_placeholder.image = uploaded_photo

    def save_decoded_image():
        global decoded_image_result_path
        default_save_path = os.path.join(DEFAULT_SAVE_DIR, "decoded_image.png")
        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 initialdir=DEFAULT_SAVE_DIR,
                                                 initialfile="decoded_image.png",
                                                 filetypes=[("PNG files", ".png"), ("All files", ".*")])
        if save_path:
            decoded_image = Image.open(decoded_image_result_path)
            decoded_image.save(save_path)
        else:
            # Save to default path if no path is chosen
            if decoded_image_result_path:
                decoded_image = Image.open(decoded_image_result_path)
                decoded_image.save(default_save_path)
                print(f"Decoded image saved to default location: {default_save_path}")
            else:
                print("No decoded image to save")

    result_area = tk.Text(decode_window, height=5, width=40)
    result_area.pack(pady=10)
    decoding_text_area_ref = result_area

    button_frame = tk.Frame(decode_window, bg="#0d1b2a")
    button_frame.pack(pady=10)

    upload_button = tk.Button(button_frame, text="Upload photo", command=upload_photo, bg="#ff4500", fg="white", font=("Arial", 12), width=12)
    upload_button.pack(side=tk.LEFT, padx=10)

    save_button = tk.Button(button_frame, text="Save image", command=save_decoded_image, bg="#ff4500", fg="white", font=("Arial", 12), width=12)
    save_button.pack(side=tk.LEFT, padx=10)

    process_button = tk.Button(button_frame, text="PROCESS", command=process_decode, bg="#ff4500", fg="white", font=("Arial", 12, "bold"), width=12)
    process_button.pack(side=tk.LEFT, padx=10)

root = tk.Tk()
root.title("MMA Steganography")
root.geometry("300x500")
root.configure(bg="#0d1b2a")

logo_image = base64_to_image(logo_base64)
logo_image = logo_image.resize((150, 150), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(root, image=logo_photo, bg="#0d1b2a")
logo_label.pack(pady=20)

main_label = tk.Label(root, text="Choose what do you want", fg="white", bg="#0d1b2a", font=("Arial", 14))
main_label.pack(pady=10)

encode_button = tk.Button(root, text="ENCODE", command=encode, bg="#00bfff", fg="white", font=("Arial", 14, "bold"), width=10, height=2)
encode_button.pack(pady=10)

decode_button = tk.Button(root, text="DECODE", command=open_decode_page, bg="#ff4500", fg="white", font=("Arial", 14, "bold"), width=10, height=2)
decode_button.pack(pady=10)

root.mainloop()
