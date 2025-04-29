import { signOut } from 'firebase/auth'
import React, { useContext } from 'react'
import { auth } from '../firebase'
import { AuthContext } from '../context/AuthContext'

const Navbar = () => {
    const {currentUser} = useContext(AuthContext)
    return(
        <div className='navbar'>
            <span className="logo">Formalyze</span>
            <div className="user">
                <img src="https://imgs.search.brave.com/pQgtjoKpKC_KiS_xOcYgpAiCX2qL-283UjaC6l-x3zo/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzA3LzA4LzQ3Lzc1/LzM2MF9GXzcwODQ3/NzUwOF9ETmt6Uklz/TkZnaWJnQ0o2S29U/Z0pqalJaTkpENG1i/NC5qcGc" alt="" />
                <span>{currentUser.displayName}</span>
                <button onClick={()=>signOut(auth)} >Logout</button>
            </div>
        </div>
    )
}

export default Navbar