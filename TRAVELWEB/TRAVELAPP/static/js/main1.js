let mic = document.getElementById("mic");
let chatareamain = document.querySelector('.chatarea-main');
let chatareaouter = document.querySelector('.chatarea-outer');

let intro = ["Hello,How can I help you?", "Hello,How may i assist you?"];
let start = ["Hello", "Hi, I am a Robo", "Hello, My name is Chitti"];
let book = ["Fill in all the necessary details in the hotel page <br> Click on Submit "];
let reserve = [ "- It is a 3nights 4days packages<br> - includes Airport/Station Transfers <br> - Daily Free Breakfast <br> - One day Sightseeing Of goa "];
let packages = ["Goa, Sikkim, Pondycherry, Rajasthan, Kerala, Mumbai are the packages available in our Travelar travel agency website"];
let password = ["Step1: Click on forget password <br> Step2: Enter your Email ID <br> Step3: A link would be sent on your given EmailID  Now you can change your password through you email" ];
let ques = ["Please click on the 'Review' option on the Taskbar :)"];
let closing = ['Thanks for visiting us!Hope we would see you soon Have a great day'];
let flight = ["The Airline are <br> Spicejet <br> Vistara <br> Indigo"];
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();

function showusermsg(usermsg){
    let output = '';
    output += `<div class="chatarea-inner user">${usermsg}</div>`;
    chatareaouter.innerHTML += output;
    return chatareaouter;
}

function showchatbotmsg(chatbotmsg){
    let output = '';
    output += `<div class="chatarea-inner chatbot">${chatbotmsg}</div>`;
    chatareaouter.innerHTML += output;
    return chatareaouter;
}

function chatbotvoice(message){
    const speech = new SpeechSynthesisUtterance();
    speech.text = "Sorry I am unaware";

    if(message.includes('hello')){
        let finalresult = intro[Math.floor(Math.random() * intro.length)];
        speech.text = finalresult;
    }
    if(message.includes('book')){
        let finalresult = book[Math.floor(Math.random() * book.length)];
        speech.text = finalresult;
    }
    if(message.includes('Goa')){
        let finalresult = reserve[Math.floor(Math.random() * reserve.length)];
        speech.text = finalresult;
    }
    if(message.includes('packages')){
        let finalresult = packages[Math.floor(Math.random() * packages.length)];
        speech.text = finalresult;
    }
    if(message.includes('password')){
        let finalresult = password[Math.floor(Math.random() * password.length)];
        speech.text = finalresult;
    }
    if(message.includes('review')){
        let finalresult = ques[Math.floor(Math.random() * ques.length)];
        speech.text = finalresult;
    }
    if(message.includes('flights')){
        let finalresult = flight[Math.floor(Math.random() * flight.length)];
        speech.text = finalresult;
    }
    if(message.includes('thank you')){
        let finalresult = closing[Math.floor(Math.random() * closing.length)];
        speech.text = finalresult;
    }
    window.speechSynthesis.speak(speech);
    chatareamain.appendChild(showchatbotmsg(speech.text));
}

recognition.onresult=function(e){
    let resultIndex = e.resultIndex;
    let transcript = e.results[resultIndex][0].transcript;
    chatareamain.appendChild(showusermsg(transcript));
    chatbotvoice(transcript);
    console.log(transcript);
}
recognition.onend=function(){
    mic.style.background="#ff3b3b";
}
mic.addEventListener("click", function(){
    mic.style.background='#39c81f';
    recognition.start();
    console.log("Activated");
})
