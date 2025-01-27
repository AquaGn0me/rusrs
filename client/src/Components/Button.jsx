import { useState, useEffect } from "react"
import './Button.css'



export function Button({color}) {

    const [count, setCount] = useState(0)
    

    // when count changes, do whats inside useEffect
    useEffect(() => {
        console.log("count 1 has changed")

    }, [count])

    useEffect(() => {
        console.log("page has just been rendered")
    }, [])


    return (
        <>
            <button onClick={() => setCount(count + 1)} style={{backgroundColor: color}}>
                <p>Check Sarcasm {count}</p>
            </button>
            
        </>
    )
}