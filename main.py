import tkinter as tk
from tkinter import messagebox
# window
window  = tk.Tk()
window.geometry("300x250")
#Creating the backround
questions = ["What is the capital of Georgia", "What is 10^4", "Which country is the largest in the world?", "What is starwberry in spanish"]
choices = [["Cleveland","Douglas","Suwanee","Atlanta"],["10,000","10234","1000","4035"],["Germany","Usa","Russia","Brazil"],["fresa","cebolla","mochilla","roja"]]
anwsers = ["Atlanta","10,000","Russia","fresa"]

#varible- keeps track of question
question_index = 0

#score varible
score = 0

# Funtions that handles button press
def buttonController(anwser):
	# Work on next time - SCORING
	global score
	global question_index
	if choices[question_index][anwser] == anwsers[question_index]:
		score += 1
	question_index +=1
	if question_index == 4:
		messagebox.showinfo("Quiz is complete","Your Score: " + str(score))

	#Config - change properties of a component
	question_label.config(text=questions[question_index])
	#button function
	button_label1.config(text=choices[question_index][0])
	button_label2.config(text=choices[question_index][1])
	button_label3.config(text=choices[question_index][2])
	button_label4.config(text=choices[question_index][3])


#Making questions
question_label = tk.Label(window, text=questions[0])
question_label.pack(pady=10)
#Making buttons
button_label1 = tk.Button(window, text=choices[0][0], command=lambda:buttonController(0))
button_label1.pack(pady=6)

button_label2 = tk.Button(window, text=choices[0][1], command=lambda:buttonController(1))
button_label2.pack(pady=6)

button_label3 = tk.Button(window, text=choices[0][2], command=lambda:buttonController(2))
button_label3.pack(pady=6)

button_label4 = tk.Button(window, text=choices[0][3], command=lambda:buttonController(3))
button_label4.pack(pady=6)











#Running the code
window.mainloop()