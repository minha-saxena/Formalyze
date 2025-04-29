# Formalyze
Formalyze is a chat application that integrates Firebase for real-time messaging and user authentication, along with an LSTM model for detecting informal messages in professional conversations. It promotes professional communication by analyzing and classifying messages based on their tone and language.

## 🧠 Overview
Formalyze is an AI-driven chat application built with Firebase for real-time database management and user authentication. It uses an LSTM model to detect informal language in messages, ensuring that communication remains professional and courteous.

## ✨ Features

-Real-time Chat: Firebase’s real-time database enables instant messaging and updates.

-LSTM Model: Detects informal language in chats and encourages professional communication.

-High Accuracy:

Accuracy: 96.71%

Precision: 97%

Recall: 96%

User Authentication: Uses Firebase Authentication to securely manage user logins and registrations.

Message Moderation: Flags informal language in messages to maintain professionalism.

🛠️ Tech Stack

Frontend: React.js, Tailwind CSS

Backend: Firebase (Real-time Database, Authentication)

AI/Model: LSTM (Long Short-Term Memory) for language classification

Libraries/Frameworks: Firebase SDK, TensorFlow, Scikit-learn

🚀 How to Use

1. Clone the Repository
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/YOUR_USERNAME/Formalyze.git
cd Formalyze
2. Install the Required Packages
Install the necessary dependencies for the frontend:

bash
Copy code
# For frontend
cd frontend
npm install
3. Set up Firebase
Go to the Firebase Console and create a new Firebase project.

Enable Firebase Authentication and Firebase Realtime Database in the console.

Obtain your Firebase credentials (API key, project ID, etc.) and configure them in your project.

4. Run the Application
Start the Frontend:
Navigate to the frontend folder and run the following command:

bash
Copy code
cd frontend
npm start
This will start the React development server, allowing you to use the chat application locally with Firebase as the backend.

5. User Authentication
Login: Use Firebase Authentication to log in with your email and password.

Registration: New users can sign up using the registration option, which stores their credentials securely in Firebase.

6. Real-Time Messaging
Start chatting in real-time once logged in. The system will automatically flag informal language based on the LSTM model, helping maintain professional communication.

🔮 Future Improvements

Integrate voice recognition for analyzing voice-based communication.

Expand the LSTM model to detect different types of informal language (e.g., slang, abbreviations).

Implement additional notification features to alert users of informal language.

Create a mobile version of the application using React Native.
