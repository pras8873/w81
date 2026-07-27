import os
import struct
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

# Binary structure definitions for .cos files
HEADER_SIZE = 40   # 0x28 bytes header offset
RECORD_SIZE = 20   # 20 bytes per record
FMT = "<5f"        # 5 x 32-bit Little-Endian Floats per record


def convert_cos_to_excel():
    """Opens dialog to select a .cos file, converts it, and asks where to save .xlsx."""
    # 1. Ask user to open the input .cos file
    cos_path = filedialog.askopenfilename(
        title="Select Input .COS File",
        filetypes=[("COS Files (*.cos)", "*.cos"), ("All Files (*.*)", "*.*")]
    )
    if not cos_path:
        return  # User canceled dialog

    # 2. Ask user where to save the output Excel file
    default_xlsx_name = os.path.splitext(os.path.basename(cos_path))[0] + ".xlsx"
    excel_path = filedialog.asksaveasfilename(
        title="Save Converted Excel File As",
        initialfile=default_xlsx_name,
        defaultextension=".xlsx",
        filetypes=[("Excel Files (*.xlsx)", "*.xlsx"), ("All Files (*.*)", "*.*")]
    )
    if not excel_path:
        return  # User canceled dialog

    # 3. Process Binary Data to Excel
    try:
        with open(cos_path, "rb") as f:
            header_bytes = f.read(HEADER_SIZE)
            body_bytes = f.read()

        num_records = len(body_bytes) // RECORD_SIZE
        records = []

        for i in range(num_records):
            chunk = body_bytes[i * RECORD_SIZE : (i + 1) * RECORD_SIZE]
            if len(chunk) == RECORD_SIZE:
                vals = struct.unpack(FMT, chunk)
                records.append(vals)

        # Build Data & Metadata Frames
        col_names = ["Value_1", "Value_2", "Value_3", "Value_4", "Value_5"]
        df_data = pd.DataFrame(records, columns=col_names)
        df_meta = pd.DataFrame([{"Header_Hex": header_bytes.hex(), "Header_Bytes": len(header_bytes)}])

        # Write to Excel File
        with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
            df_data.to_excel(writer, sheet_name="Data", index=True, index_label="Row")
            df_meta.to_excel(writer, sheet_name="Metadata", index=False)

        messagebox.showinfo(
            "Success",
            f"Successfully exported {len(records)} records!\n\nSaved to:\n{excel_path}"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert .cos file:\n{str(e)}")


def convert_excel_to_cos():
    """Opens dialog to select edited Excel file, converts it, and asks where to save .cos."""
    # 1. Ask user to open edited Excel file
    excel_path = filedialog.askopenfilename(
        title="Select Edited Excel File",
        filetypes=[("Excel Files (*.xlsx)", "*.xlsx"), ("All Files (*.*)", "*.*")]
    )
    if not excel_path:
        return  # User canceled dialog

    # 2. Ask user where to save reconstructed .cos file
    default_cos_name = os.path.splitext(os.path.basename(excel_path))[0] + "_edited.cos"
    cos_path = filedialog.asksaveasfilename(
        title="Save Reconstructed .COS File As",
        initialfile=default_cos_name,
        defaultextension=".cos",
        filetypes=[("COS Files (*.cos)", "*.cos"), ("All Files (*.*)", "*.*")]
    )
    if not cos_path:
        return  # User canceled dialog

    # 3. Process Excel Data back to Binary .cos Structure
    try:
        df_data = pd.read_excel(excel_path, sheet_name="Data")
        df_meta = pd.read_excel(excel_path, sheet_name="Metadata")

        # Extract Header Bytes
        header_hex = df_meta["Header_Hex"].iloc[0]
        header_bytes = bytes.fromhex(header_hex)

        # Read numerical value columns
        val_cols = [c for c in df_data.columns if c != "Row"][:5]

        # Pack floats into binary format
        body_bytes = bytearray()
        for _, row in df_data[val_cols].iterrows():
            row_vals = [float(row[col]) for col in val_cols]
            body_bytes.extend(struct.pack(FMT, *row_vals))

        # Write output .cos file
        with open(cos_path, "wb") as f:
            f.write(header_bytes)
            f.write(body_bytes)

        messagebox.showinfo(
            "Success",
            f"Successfully rebuilt binary .cos file!\n\nSaved to:\n{cos_path}"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert Excel back to .cos:\n{str(e)}")


def create_gui():
    """Builds the main GUI Window."""
    root = tk.Tk()
    root.title("COS Binary Converter")
    root.geometry("450x230")
    root.resizable(False, False)

    # UI Styling / Labels
    lbl_title = tk.Label(
        root,
        text="COS <-> Excel Converter",
        font=("Segoe UI", 14, "bold")
    )
    lbl_title.pack(pady=(15, 5))

    lbl_sub = tk.Label(
        root,
        text="Select a file to export to Excel or reconstruct a binary .cos file.",
        font=("Segoe UI", 9),
        fg="gray"
    )
    lbl_sub.pack(pady=(0, 15))

    # Action Buttons
    btn_to_excel = tk.Button(
        root,
        text="1. Open .COS File ➔ Save as Excel",
        font=("Segoe UI", 10, "bold"),
        bg="#0284c7",
        fg="white",
        padx=10,
        pady=5,
        command=convert_cos_to_excel
    )
    btn_to_excel.pack(fill="x", padx=40, pady=5)

    btn_to_cos = tk.Button(
        root,
        text="2. Open Edited Excel ➔ Save as .COS",
        font=("Segoe UI", 10, "bold"),
        bg="#16a34a",
        fg="white",
        padx=10,
        pady=5,
        command=convert_excel_to_cos
    )
    btn_to_cos.pack(fill="x", padx=40, pady=5)

    root.mainloop()


if __name__ == "__main__":
    create_gui()