import React, { useState } from 'react';
import './App.css';

function App() {
const [inputText, setInputText] = useState('');
const [sentences, setSentences] = useState([]);
const [hoveredSentenceIndex, setHoveredSentenceIndex] = useState(null);
const [popupPosition, setPopupPosition] = useState({ top: 0, left: 0 });

const handleInputChange = (event) => {
setInputText(event.target.value);
};

const handleButtonClick = () => {
const sentencesArray = inputText.split('.').filter(sentence => sentence.trim() !== '').map(sentence => sentence.trim() + '.');
setSentences(sentencesArray);
};

const handleMouseEnter = (event, index) => {
const rect = event.target.getBoundingClientRect();
setPopupPosition({ top: rect.bottom + window.scrollY, left: rect.left + window.scrollX });
setHoveredSentenceIndex(index);
};

const handleMouseLeave = () => {
setHoveredSentenceIndex(null);
};

return (
<div className="App">
<textarea
value={inputText}
onChange={handleInputChange}
placeholder="Enter your text here"
/>
<button onClick={handleButtonClick}>Display Paragraph</button>
<div className="paragraph">
{sentences.map((sentence, index) => (
<span
key={index}
className="sentence"
onMouseEnter={(event) => handleMouseEnter(event, index)}
onMouseLeave={handleMouseLeave}
>
{sentence}
</span>
))}
</div>
{hoveredSentenceIndex !== null && (
<div className="popup-box" style={{ top: popupPosition.top, left: popupPosition.left }}>
<p>{sentences[hoveredSentenceIndex]}</p>
</div>
)}
</div>
);
}

export default App;
