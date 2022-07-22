import sys
import vlc
import file_picker
import tkinter as tk


def convert_to_time(time_in_ms: int) -> str:
    """Function converting time in milliseconds to hh::mm::ss format

    :param time_in_ms: time in milliseconds
    :return: Time in hh::mm::ss format
    """
    seconds = time_in_ms//1000
    minutes = seconds//60
    hrs = minutes//60

    if len(str(seconds % 60)) < 2:
        seconds = f'0{seconds % 60}'
    else:
        seconds = str(seconds % 60)

    if len(str(minutes % 60)) < 2:
        minutes = f'0{minutes % 60}'
    else:
        minutes = str(minutes % 60)

    if len(str(hrs % 60)) < 2:
        hrs = f'0{hrs % 60}'
    else:
        hrs = str(hrs % 60)

    displ = f'{hrs}:{minutes}:{seconds}'
    return displ


class VLCBindings:
    def skip_5_sec(self):
        """Skips 5 seconds of the video"""
        self.player.set_time(self.player.get_time() + 5000)

    def rewind_5_sec(self):
        """Rewinds player, 5 seconds back"""
        self.player.set_time(self.player.get_time() - 5000)

    def resume_playback(self):
        """Resumes the playback of the video"""
        self.player.play()

    def pause_playback(self):
        """Pauses the playback of the video"""
        self.player.pause()

    def quit_app(self):
        """Exits the program"""
        sys.exit(0)

    def end_callback(self, event):
        """Quits the program when the playback ends"""
        sys.exit(0)

    def pos_callback(self, event):
        """Updates the GUI during playback"""
        sys.stdout.write('\r%s to (%.2f%%)' % (event.type,
                                               self.player.get_position() * 100))
        self.current_time = self.player.get_time()
        self.duration = self.media.get_duration()
        self.current_time_label['text'] = convert_to_time(self.current_time)
        self.duration_label['text'] = convert_to_time(self.duration)
        self.scale_bar["to"] = (self.duration//1000)
        if not self.scroll:
            self.scale_bar.set(self.current_time//1000)

    def fade_in(self, event):
        """Function that makes the control panel appear."""
        self.root.attributes("-alpha", 1)

    def fade_out(self, event):
        """Function that hides the control panel."""
        if not self.suppress_hide:
            self.root.attributes("-alpha", 0.005)

    def suppress_scroll(self, event):
        """Function that disables resetting of the scale bar to previous position."""
        self.scroll = True

    def move_scroll(self, event):
        """Function that sets the current playback time to the one selected by scale bar."""
        self.player.set_time(self.scale_bar.get() * 1000)
        self.scroll = False

    def suppress_hide_on(self, event):
        """Function that disables auto-hide of the control panel."""
        self.suppress_hide = True
        self.root.attributes("-alpha", 1)

    def suppress_hide_off(self, event):
        """Function that enables auto-hide of the control panel."""
        self.suppress_hide = False
        self.root.attributes("-alpha", 0.005)

    def __init__(self, path_to_video: str):
        """Initalizes a VLC instance and a control panel to interact with playback
        :param path_to_video: path to media
        """
        #Initialize VLC instance, media, and an event manager
        self.instance = vlc.Instance()
        self.media = self.instance.media_new(path_to_video)
        self.player = self.instance.media_player_new()
        self.current_time = ""

        self.player.set_media(self.media)
        self.player.play()

        self.event_manager = self.player.event_manager()
        self.event_manager.event_attach(vlc.EventType(268), self.pos_callback)

        self.duration = self.media.get_duration()

        #Initalize control panel to manage audio/video playback
        self.root = tk.Tk()

        self.scroll = False
        self.suppress_hide = False

        self.root.attributes("-topmost", True)
        self.root.bind("<Enter>", self.fade_in)
        self.root.bind("<Leave>", self.fade_out)
        self.root.bind("<FocusIn>", self.suppress_hide_on)
        self.root.bind("<FocusOut>", self.suppress_hide_off)

        play_image = tk.PhotoImage(file=r"..//gui_images//play_button.png")
        pause_image = tk.PhotoImage(file=r"..//gui_images//pause_button.png")
        ff_image = tk.PhotoImage(file=r"..//gui_images//ff_button.png")
        rev_image = tk.PhotoImage(file=r"..//gui_images//rev_button.png")

        self.play_button = tk.Button(self.root, text="play", command=self.resume_playback, image=play_image)
        self.pause_button = tk.Button(self.root, text="pause", command=self.pause_playback, image=pause_image)
        self.fast_forward = tk.Button(self.root, text="skip", command=self.skip_5_sec, image=ff_image)
        self.rewind = tk.Button(self.root, text="rewind", command=self.rewind_5_sec, image=rev_image)
        self.scale_bar = tk.Scale(self.root, from_=0, to=(self.duration//1000), orient="horizontal", showvalue=False)
        self.scale_bar.bind("<ButtonRelease-1>", self.move_scroll)
        self.scale_bar.bind("<Button-1>", self.suppress_scroll)
        self.current_time_label = tk.Label(text=self.current_time)
        self.duration_label = tk.Label(text=self.duration)

        self.play_button.grid(column=0, row=1)
        self.pause_button.grid(column=1, row=1)
        self.fast_forward.grid(column=2, row=1)
        self.rewind.grid(column=3, row=1)
        self.scale_bar.grid(column=1, columnspan=2, row=0)
        self.current_time_label.grid(column=0, row=0)
        self.duration_label.grid(column=3, row=0)

        tk.mainloop()


if __name__ == "__main__":
    picker = file_picker.FilePicker()
    path = ""
    while not path:
        path = picker.pick_file()
    VLCBindings(path)
