import { doc, onSnapshot } from "firebase/firestore";
import React, { useContext, useEffect, useState } from "react";
import { AuthContext } from "../context/AuthContext";
import { ChatContext } from "../context/ChatContext";
import { db } from "../firebase";

const Chats = () => {
    const [chats, setChats] = useState(null);

    const { currentUser } = useContext(AuthContext);
    const chatContext = useContext(ChatContext);

    if (!chatContext) {
        console.error("ChatContext is not available. Ensure ChatContextProvider is correctly wrapping components.");
        return null;
    }

    const { dispatch } = chatContext;

    useEffect(() => {
        if (!currentUser?.uid) {
            console.warn("currentUser is not available yet.");
            return;
        }

        const getChats = () => {
            const unsub = onSnapshot(doc(db, "userChats", currentUser.uid), (doc) => {
                setChats(doc.data());
            });
            return () => unsub();
        };

        currentUser.uid && getChats();
    }, [currentUser?.uid]);

    const handleSelect = (u) => {
        if (!dispatch) {
            console.error("Dispatch function is not available in ChatContext.");
            return;
        }
        dispatch({ type: "CHANGE_USER", payload:u });
    };

    return (
        <div className="chats">
            {chats &&
                Object.entries(chats)?.sort((a, b) => b[1].date - a[1].date).map((chat) => (
                        <div
                            className="userChat"
                            key={chat[0]}
                            onClick={() => handleSelect(chat[1].userInfo)}
                        >
                            <img
                                src="https://imgs.search.brave.com/x_rFDF8ZfdPz_ICvGjGYjzQkixSDbAaqZRn5_AQYR00/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy9i/L2I2L0ltYWdlX2Ny/ZWF0ZWRfd2l0aF9h/X21vYmlsZV9waG9u/ZS5wbmc"
                                alt=""
                            />
                            <div className="userChatInfo">
                                <span>{chat[1].userInfo.displayName}</span>
                                <p>{chat[1].lastMessage?.text}</p>
                            </div>
                        </div>
                    ))}
        </div>
    );
};

export default Chats;
