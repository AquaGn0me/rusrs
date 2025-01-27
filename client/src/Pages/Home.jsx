import { Button } from "../Components/Button"
import { Textbox } from "../Components/Textbox"
import Navbar from "../Components/Navbar"
import './Home.css'

export function Home() {

    return (
        <div className="Home">
            <Navbar/>
            <section class="main_stack">
                <div>
                    <textarea id="text_input" placeholder="Text here" ></textarea>
                    <Button type='submit'>Check Sarcasm</Button>
                </div>

            </section>
        </div>
    )
}