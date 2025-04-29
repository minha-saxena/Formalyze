import React, { useState } from 'react';
import Add from "../img/addAvatar.png";
import { createUserWithEmailAndPassword, updateProfile , onAuthStateChanged} from "firebase/auth";
import {auth, db } from "../firebase";
import { doc, setDoc } from "firebase/firestore"; 
import { useNavigate, Link } from 'react-router-dom';

const Register = () => {

    const [err, setErr] = useState(false);
    const Navigate = useNavigate();

    const handleSubmit = async (e) =>{
        e.preventDefault();
        
        const displayName = e.target[0].value;
        console.log(e);
        const email = e.target[1].value;
        const password = e.target[2].value;
        const file = e.target[3].files[0];

        try{
            //create user
            const res = await createUserWithEmailAndPassword(auth , email,password);
            console.log(res);

            //skip the image task
            await updateProfile(res.user, {
                displayName,
            });

            await setDoc(doc(db,"users",res.user.uid),{
                uid: res.user.uid,
                displayName,
                email
            });
            await setDoc(doc(db,"userChats",res.user.uid),{});

            onAuthStateChanged(auth, (user) => {
                console.log("Updated user:", user); // Confirm displayName is available
            });
    

            Navigate("/");


        }catch(err){
            console.log(err);
            setErr(true);
        }
    
    };


   
    

    return(
        <div className='formContainer'>
            <div className='formWrapper'>
                <span className="logo">Formalyze</span>
                <span className="title">Register</span>
                <form onSubmit={handleSubmit}>
                    <input type="text" placeholder='display name'/>
                    <input type="email" placeholder='email'/>
                    <input type="password" placeholder='password'/>
                    <input style={{display:"none"}} type="file" id='file' />
                    <label htmlFor="file">
                        <img src={Add} alt="" />
                        <span>Add an avatar</span>
                    </label>
                    <button>Sign Up</button>
                    {err && <span>Something went wrong</span>}
                </form>
                <p>Already have an account? <Link to="/login">Login</Link></p>
            </div>
        </div>
    );
};

export default Register;