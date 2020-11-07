import glob
import pandas as pd
import tkinter as tk
import webbrowser


class QuestionRequest():

    def __init__(self):
        self.path = '/Users/makidaisuke/Desktop/my_pands/数学/問題集/'
        self.csv_file = glob.glob(self.path + '*.csv')

        self.img_file = glob.glob(self.path + '*_img')

    def question_select(self):
        subject = ['数Ｉ', '数A', '数Ⅱ', '数B', '数Ⅲ']
        i = 0

        while i < len(subject):
            for q in self.csv_file:
                if q == (self.path + subject[i] + '.csv'):
                    df = pd.read_csv(q)
                    print('kk')

                    for index, v in enumerate(df.Finish):
                        if v == False:
                            return [df.iloc[index], subject[i], q, index]
                            break
                    else:
                        i += 1

    def image_select(self):
        df, subject, file_path, index = self.question_select()
        img = (self.path + subject + '_img/' + df['Title'] + '.png')
        print(df)
        print(img)
        return [df, img, file_path, index]


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        request = QuestionRequest()
        self.df, self.img, self.file_path, self.index = request.image_select()
        self.master.title(self.df['Title'])
        self.master.geometry("1300x1300")
        self.image_canvas()
        self.create_widgets()


    def image_canvas(self):
        self.img = tk.PhotoImage(file=self.img)
        self.dst_image = self.img.subsample(2, 2)
        self.canvas = tk.Canvas(width=1200, height=900)
        self.canvas.place(x=0, y=0)
        self.canvas.create_image(0, 0, image=self.dst_image, anchor=tk.NW)


    def answer(self):
        webbrowser.open(self.df['Answer'])

    def lesson(self):
        webbrowser.open(self.df['Lesson'])

    def correct_or_incorrect(self):
        df = pd.read_csv(self.file_path)
        if df.loc[self.index, 'Finish'] == False:
            df.loc[self.index, 'Finish'] = True
        df.to_csv(self.file_path)


    def create_widgets(self):
        btn1 = tk.Button(self.master, text='解答', width=10, height=5, command=self.answer)
        btn1.place(x=1150, y=100)
        btn2 = tk.Button(self.master, text='授業', width=10, height=5, command=self.lesson)
        btn2.place(x=1150, y=250)
        btn3 = tk.Button(self.master, text='正解', width=10, height=5, command=self.correct_or_incorrect)
        btn3.place(x=1150, y=400)




root = tk.Tk()
app = Application(master=root)
app.mainloop()

