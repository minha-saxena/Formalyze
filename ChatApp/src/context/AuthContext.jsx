import { onAuthStateChanged } from "firebase/auth";
import { createContext, useEffect, useState } from "react";
import { auth } from "../firebase"; // Make sure you have initialized Firebase correctly

export const AuthContext = createContext();

export const AuthContextProvider = ({ children }) => {
  const [currentUser, setCurrentUser] = useState(null);
  const [loading, setLoading] = useState(true); // Add loading state

  useEffect(() => {
    const unsub = onAuthStateChanged(auth, (user) => {
      setCurrentUser(user);
      setLoading(false); // Set loading to false after user authentication is checked
    });

    return () => unsub(); // Ensure proper cleanup when component unmounts
  }, []);

  // While loading the authentication status, show a loading spinner or message
  if (loading) {
    return <div>Loading...</div>; // Or replace with a loading spinner or component
  }

  return (
    <AuthContext.Provider value={{ currentUser }}>
      {children}
    </AuthContext.Provider>
  );
};
