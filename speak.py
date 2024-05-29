import speech_recognition as sr

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Chuẩn bị microphone...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Microphone đã sẵn sàng, bạn có thể bắt đầu nói.")
        audio = recognizer.listen(source)

    try:
        print("Đang nhận diện giọng nói...")
        transcription = recognizer.recognize_google(audio, language='vi-VN')
        print(f"Bạn đã nói: {transcription}")
        return transcription
    except sr.RequestError:
        print("Không thể kết nối với dịch vụ nhận diện giọng nói. Vui lòng kiểm tra kết nối internet của bạn.")
        return None
    except sr.UnknownValueError:
        print("Không hiểu được giọng nói. Vui lòng thử lại.")
        return None

# Kiểm tra hàm
if __name__ == "__main__":
    while True:
        result = recognize_speech_from_mic()
        if result:
            print(f"Phát hiện giọng nói: {result}")
        else:
            print("Không nhận diện được giọng nói.")
        cont = input("Bạn có muốn tiếp tục không? (y/n): ")
        if cont.lower() != 'y':
            break
