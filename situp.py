# import cv2
#
# cap = cv2.VideoCapture(1)
# while True:
#     scc, frame = cap.read()
#     cv2.imshow("frame", frame)
#     if cv2.waitKey(12) == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

import speech_recognition as sr
def record_voice():
	microphone = sr.Recognizer()

	with sr.Microphone() as live_phone:
		microphone.adjust_for_ambient_noise(live_phone)

		print("I'm trying to hear you: ")
		audio = microphone.listen(live_phone)
		try:
			phrase = microphone.recognize_google(audio, language='en')
			return phrase
		except sr.UnkownValueError:
			return "I didn't understand what you said"

if __name__ == '__main__':
	phrase = record_voice()

	with open('you_said_this.txt','w') as file:
		file.write(phrase)

	print('the last sentence you spoke was saved in you_said_this.txt')