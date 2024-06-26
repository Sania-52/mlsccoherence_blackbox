import pyttsx3
text_speech = pyttsx3.init()

answer = input("What you want to convert to speech?")
text_speech.say(answer)
text_speech.runAndWait()

#Text-to-Speech Conversion

# speech to text and text to speech
import SpeechRecognition as sr
import pyttsx3 
 
r = sr.Recognizer() 

def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command) 
	engine.runAndWait()

#speak

while(1): 

	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level 
			r.adjust_for_ambient_noise(source2, duration=0.2)
			
			#listens for the user's input 
			audio2 = r.listen(source2)
			
			# Using google to recognize audio
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()

			print("Did you say ",MyText)
			SpeakText(MyText)
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occurred")

