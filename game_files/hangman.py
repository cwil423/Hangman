import random
from tkinter import *
from PIL import ImageTk, Image



root = Tk()
root.title('Hangman')

word_list = []

# selects word from list
with open('words.txt', 'r') as f:
    words = f.readlines()
    for word in words:
    	if len(word.strip()) == 5:
    		word_list.append(word.strip())
    		word = random.choice(word_list)


print(word)

#breaks word into list to make it easier to work with
list_word = list(word.strip())
blank_word = []

for letter in list_word:
	blank_word.append(' - ')


images = [
ImageTk.PhotoImage(Image.open('4.jpg')),
ImageTk.PhotoImage(Image.open('5.jpg')),
ImageTk.PhotoImage(Image.open('6.jpg')),
ImageTk.PhotoImage(Image.open('7.jpg')),
ImageTk.PhotoImage(Image.open('8.jpg')),
ImageTk.PhotoImage(Image.open('9.jpg')),
ImageTk.PhotoImage(Image.open('10.jpg')),
]

current_img = images[0]

image_position = 0
guesses = 6
guesses_text = StringVar(root, f'You have {guesses} guesses left.')

blank_word_text = StringVar(root, blank_word)

wrong_letters = []

def submit(contents):
	global guesses
	global image_position
	guess = entry_box.get()
	for letter in range(len(list_word)):
		if guess == list_word[letter]:
			blank_word[letter] = guess
			blank_word_text.set(blank_word)
	if guess not in list_word:
		guesses -= 1
		guesses_text.set(f'You have {guesses} guesses left.')
		image_position += 1
		update_image()
		wrong_letters.append(guess)
		guessed_letters_box.configure(text=wrong_letters)
	win_or_lose()

def win_or_lose():
	if blank_word == list_word:
		guesses_text.set('YOU WIN!!!')
	if guesses == 0:
		if blank_word != list_word:
			guesses_text.set(f'You Lose! \n The anser was {word}.')
		else:
			guesses_text.set('YOU WIN!!!')
		entry_button.configure(state=DISABLED)

def update_image():
	global guesses
	images_box.configure(image=images[image_position])
	images_box.image=images[image_position]



	

		



images_box = Label(root, width=200, height=345, bg='gray', image=current_img)
images_box.grid(column=0, row=0, rowspan=4)	

display_text = Label(root, width=55, height=20, bg='light blue', textvariable=blank_word_text)
display_text.grid(column=1, row=0, sticky=N)

display_guesses = Label(root, width=20, height=2, bg='white', textvariable=guesses_text)
display_guesses.grid(column=1, row=1)

entry_box = Entry(root, width=25, font=100)
entry_box.grid(column=1, row=2)

entry_button = Button(root, width=10, text='Submit', command=lambda: submit(entry_box.get))
entry_button.grid(column=1, row=3)

guessed_letters_box = Label(root, bg='light blue', text=wrong_letters)
guessed_letters_box.grid(column=1, row=0, pady=165)


root.mainloop()