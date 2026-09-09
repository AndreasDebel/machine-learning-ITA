"""Tkinter front-end for the primality helpers."""

import tkinter as tk
from tkinter import ttk

from python_project.prime.core import is_prime, next_prime, prev_prime

PRIME_FG = "#1a7f37"
NOT_PRIME_FG = "#b3261e"
ERROR_FG = "#9a6700"
MUTED_FG = "#57606a"


class PrimeApp(ttk.Frame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master, padding=20)
        self.entry_var = tk.StringVar()
        self.prev_var = tk.StringVar(value="\u2014")
        self.next_var = tk.StringVar(value="\u2014")
        self._build()

    def _build(self) -> None:
        self.columnconfigure(1, weight=1)

        ttk.Label(self, text="Number:").grid(row=0, column=0, sticky="w")
        entry = ttk.Entry(self, textvariable=self.entry_var, width=18, justify="right")
        entry.grid(row=0, column=1, sticky="ew", padx=(8, 8))
        entry.focus_set()
        ttk.Button(self, text="Check", command=self.check).grid(row=0, column=2)

        self.verdict = ttk.Label(
            self, text="Enter a whole number.", font=("Segoe UI", 13, "bold"),
            foreground=MUTED_FG, anchor="center",
        )
        self.verdict.grid(row=1, column=0, columnspan=3, pady=(18, 14))

        ttk.Separator(self).grid(row=2, column=0, columnspan=3, sticky="ew")

        ttk.Label(self, text="Previous prime", foreground=MUTED_FG).grid(
            row=3, column=0, columnspan=2, sticky="w", pady=(12, 0)
        )
        ttk.Label(self, textvariable=self.prev_var, font=("Segoe UI", 10, "bold")).grid(
            row=3, column=2, sticky="e", pady=(12, 0)
        )

        ttk.Label(self, text="Next prime", foreground=MUTED_FG).grid(
            row=4, column=0, columnspan=2, sticky="w", pady=(4, 0)
        )
        ttk.Label(self, textvariable=self.next_var, font=("Segoe UI", 10, "bold")).grid(
            row=4, column=2, sticky="e", pady=(4, 0)
        )

        # Enter anywhere in the window triggers a check.
        self.winfo_toplevel().bind("<Return>", lambda _event: self.check())

    def _show(self, text: str, colour: str) -> None:
        self.verdict.configure(text=text, foreground=colour)

    def check(self) -> None:
        raw = self.entry_var.get().strip().replace("_", "")
        try:
            n = int(raw)
        except ValueError:
            self._show(
                "Not a whole number." if raw else "Enter a number first.", ERROR_FG
            )
            self.prev_var.set("\u2014")
            self.next_var.set("\u2014")
            return

        if is_prime(n):
            self._show(f"{n:,} is prime", PRIME_FG)
        else:
            self._show(f"{n:,} is not prime", NOT_PRIME_FG)

        below = prev_prime(n)
        self.prev_var.set("none" if below is None else f"{below:,}")
        self.next_var.set(f"{next_prime(n):,}")


def main() -> None:
    root = tk.Tk()
    root.title("Prime Checker")
    root.minsize(340, 220)
    root.resizable(False, False)
    PrimeApp(root).pack(fill="both", expand=True)
    root.mainloop()


if __name__ == "__main__":
    main()
