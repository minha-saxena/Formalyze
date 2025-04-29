import React, { useContext, useEffect, useRef } from 'react'
import { AuthContext } from '../context/AuthContext'
import { ChatContext } from '../context/ChatContext'

const Message = ({message}) => {
    const {currentUser} = useContext(AuthContext)
    const {data} = useContext(ChatContext)

    const ref = useRef();

    useEffect(()=>{
        ref.current?.scrollIntoView({behavious:"smooth"});
    },[message]);
    return(
        <div ref={ref} 
        className={`message ${message.senderId === currentUser.uid &&"owner"}`}
        >
            <div className="messageInfo">
            <img src={
                message.senderId === currentUser.uid ? "https://imgs.search.brave.com/pQgtjoKpKC_KiS_xOcYgpAiCX2qL-283UjaC6l-x3zo/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzA3LzA4LzQ3Lzc1/LzM2MF9GXzcwODQ3/NzUwOF9ETmt6Uklz/TkZnaWJnQ0o2S29U/Z0pqalJaTkpENG1i/NC5qcGc"  :  "https://imgs.search.brave.com/x_rFDF8ZfdPz_ICvGjGYjzQkixSDbAaqZRn5_AQYR00/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy9i/L2I2L0ltYWdlX2Ny/ZWF0ZWRfd2l0aF9h/X21vYmlsZV9waG9u/ZS5wbmc" 
            } alt="" />
                <span>just now</span>
            </div>

            <div className="messageContent">
                <p>{message.text}</p>
                
            </div>
            
        </div>
    )
}

export default Message