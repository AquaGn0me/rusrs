import Navbar from "../Components/Navbar"
import '../Pages/About.css'

export function About() {
    return (
        <div className="Home">
            <Navbar/>
            <h1>About R-U-SERIO.US</h1>
            
            {/* About section with a blurb */}
            <div className="about-box">
                <p>
                Our project is a tool designed to help individuals better understand tone and sarcasm in written communication. It allows users to input a block of text and then go through it line by line to check for sarcastic remarks. This is especially beneficial for those who may find it challenging to interpret tone in text-based conversations, such as individuals on the autism spectrum or those with similar difficulties in understanding subtle social cues. By providing an accessible and interactive way to analyze tone, our goal is to bridge communication gaps and promote better understanding in online conversations, emails, and other written forms of communication.

With the rise of digital communication, tone is often lost in text, and sarcasm can be particularly difficult to detect. This project seeks to offer a solution, making online interactions more inclusive and helping users feel more confident in interpreting the tone behind the words.
                </p>
            </div>
        </div>
    )
}
