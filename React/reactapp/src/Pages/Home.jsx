import { Button } from "../Components/Button"
import { Textbox } from "../Components/Textbox"
import Navbar from "../Components/Navbar"
import './Home.css'

export function Home() {

    return (
        <div className="Home">
            <Navbar/>
            <div>
                <h1>This is the home page</h1>
            </div>
        </div>
    )
}