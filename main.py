import tkinter as tk

# window
window  = tk.Tk()
window.geometry("300x250")
#Creating the backround
questions = ["What is the capital of Georgia", "What is 10^4", "Which country is the largest in the world?"]
choices = [["Cleveland","Douglas","Suwanee","Atlanta"],["10,000","10234","1000","4035"],["Germany","Usa","Russia","Brazil"]]
anwsers = ["Atlanta","10,000","Russia"]

#varible- keeps track of question
question_index = 0


# Funtions that handles button press
def buttonController():
	global question_index
	question_index +=1
	#Config - change properties of a component
	question_label.config(text=questions[question_index])

#button function
	button_label1.config(text=choices[question_index])
	button_label2.config(text=choices[question_index])
#Making questions
question_label = tk.Label(window, text=questions[0])
question_label.pack(pady=10)
#Making buttons
button_label1 = tk.Button(window, text=choices[0][0], command=buttonController)
button_label1.pack(pady=6)

button_label2 = tk.Button(window, text=choices[0][1], command=buttonController)
button_label2.pack(pady=6)

button_label3 = tk.Button(window, text=choices[0][2], command=buttonController)
button_label3.pack(pady=6)

button_label4 = tk.Button(window, text=choices[0][3], command=buttonController)
button_label4.pack(pady=6)











#Running the code
window.mainloop()