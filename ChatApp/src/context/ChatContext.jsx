import { createContext, useContext, useReducer } from "react";
import { AuthContext } from "./AuthContext";
import { Navigate } from "react-router-dom"; // Import Navigate for redirection

export const ChatContext = createContext();

export const ChatContextProvider = ({ children }) => {
  const { currentUser } =useContext(AuthContext);

  // If no user is logged in, redirect to the register page
  

  const INITIAL_STATE = {
    chatId: "null",
    user: {},
  };

  const chatReducer = (state, action) => {
    switch (action.type) {
      case "CHANGE_USER":
        return {
          user: action.payload,
          chatId:
            currentUser.uid > action.payload.uid
              ? currentUser.uid + action.payload.uid
              : action.payload.uid + currentUser.uid,
        };
      default:
        return state;
    }
  };

  const [state, dispatch] = useReducer(chatReducer, INITIAL_STATE);

  return (
    <ChatContext.Provider value={{ data: state, dispatch }}>
      {children}
    </ChatContext.Provider>
  );
};
