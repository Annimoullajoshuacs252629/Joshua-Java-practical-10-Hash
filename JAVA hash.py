import tkinter as tk
from tkinter import messagebox


class BasicHashTableGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Basic Hash Table")
        self.root.geometry("400x580")
        self.root.resizable(False, False)

        self.table_size = 10
        self.hash_table = [None] * self.table_size

        # Title
        self.title_label = tk.Label(
            root, text="BASIC HASH TABLE", font=("Arial", 16, "bold")
        )
        self.title_label.pack(pady=10)

        # Table Size Frame
        size_frame = tk.Frame(root)
        size_frame.pack(pady=5)

        tk.Label(
            size_frame, text="Table Size:", font=("Arial", 10, "bold")
        ).pack(side=tk.LEFT, padx=5)

        self.size_entry = tk.Entry(
            size_frame, width=15, justify="center", font=("Arial", 10)
        )
        self.size_entry.insert(0, "10")
        self.size_entry.pack(side=tk.LEFT, padx=5)

        self.create_btn = tk.Button(
            size_frame,
            text="Create Table",
            width=12,
            command=self.create_table,
        )
        self.create_btn.pack(side=tk.LEFT, padx=5)

        # Enter Key Frame
        key_frame = tk.Frame(root)
        key_frame.pack(pady=5)

        tk.Label(
            key_frame, text="Enter Key:", font=("Arial", 10, "bold")
        ).pack(side=tk.LEFT, padx=5)

        self.key_entry = tk.Entry(
            key_frame, width=15, justify="center", font=("Arial", 10)
        )
        self.key_entry.pack(side=tk.LEFT, padx=5)

        # Operations Buttons Frame (Insert, Delete, Traverse)
        ops_frame = tk.Frame(root)
        ops_frame.pack(pady=5)

        tk.Button(
            ops_frame, text="Insert", width=10, command=self.insert_key
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            ops_frame, text="Delete", width=10, command=self.delete_key
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            ops_frame, text="Traverse", width=10, command=self.traverse_table
        ).pack(side=tk.LEFT, padx=5)

        # Reset & Clear Frame
        reset_frame = tk.Frame(root)
        reset_frame.pack(pady=5)

        tk.Button(
            reset_frame, text="Reset Table", width=12, command=self.reset_table
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            reset_frame, text="Clear Key", width=12, command=self.clear_key
        ).pack(side=tk.LEFT, padx=5)

        # Hash Function Label
        self.formula_label = tk.Label(
            root,
            text="Hash Function: index = key % table size",
            font=("Arial", 9, "bold"),
        )
        self.formula_label.pack(pady=10)

        # Table Display Container Frame
        self.table_container = tk.Frame(root)
        self.table_container.pack(pady=5)

        # Status Bar Label
        self.status_label = tk.Label(
            root, text="", font=("Arial", 9, "bold"), fg="black"
        )
        self.status_label.pack(side=tk.BOTTOM, pady=10)

        # Initialize the table display
        self.build_table_ui()

    def build_table_ui(self):
        for widget in self.table_container.winfo_children():
            widget.destroy()

        # Headers
        tk.Label(
            self.table_container, text="INDEX", font=("Arial", 10, "bold")
        ).grid(row=0, column=0, padx=10, pady=2)
        tk.Label(
            self.table_container, text="VALUE", font=("Arial", 10, "bold")
        ).grid(row=0, column=1, padx=10, pady=2)

        # Table Rows
        for i in range(self.table_size):
            # Index box
            idx_box = tk.Label(
                self.table_container,
                text=str(i),
                width=15,
                relief="solid",
                bd=1,
                bg="#f0f0f0",
            )
            idx_box.grid(row=i + 1, column=0, padx=5, pady=2)

            # Value box
            val_text = (
                "Empty"
                if self.hash_table[i] is None
                else str(self.hash_table[i])
            )
            val_box = tk.Label(
                self.table_container,
                text=val_text,
                width=15,
                relief="solid",
                bd=1,
                bg="white" if val_text != "Empty" else "#f0f0f0",
            )
            val_box.grid(row=i + 1, column=1, padx=5, pady=2)

    def create_table(self):
        try:
            size = int(self.size_entry.get())
            if size <= 0:
                raise ValueError
            self.table_size = size
            self.hash_table = [None] * self.table_size
            self.build_table_ui()
            self.status_label.config(text=f"Created table of size {size}.")
        except ValueError:
            messagebox.showerror(
                "Error", "Please enter a valid positive integer for size."
            )

    def insert_key(self):
        key_str = self.key_entry.get().strip()
        if not key_str:
            messagebox.showwarning("Input Error", "Please enter a key.")
            return

        try:
            key = int(key_str)
            index = key % self.table_size
            self.hash_table[index] = key
            self.build_table_ui()
            self.status_label.config(
                text=f"{key} inserted at index {index}."
            )
        except ValueError:
            messagebox.showerror("Error", "Key must be an integer.")

    def delete_key(self):
        key_str = self.key_entry.get().strip()
        if not key_str:
            messagebox.showwarning("Input Error", "Please enter a key.")
            return

        try:
            key = int(key_str)
            index = key % self.table_size
            if self.hash_table[index] == key:
                self.hash_table[index] = None
                self.build_table_ui()
                self.status_label.config(
                    text=f"Deleted key {key} from index {index}."
                )
            else:
                self.status_label.config(
                    text=f"Key {key} not found at index {index}."
                )
        except ValueError:
            messagebox.showerror("Error", "Key must be an integer.")

    def traverse_table(self):
        items = [
            f"[{idx}]: {val}"
            for idx, val in enumerate(self.hash_table)
            if val is not None
        ]
        if items:
            self.status_label.config(text="Table Traversal: " + ", ".join(items))
        else:
            self.status_label.config(text="Table is completely empty.")

    def reset_table(self):
        self.hash_table = [None] * self.table_size
        self.build_table_ui()
        self.status_label.config(text="Table reset to empty state.")

    def clear_key(self):
        self.key_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = BasicHashTableGUI(root)
    root.mainloop()