import sys
import tkinter as tk
import os.path
import cv2
import TIMER_Algorithm
from PIL import ImageTk, Image
from VideoModuleBackEnd import FrameAnalyzer
from tkinter import filedialog, messagebox

import threading
import time

w = None


def vp_start_gui():
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1(root)
    root.mainloop()


def create_Toplevel1(root, *args, **kwargs):
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    return w, top


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):

        self.LaneOneVideoPath = None
        self.LaneTwoVideoPath = None
        self.LaneThreeVideoPath = None
        self.LaneFourVideoPath = None
        self.SkipFrameRate = 15

        self.Lane_One_Result = None
        self.Lane_Two_Result = None
        self.Lane_Three_Result = None
        self.Lane_Four_Result = None

        self.Lan_AM_Prev = [False, False, False, False]
        self.Lan_AM = [False, False, False, False]

        self.frame = [None, None, None, None]
        self.count = [0, 0, 0, 0]

        self.priority = None
        self.temp_time_req = None

        def LanOneDisplay():
            frame_count = 0
            VideoSourceLanOne = cv2.VideoCapture(self.LaneOneVideoPath)
            print('Processing Thread One ', self.LaneOneVideoPath)
            while True:
                _, self.frame[0] = VideoSourceLanOne.read()
                if _:
                    if frame_count != self.SkipFrameRate:
                        frame_count = frame_count + 1
                        pass
                    else:
                        if self.count[0] == 0:
                            # self.count[0] = 1
                            self.Lane_One_Result = FrameAnalyzer(self.frame[0])
                            if self.Lane_One_Result[1] == 'Emergency_Vehicles':
                                if self.Lan_AM_Prev[0]:
                                    self.Lan_AM[0] = True
                                else:
                                    self.Lan_AM[0] = False
                                self.Lan_AM_Prev[0] = True
                            else:
                                self.Lan_AM_Prev[0] = False
                                self.Lan_AM[0] = False
                        cv2image = cv2.cvtColor(self.frame[0], cv2.COLOR_BGR2RGBA)
                        imgtk = ImageTk.PhotoImage(image=Image.fromarray(cv2image).resize((550, 300)))
                        self.lblLaneOneMedia.imgtk = imgtk
                        self.lblLaneOneMedia.configure(image=imgtk)
                        frame_count = 0
                        time.sleep(2)
                else:
                    break

        def LanTwoDisplay():
            frame_count = 0
            VideoSourceLanTwo = cv2.VideoCapture(self.LaneTwoVideoPath)
            print('Processing Thread Two ', self.LaneTwoVideoPath)
            while True:
                _, self.frame[1] = VideoSourceLanTwo.read()
                if _:
                    if frame_count != self.SkipFrameRate:
                        frame_count = frame_count + 1
                        pass
                    else:
                        if self.count[1] == 0:
                            # self.count[1] = 1
                            self.Lane_Two_Result = FrameAnalyzer(self.frame[1])
                            if self.Lane_Two_Result[1] == 'Emergency_Vehicles':
                                if self.Lan_AM_Prev[1]:
                                    self.Lan_AM[1] = True
                                else:
                                    self.Lan_AM[1] = False
                                self.Lan_AM_Prev[1] = True
                            else:
                                self.Lan_AM_Prev[1] = False
                                self.Lan_AM[1] = False
                        cv2image = cv2.cvtColor(self.frame[1], cv2.COLOR_BGR2RGBA)
                        imgtk = ImageTk.PhotoImage(image=Image.fromarray(cv2image).resize((550, 300)))
                        self.lblLaneTwoMedia.imgtk = imgtk
                        self.lblLaneTwoMedia.configure(image=imgtk)
                        frame_count = 0
                        time.sleep(2)
                else:
                    break

        def LanThreeDisplay():
            frame_count = 0
            VideoSourceLanThree = cv2.VideoCapture(self.LaneThreeVideoPath)
            print('Processing Thread Three ', self.LaneThreeVideoPath)
            while True:
                _, self.frame[2] = VideoSourceLanThree.read()
                if _:
                    if frame_count != self.SkipFrameRate:
                        frame_count = frame_count + 1
                        pass
                    else:
                        if self.count[2] == 0:
                            # self.count[2] = 1
                            self.Lane_Three_Result = FrameAnalyzer(self.frame[2])
                            if self.Lane_Three_Result[1] == 'Emergency_Vehicles':
                                if self.Lan_AM_Prev[2]:
                                    self.Lan_AM[2] = True
                                else:
                                    self.Lan_AM[2] = False
                                self.Lan_AM_Prev[2] = True
                            else:
                                self.Lan_AM_Prev[2] = False
                                self.Lan_AM[2] = False
                        cv2image = cv2.cvtColor(self.frame[2], cv2.COLOR_BGR2RGBA)
                        imgtk = ImageTk.PhotoImage(image=Image.fromarray(cv2image).resize((550, 300)))
                        self.lblLaneThreeMedia.imgtk = imgtk
                        self.lblLaneThreeMedia.configure(image=imgtk)
                        frame_count = 0
                        time.sleep(2)
                else:
                    break

        def LanFourDisplay():
            frame_count = 0
            VideoSourceLanFour = cv2.VideoCapture(self.LaneFourVideoPath)
            print('Processing Thread Four ', self.LaneFourVideoPath)
            while True:
                _, self.frame[3] = VideoSourceLanFour.read()
                if _:
                    if frame_count != self.SkipFrameRate:
                        frame_count = frame_count + 1
                        pass
                    else:
                        if self.count[3] == 0:
                            # self.count[3] = 1
                            self.Lane_Four_Result = FrameAnalyzer(self.frame[3])
                            if self.Lane_Four_Result[1] == 'Emergency_Vehicles':
                                if self.Lan_AM_Prev[3]:
                                    self.Lan_AM[3] = True
                                else:
                                    self.Lan_AM[3] = False
                                self.Lan_AM_Prev[3] = True
                            else:
                                self.Lan_AM_Prev[3] = False
                                self.Lan_AM[3] = False
                        cv2image = cv2.cvtColor(self.frame[3], cv2.COLOR_BGR2RGBA)
                        imgtk = ImageTk.PhotoImage(image=Image.fromarray(cv2image).resize((550, 300)))
                        self.lblLaneFourMedia.imgtk = imgtk
                        self.lblLaneFourMedia.configure(image=imgtk)
                        frame_count = 0
                        time.sleep(2)
                else:
                    break

        # def LanProcess():
        #     while True:
        #         time.sleep(4)
        #         self.Lane_One_Result = FrameAnalyzer(self.frame[0])
        #         if self.Lane_One_Result[1] == 'Emergency_Vehicles':
        #             self.Lan_AM[0] = True
        #         else:
        #             self.Lan_AM[0] = False
        #         self.Lane_Two_Result = FrameAnalyzer(self.frame[1])
        #         if self.Lane_Two_Result[1] == 'Emergency_Vehicles':
        #             self.Lan_AM[1] = True
        #         else:
        #             self.Lan_AM[1] = False
        #         self.Lane_Three_Result = FrameAnalyzer(self.frame[2])
        #         if self.Lane_Three_Result[1] == 'Emergency_Vehicles':
        #             self.Lan_AM[2] = True
        #         else:
        #             self.Lan_AM[2] = False
        #         self.Lane_Four_Result = FrameAnalyzer(self.frame[3])
        #         if self.Lane_Four_Result[1] == 'Emergency_Vehicles':
        #             self.Lan_AM[3] = True
        #         else:
        #             self.Lan_AM[3] = False

        def Lantimereq():
            self.temp_time_req = TIMER_Algorithm.Calculate_Time_Required(
                self.Lane_One_Result[0][1],
                self.Lane_Two_Result[0][1],
                self.Lane_Three_Result[0][1],
                self.Lane_Four_Result[0][1],
            )

        def SetPrority():
            while True:
                if self.Lane_One_Result is None or self.Lane_Two_Result is None or self.Lane_Three_Result is None or \
                        self.Lane_Four_Result is None:
                    pass
                else:
                    print('\n\nProcessing for timing')

                    time_req = TIMER_Algorithm.Calculate_Time_Required(
                        self.Lane_One_Result[0][1],
                        self.Lane_Two_Result[0][1],
                        self.Lane_Three_Result[0][1],
                        self.Lane_Four_Result[0][1],
                    )

                    priority = {}
                    priority_do_not_set_for = [1, 2, 3, 4]

                    Ambulance_count = 0
                    for i in range(4):
                        if self.Lan_AM[i]:
                            priority_do_not_set_for.remove(i + 1)
                            if i == 0:
                                time_req.pop(0)
                            else:
                                time_req.pop(Ambulance_count - 1)
                            Ambulance_count += 1
                            priority[str(i)] = len(priority) + 1

                    for i in range(len(priority_do_not_set_for)):
                        max_value = max(time_req)
                        index = time_req.index(max_value)
                        lane_no = priority_do_not_set_for[index]
                        time_req.remove(max_value)
                        priority_do_not_set_for.pop(index)
                        priority['' + str(lane_no)] = len(priority) + 1

                    print(priority)
                    priority_function = []
                    for i in range(4):
                        num = int(next(iter(priority))) + i
                        if num > 4:
                            num = num - 4
                        priority_function.append(str(num))
                    print(priority_function)
                    order = 1
                    for k in priority_function:
                        priority[k] = order
                        order += 1

                    self.priority = priority
                    Result_display()
                    for k in priority_function:
                        t = int(self.temp_time_req[int(k) - 1])
                        Go_lane_Counter(k, t, True)
                        # Result_display()
                        for i in range(4):
                            if self.Lan_AM[i]:
                                Go_lane_Counter(str(i + 1), 5, False)
                                # self.Lan_AM[i] = False
                        Result_display()
                        # self.Lan_AM = [False, False, False, False]
                    # time.sleep(0.005)

        def Result_display():
            Lantimereq()
            lane_text = [None, None, None, None]

            Lane_Result = [self.Lane_One_Result[0][1], self.Lane_Two_Result[0][1], self.Lane_Three_Result[0][1],
                           self.Lane_Four_Result[0][1]]
            for i in range(4):
                lane_text[i] = 'Lane : ' + str(i + 1) + ',  P : ' + str(
                    self.priority.get(str(i + 1))) + ', TV : ' + str(
                    Lane_Result[i]) + ', EV : ' + str(int(self.Lan_AM[i])) + ', ETR : ' + str(
                    int(self.temp_time_req[i])) + ' Sec'
            self.lblLaneOneResult.configure(text=lane_text[0])
            self.lblLaneTwoResult.configure(text=lane_text[1])
            self.lblLaneThreeResult.configure(text=lane_text[2])
            self.lblLaneFourResult.configure(text=lane_text[3])

        def Go_lane_Counter(k, t, detect):
            count = 0
            temp = 'Lane: ' + k + ', ETR: '
            if detect:
                while t > 0:
                    if count is 0:
                        for i in range(4):
                            if i + 1 != int(k) and self.Lan_AM[i] is True:
                                count = 1
                                temp = 'EV detected, Lane: ' + k + ', '
                                if t >= 10:
                                    t = 5
                    Result_display()
                    GoLane_text = temp + str(t) + ' Sec'
                    self.golane.configure(text=GoLane_text)
                    t = t - 1
                    time.sleep(1)
            else:

                while t > 0:
                    Result_display()
                    if self.Lan_AM[int(k) - 1]:
                        GoLane_text = 'EV detected, Lane: ' + k
                    else:
                        GoLane_text = 'Lane: ' + k + ', ' + str(t) + ' Sec'
                        t = t-1
                    self.golane.configure(text=GoLane_text)
                    time.sleep(1)

                # while self.Lan_AM[int(k) - 1]:
                #     Result_display()
                #
                #     GoLane_text = 'EV detected, Lane: ' + k
                #     self.golane.configure(text=GoLane_text)
                #     time.sleep(1)
                # while t > 0:
                #     Result_display()
                #     GoLane_text = 'EV passed, Lane: ' + k + ', ETR: ' + str(t) + ' Sec'
                #     self.golane.configure(text=GoLane_text)
                #     t = t - 1
                #     time.sleep(1)

        def selectLaneOneMedia(event):
            # Get File directory from user
            VideoFileName = filedialog.askopenfilename(initialdir="test_data", title="Select file", filetypes=(
                ("mp4 files", "*.mp4"), ("png files", "*.png"), ("all files", "*.*")))
            self.LaneOneVideoPath = VideoFileName
            self.lblLaneOneMedia.configure(text=VideoFileName)

        def selectLaneTwoMedia(event):
            # Get File directory from user
            VideoFileName = filedialog.askopenfilename(initialdir="test_data", title="Select file", filetypes=(
                ("mp4 files", "*.mp4"), ("png files", "*.png"), ("all files", "*.*")))
            self.LaneTwoVideoPath = VideoFileName
            self.lblLaneTwoMedia.configure(text=VideoFileName)

        def selectLaneThreeMedia(event):
            # Get File directory from user
            VideoFileName = filedialog.askopenfilename(initialdir="test_data", title="Select file", filetypes=(
                ("mp4 files", "*.mp4"), ("png files", "*.png"), ("all files", "*.*")))
            self.LaneThreeVideoPath = VideoFileName
            self.lblLaneThreeMedia.configure(text=VideoFileName)

        def selectLaneFourMedia(event):
            # Get File directory from user
            VideoFileName = filedialog.askopenfilename(initialdir="test_data", title="Select file", filetypes=(
                ("mp4 files", "*.mp4"), ("png files", "*.png"), ("all files", "*.*")))
            self.LaneFourVideoPath = VideoFileName
            self.lblLaneFourMedia.configure(text=VideoFileName)

        # def display_output(event):

        def btnCalculateResult(event):
            if self.LaneOneVideoPath is None:
                messagebox.showerror('Lan 1 Missing', 'No Media Found at Lan 1')
                return
            if self.LaneTwoVideoPath is None:
                messagebox.showerror('Lan 2 Missing', 'No Media Found at Lan 2')
                return

            if self.LaneThreeVideoPath is None:
                messagebox.showerror('Lan 3 Missing', 'No Media Found at Lan 3')
                return

            if self.LaneFourVideoPath is None:
                messagebox.showerror('Lan 4 Missing', 'No Media Found at Lan 4')
                return

            threading.Thread(target=LanOneDisplay).start()
            threading.Thread(target=LanTwoDisplay).start()
            threading.Thread(target=LanThreeDisplay).start()
            threading.Thread(target=LanFourDisplay).start()
            # threading.Thread(target=LanProcess).start()
            threading.Thread(target=SetPrority).start()

        def Stop_function(event):
            ans = messagebox.askyesno('Stop Function', 'Do you want to exit?')
            if ans:
                top.destroy()
                top.quit()
            else:
                return

        def exit_top(event):
            top.destroy()
            top.quit()
            # import Smart_Traffic_Control
            # Smart_Traffic_Control.vp_start_gui()

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 14 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font11 = "-family {Sitka Small} -size 19 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font12 = "-family {Times New Roman} -size 36 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        font14 = "-family {Sitka Small} -size 13 -weight normal -slant" \
                 " roman -underline 0 -overstrike 0"

        top.geometry("1571x1010+26+5")
        top.title("New Toplevel")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.state("zoomed")
        top.bind("<Escape>", exit_top)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.003, rely=0.089, height=774, width=1564)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location, "gui_images\\lane_back_2.png")
        self._img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=self._img0)
        self.Label1.configure(text='''Label''')
        self.Label1.configure(width=1564)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.21, rely=0.01, height=73, width=907)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Adaptive traffic management system''')
        self.Label2.configure(width=907)

        self.lblLaneOneMedia = tk.Label(top)
        self.lblLaneOneMedia.place(relx=0.022, rely=0.114, height=296, width=552)

        self.lblLaneOneMedia.configure(activebackground="#f9f9f9")
        self.lblLaneOneMedia.configure(activeforeground="black")
        self.lblLaneOneMedia.configure(background="#ffffff")
        self.lblLaneOneMedia.configure(disabledforeground="#a3a3a3")
        self.lblLaneOneMedia.configure(font=font14)
        self.lblLaneOneMedia.configure(foreground="#000000")
        self.lblLaneOneMedia.configure(highlightbackground="#d9d9d9")
        self.lblLaneOneMedia.configure(highlightcolor="black")
        self.lblLaneOneMedia.configure(relief="groove")
        self.lblLaneOneMedia.configure(text='''Select Lane 1 Media''')
        self.lblLaneOneMedia.configure(width=552)
        self.lblLaneOneMedia.bind('<Button-1>', selectLaneOneMedia)

        self.lblLaneTwoMedia = tk.Label(top)
        self.lblLaneTwoMedia.place(relx=0.595, rely=0.114, height=296, width=552)
        self.lblLaneTwoMedia.configure(activebackground="#f9f9f9")
        self.lblLaneTwoMedia.configure(activeforeground="black")
        self.lblLaneTwoMedia.configure(background="#ffffff")
        self.lblLaneTwoMedia.configure(disabledforeground="#a3a3a3")
        self.lblLaneTwoMedia.configure(font=font14)
        self.lblLaneTwoMedia.configure(foreground="#000000")
        self.lblLaneTwoMedia.configure(highlightbackground="#d9d9d9")
        self.lblLaneTwoMedia.configure(highlightcolor="black")
        self.lblLaneTwoMedia.configure(relief="groove")
        self.lblLaneTwoMedia.configure(text='''Select Lan 2 Media''')
        self.lblLaneTwoMedia.bind('<Button-1>', selectLaneTwoMedia)

        self.lblLaneThreeMedia = tk.Label(top)
        self.lblLaneThreeMedia.place(relx=0.602, rely=0.635, height=296, width=552)
        self.lblLaneThreeMedia.configure(activebackground="#f9f9f9")
        self.lblLaneThreeMedia.configure(activeforeground="black")
        self.lblLaneThreeMedia.configure(background="#ffffff")
        self.lblLaneThreeMedia.configure(disabledforeground="#a3a3a3")
        self.lblLaneThreeMedia.configure(font=font14)
        self.lblLaneThreeMedia.configure(foreground="#000000")
        self.lblLaneThreeMedia.configure(highlightbackground="#d9d9d9")
        self.lblLaneThreeMedia.configure(highlightcolor="black")
        self.lblLaneThreeMedia.configure(relief="groove")
        self.lblLaneThreeMedia.configure(text='''Select Lane 3 Media''')
        self.lblLaneThreeMedia.bind('<Button-1>', selectLaneThreeMedia)

        self.lblLaneFourMedia = tk.Label(top)
        self.lblLaneFourMedia.place(relx=0.019, rely=0.635, height=296, width=552)
        self.lblLaneFourMedia.configure(activebackground="#f9f9f9")
        self.lblLaneFourMedia.configure(activeforeground="black")
        self.lblLaneFourMedia.configure(background="#ffffff")
        self.lblLaneFourMedia.configure(disabledforeground="#a3a3a3")
        self.lblLaneFourMedia.configure(font=font14)
        self.lblLaneFourMedia.configure(foreground="#000000")
        self.lblLaneFourMedia.configure(highlightbackground="#d9d9d9")
        self.lblLaneFourMedia.configure(highlightcolor="black")
        self.lblLaneFourMedia.configure(relief="groove")
        self.lblLaneFourMedia.configure(text='''Select Lan 4 Media''')
        self.lblLaneFourMedia.bind('<Button-1>', selectLaneFourMedia)

        self.lblLaneOneResult = tk.Label(top)
        self.lblLaneOneResult.place(relx=0.025, rely=0.516, height=26, width=542)
        self.lblLaneOneResult.configure(activebackground="#f9f9f9")
        self.lblLaneOneResult.configure(activeforeground="black")
        self.lblLaneOneResult.configure(background="#000000")
        self.lblLaneOneResult.configure(disabledforeground="#a3a3a3")
        self.lblLaneOneResult.configure(font=font10)
        self.lblLaneOneResult.configure(foreground="#ffffff")
        self.lblLaneOneResult.configure(highlightbackground="#d9d9d9")
        self.lblLaneOneResult.configure(highlightcolor="black")
        self.lblLaneOneResult.configure(text='''Lane : 1, P : , TV : , EV : , ETR : Sec''')
        self.lblLaneOneResult.configure(width=542)

        self.lblLaneTwoResult = tk.Label(top)
        self.lblLaneTwoResult.place(relx=0.598, rely=0.516, height=26, width=552)

        self.lblLaneTwoResult.configure(activebackground="#f9f9f9")
        self.lblLaneTwoResult.configure(activeforeground="black")
        self.lblLaneTwoResult.configure(background="#000000")
        self.lblLaneTwoResult.configure(disabledforeground="#a3a3a3")
        self.lblLaneTwoResult.configure(font=font10)
        self.lblLaneTwoResult.configure(foreground="#ffffff")
        self.lblLaneTwoResult.configure(highlightbackground="#d9d9d9")
        self.lblLaneTwoResult.configure(highlightcolor="black")
        self.lblLaneTwoResult.configure(text='''Lane : 2, P : , TV : , EV : , ETR : Sec''')
        self.lblLaneTwoResult.configure(width=552)

        self.lblLaneThreeResult = tk.Label(top)
        self.lblLaneThreeResult.place(relx=0.598, rely=0.57, height=26, width=552)
        self.lblLaneThreeResult.configure(activebackground="#f9f9f9")
        self.lblLaneThreeResult.configure(activeforeground="black")
        self.lblLaneThreeResult.configure(background="#000000")
        self.lblLaneThreeResult.configure(disabledforeground="#a3a3a3")
        self.lblLaneThreeResult.configure(font=font10)
        self.lblLaneThreeResult.configure(foreground="#ffffff")
        self.lblLaneThreeResult.configure(highlightbackground="#d9d9d9")
        self.lblLaneThreeResult.configure(highlightcolor="black")
        self.lblLaneThreeResult.configure(text='''Lane : 3, P : , TV : , EV : , ETR : Sec''')
        self.lblLaneThreeResult.configure(width=542)

        self.lblLaneFourResult = tk.Label(top)
        self.lblLaneFourResult.place(relx=0.025, rely=0.57, height=26, width=542)
        self.lblLaneFourResult.configure(activebackground="#f9f9f9")
        self.lblLaneFourResult.configure(activeforeground="black")
        self.lblLaneFourResult.configure(background="#000000")
        self.lblLaneFourResult.configure(disabledforeground="#a3a3a3")
        self.lblLaneFourResult.configure(font=font10)
        self.lblLaneFourResult.configure(foreground="#ffffff")
        self.lblLaneFourResult.configure(highlightbackground="#d9d9d9")
        self.lblLaneFourResult.configure(highlightcolor="black")
        self.lblLaneFourResult.configure(text='''Lane : 4, P : , TV : , EV : , ETR : Sec''')
        self.lblLaneFourResult.configure(width=552)

        self.btnCalculateTiming = tk.Button(top)
        self.btnCalculateTiming.place(relx=0.423, rely=0.52, height=63, width=206)
        self.btnCalculateTiming.configure(activebackground="#ececec")
        self.btnCalculateTiming.configure(activeforeground="#d7def7")
        self.btnCalculateTiming.configure(background="#a1e9ff")
        self.btnCalculateTiming.configure(disabledforeground="#f9f9f9")
        self.btnCalculateTiming.configure(font=font11)
        self.btnCalculateTiming.configure(foreground="#ffffff")
        self.btnCalculateTiming.configure(highlightbackground="#d9d9d9")
        self.btnCalculateTiming.configure(highlightcolor="black")
        self.btnCalculateTiming.configure(pady="0")
        self.btnCalculateTiming.configure(text='''Calculate''')
        self.btnCalculateTiming.configure(width=206)
        self.btnCalculateTiming.bind('<Button-1>', btnCalculateResult)

        self.golane = tk.Label(top)
        self.golane.place(relx=0.41, rely=0.6, height=60, width=250)
        self.golane.configure(activebackground="#f9f9f9")
        self.golane.configure(activeforeground="white")
        self.golane.configure(background="#000000")
        self.golane.configure(disabledforeground="#a3a3a3")
        self.golane.configure(font=font10)
        self.golane.configure(foreground="#ffffff")
        self.golane.configure(highlightbackground="#d9d9d9")
        self.golane.configure(highlightcolor="black")
        self.golane.configure(text='''Lane: ,ETR: ''')
        self.golane.configure(width=552)
        self.Stop_Button = tk.Button(top)
        self.Stop_Button.place(relx=0.423, rely=0.72, height=63, width=206)
        self.Stop_Button.configure(activebackground="#ececec")
        self.Stop_Button.configure(activeforeground="#d7def7")
        self.Stop_Button.configure(background="#a1e9ff")
        self.Stop_Button.configure(disabledforeground="#a3a3a3")
        self.Stop_Button.configure(font=font11)
        self.Stop_Button.configure(foreground="#ffffff")
        self.Stop_Button.configure(highlightbackground="#d9d9d9")
        self.Stop_Button.configure(highlightcolor="black")
        self.Stop_Button.configure(pady="0")
        self.Stop_Button.configure(text='''Stop''')
        self.Stop_Button.configure(width=206)
        self.Stop_Button.bind('<Button-1>', Stop_function)


if __name__ == '__main__':
    vp_start_gui()
