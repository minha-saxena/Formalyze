import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

// Firebase configuration object (your credentials)
const firebaseConfig = {
  apiKey: "AIzaSyCDXZnK3KrFp3UcqznsenkdjzXp34pCP_w",
  authDomain: "chat-app-4bce8.firebaseapp.com",
  projectId: "chat-app-4bce8",
  storageBucket: "chat-app-4bce8.firebasestorage.app",
  messagingSenderId: "87460476412",
  appId: "1:87460476412:web:5040bc03bbcb8df608ae79",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firebase Authentication and Firestore
export const auth = getAuth(app);  // Use the `app` instance here for proper initialization
export const db = getFirestore(app); // If you're using Firestore, initialize it with `app` too

export default app; // Export app if needed in other parts of the app
