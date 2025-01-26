import { Button } from "../Components/Button"
import { Textbox } from "../Components/Textbox"
import Navbar from "../Components/Navbar"
import './Home.css'

export function Home() {

    return (
        <div className="Home">
            <Navbar/>
            <div class="main_stack">
                <h1>
                    <form action="/check_sarcasm">
                        <textarea id="text_input" placeholder="Text here"></textarea>
                        <button type='submit'>Check Sarcasm</button>
                    </form>                
                </h1>
            </div>
          </navbar>
      </div>
  )
}