import cv2
from deepface import DeepFace

# Create a video capture object
cap = cv2.VideoCapture(0)

# Load the pre-trained emotion detection model
model = DeepFace.build_model('Emotion')

# Define a dictionary of emotions and their corresponding colors for visualization
EMOTION_COLORS = {
    'angry': (0, 0, 255),
    'disgust': (0, 255, 0),
    'fear': (255, 0, 0),
    'happy': (255, 255, 0),
    'sad': (0, 255, 255),
    'surprise': (255, 0, 255),
    'neutral': (128, 128, 128)
}

# Loop over frames from the video stream
while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = cv2.CascadeClassifier('eyes\haarcascade_frontalface_default.xml').detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    # Loop over the detected faces
    for (x, y, w, h) in faces:
        # Extract the face ROI
        face_roi = frame[y:y+h, x:x+w]

        # Preprocess the face ROI for emotion detection
        face = cv2.resize(face_roi, (48, 48))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        face = face.astype('float') / 255.0
        face = face.reshape((1, 48, 48, 1))

        # Make a prediction on the face ROI using the emotion detection model
        emotion_preds = model.predict(face)[0]

        # Get the label with the highest probability
        emotion_label = DeepFace.find_apparent_emotion(emotion_preds, threshold=0.5)

        # Draw a rectangle around the face ROI and label it with the predicted emotion
        cv2.rectangle(frame, (x, y), (x+w, y+h), EMOTION_COLORS[emotion_label], 2)
        cv2.putText(frame, emotion_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, EMOTION_COLORS[emotion_label], 2)

    # Show the output frame
    cv2.imshow('Face Emotion Detection', frame)

    # Check for the 'q' key to exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
