import React, { useContext, useEffect, useState } from 'react';
import Message from './Message';
import { ChatContext } from '../context/ChatContext';
import { doc, onSnapshot } from 'firebase/firestore';
import { db } from '../firebase';

const Messages = () => {
    const [messages, setMessages] = useState([]); // Initialize as an empty array
    const { data } = useContext(ChatContext);

    useEffect(() => {
        
        if (!data?.chatId) return;

        const unsub = onSnapshot(doc(db, "chats", data.chatId), (doc) => {
            if (doc.exists()) {
                setMessages(doc.data().messages || []); // Ensure messages is always an array
            } else {
                setMessages([]); // Fallback if the document doesn't exist
            }
        });

        return () => {
            unsub();
        };
    }, [data?.chatId]); // Safely access `data.chatId`

    return (
        <div className="messages">
            {messages.map((m) => (
                <Message message={m} key={m.id} />
            ))}
        </div>
    );
};

export default Messages;
