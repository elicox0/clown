import time
import threading
import tkinter as tk

MAX_ROWS = 5
MAX_COLS = 10

class Stopwatch:
    def __init__(self, frame, label, index) -> None:
        self.is_running = False
        self.start_time = None
        self.elapsed_time = 0
        self.frame = frame
        self.label = label
        self.index = index

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time()
        
class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Outside")
        self.stopwatches = []
        self.next_index = 0
        self.row = 0
        self.column = 1

        frame = tk.Frame(self.root)
        frame.grid(row=0, column=0, padx=30, pady=10)
        tk.Button(
                frame, 
                text="Add Stopwatch", 
                command=self.create_stopwatch
        ).pack()

    def create_stopwatch(self):
        frame = tk.Frame(self.root)
        frame.grid(
                row=self.row, 
                column=self.column, 
                padx=10, 
                pady=10
        )
        label = tk.Label(
            frame,
            text=f"Stopwatch {self.next_index+1}"
        )
        label.pack()
        sw = Stopwatch(frame, label, self.next_index)
        # tk.Label(
        #     frame,
        #     text=sw.dynamiclabel
        # ).pack()
        self.stopwatches.append(sw)
        tk.Button(
            frame, 
            text="Start", 
            command=lambda i=self.next_index: self.start_stopwatch(i)
        ).pack()
        tk.Button(
            frame, 
            text="Stop", 
            command=lambda i=self.next_index: self.stop_stopwatch(i)
        ).pack()
        tk.Button(
            frame, 
            text="Reset", 
            command=lambda i=self.next_index: self.reset_stopwatch(i)
        ).pack()
        # self.update_stopwatches()
        self.next_index += 1
        if self.next_index % MAX_ROWS == 0 and self.next_index > 1:
            self.column += 1
            self.row = 0
        else:
            self.row += 1

    def start_stopwatch(self, index):
        sw = self.stopwatches[index]
        if not sw.is_running:
            sw.is_running = True
            if sw.elapsed_time == 0: 
                sw.start_time = time.time()

    def stop_stopwatch(self, index):
        sw = self.stopwatches[index]
        sw.elapsed_time = time.time() - sw.start_time
        sw.is_running = False

    def reset_stopwatch(self, index):
        self.stopwatches[index].start_time = time.time()

    def _update_stopwatches(self):
        while True:
            for i, stopwatch in enumerate(self.stopwatches):
                if stopwatch.is_running:
                    elapsed_time = time.time() - stopwatch.start_time
                else:
                    elapsed_time = stopwatch.elapsed_time
                # elapsed_time = (time.time() - stopwatch.start_time) if stopwatch.is_running else 0
                # stopwatch.dynamiclabel.set(f"Stopwatch {i+1}: {elapsed_time:.2f} seconds")
                stopwatch.label.config(text=f"Stopwatch {i+1}: {elapsed_time:.2f}")
    def update_stopwatches(self):
        thread = threading.Thread(target=self._update_stopwatches)
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    app.update_stopwatches()
    root.mainloop()

