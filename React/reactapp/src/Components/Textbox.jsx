import { useState } from "react"
//import './App.css'


export function Textbox() {

    const [text, setText] = useState("")

    return(
        <div className="Textbox">
            {/* input is a tag for created a text box*/}
            <input onChange={(e) => setText(e.target.value)}></input>
            <p>{text}</p>
        </div>
    )
}