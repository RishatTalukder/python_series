import json
import os
import tkinter as tk
from tkinter import ttk, messagebox

# File path for the local JSON storage
DB_FILE = "notes.json"

class NotesApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("My Notes")
        self.geometry("650x400")
        self.minsize(500, 300)

        # Load notes from JSON or fallback to defaults
        self.notes = self._load_notes()
        self.selected_note = None

        self._configure_styles()
        self._build_ui()
        self._populate_sidebar()

    def _load_notes(self):
        """Loads notes from notes.json if it exists, otherwise creates it with default notes."""
        default_notes = {
            "Python": "Today I learned about Tkinter layouts and JSON persistence.",
            "ML": "Machine learning basics and linear regression.",
            "Ideas": "1. Build a desktop app\n2. Save notes to JSON"
        }
        
        if not os.path.exists(DB_FILE):
            self._write_to_file(default_notes)
            return default_notes

        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            messagebox.showerror("Error", "Could not load notes.json. Using defaults.")
            return default_notes

    def _save_notes_to_db(self):
        """Saves current self.notes dictionary to notes.json."""
        self._write_to_file(self.notes)

    def _write_to_file(self, data):
        """Helper to write data to disk."""
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def _configure_styles(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        self.bg_color = "#f5f5f7"
        self.sidebar_bg = "#e8e8ed"
        
        self.configure(bg=self.bg_color)
        self.style.configure("Sidebar.TFrame", background=self.sidebar_bg)
        self.style.configure("Main.TFrame", background=self.bg_color)
        self.style.configure("TLabel", background=self.bg_color, font=("Segoe UI", 10))
        self.style.configure("Header.TLabel", font=("Segoe UI", 12, "bold"))
        self.style.configure("SidebarHeader.TLabel", background=self.sidebar_bg, font=("Segoe UI", 11, "bold"))

    def _build_ui(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- LEFT SIDEBAR ---
        self.sidebar = ttk.Frame(self, style="Sidebar.TFrame", padding=10)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        lbl_app_title = ttk.Label(self.sidebar, text="My Notes", style="SidebarHeader.TLabel")
        lbl_app_title.pack(anchor="w", pady=(0, 10))

        self.lst_notes = tk.Listbox(
            self.sidebar, 
            bd=0, 
            highlightthickness=0, 
            bg=self.sidebar_bg,
            selectbackground="#007acc", 
            selectforeground="white",
            font=("Segoe UI", 10),
            activestyle="none"
        )
        self.lst_notes.pack(fill="both", expand=True, pady=(0, 10))
        self.lst_notes.bind("<<ListboxSelect>>", self._on_note_select)

        btn_new = ttk.Button(self.sidebar, text="+ New Note", command=self._new_note)
        btn_new.pack(fill="x")

        # --- RIGHT MAIN CONTENT AREA ---
        self.main_area = ttk.Frame(self, style="Main.TFrame", padding=15)
        self.main_area.grid(row=0, column=1, sticky="nsew")
        self.main_area.grid_columnconfigure(0, weight=1)
        self.main_area.grid_rowconfigure(3, weight=1)

        lbl_title = ttk.Label(self.main_area, text="Title:")
        lbl_title.grid(row=0, column=0, sticky="w", pady=(0, 2))

        self.ent_title = ttk.Entry(self.main_area, font=("Segoe UI", 10))
        self.ent_title.grid(row=1, column=0, sticky="ew", pady=(0, 10))

        lbl_content = ttk.Label(self.main_area, text="Content:")
        lbl_content.grid(row=2, column=0, sticky="w", pady=(0, 2))

        self.txt_content = tk.Text(
            self.main_area, 
            font=("Segoe UI", 10), 
            wrap="word", 
            bd=1, 
            relief="solid", 
            highlightthickness=0
        )
        self.txt_content.grid(row=3, column=0, sticky="nsew", pady=(0, 10))

        btn_frame = ttk.Frame(self.main_area, style="Main.TFrame")
        btn_frame.grid(row=4, column=0, sticky="e")

        btn_save = ttk.Button(btn_frame, text="Save", command=self._save_note)
        btn_save.pack(side="left", padx=5)

        btn_delete = ttk.Button(btn_frame, text="Delete", command=self._delete_note)
        btn_delete.pack(side="left")

    def _populate_sidebar(self):
        self.lst_notes.delete(0, tk.END)
        for title in self.notes:
            self.lst_notes.insert(tk.END, f"  • {title}")

    def _on_note_select(self, event):
        selection = self.lst_notes.curselection()
        if not selection:
            return

        index = selection[0]
        title = list(self.notes.keys())[index]
        self.selected_note = title

        self.ent_title.delete(0, tk.END)
        self.ent_title.insert(0, title)

        self.txt_content.delete("1.0", tk.END)
        self.txt_content.insert("1.0", self.notes[title])

    def _new_note(self):
        self.lst_notes.selection_clear(0, tk.END)
        self.selected_note = None
        self.ent_title.delete(0, tk.END)
        self.txt_content.delete("1.0", tk.END)
        self.ent_title.focus_set()

    def _save_note(self):
        title = self.ent_title.get().strip()
        content = self.txt_content.get("1.0", tk.END).strip()

        if not title:
            messagebox.showwarning("Warning", "Title cannot be empty.")
            return

        # If renaming an existing note, remove old key
        if self.selected_note and self.selected_note != title:
            del self.notes[self.selected_note]

        self.notes[title] = content
        self.selected_note = title
        
        # Save changes to JSON file
        self._save_notes_to_db()
        
        self._populate_sidebar()

        # Reselect active note in sidebar
        titles = list(self.notes.keys())
        idx = titles.index(title)
        self.lst_notes.selection_set(idx)

    def _delete_note(self):
        if not self.selected_note:
            self._new_note()
            return

        del self.notes[self.selected_note]
        
        # Save changes to JSON file
        self._save_notes_to_db()
        
        self._populate_sidebar()
        self._new_note()

if __name__ == "__main__":
    app = NotesApp()
    app.mainloop()