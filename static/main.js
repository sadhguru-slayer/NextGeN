console.log("object")

const social = document.getElementById("social").value
// console.log(social)

const timeElem = document.getElementById("time")

timeElem.addEventListener("change",()=> timeSpend())

// console.log(time)
let a,b
const interestsElem = document.getElementById("interests")
interestsElem.addEventListener("change",() => interestSelected())
function interestSelected() {
    const interests = document.getElementById("interests").value
    
        if (interests == "life")
             b+= 1
        else if (interests == "mus")
        b+= 1
        else if (interests == "dan")
        b+= 1
        else if(interests == "edi")
        b+= 1
        else if(interests == "memes")
        b+= 1
        else
        b = 0
    
        console.log(b)
    }




function timeSpend() {
const time = document.getElementById("time").value

    if (time == "less1")
         a= 5
    else if (time == "1to2")
        a = 4
    else if (time == "3to4")
        a = 3
    else if(time == "5+")
        a = 1
    else
    a = 0

    console.log(a)
}


const quest = document.getElementById("question")
const quest2 = document.getElementById("question2")



let questions = [
    "Q. John describes a situation at his previous job where he had to make a decision to terminate an underperforming employee. He explains the steps he took and the outcomes.",

    "Q. Jane shares an experience where she had to choose between two competing projects and explains her decision-making process.",

    "Q. Sarah discusses her self-awareness in decision-making and her practice of seeking feedback from colleagues to mitigate bias.",

    "Q. Michael shares his strategies for managing stress, including setting clear boundaries between work and personal life.",

    "Q. Jane talks about mediating a disagreement between two team members and how she encouraged open communication to find a solution.",

    "Q. Mark shares a conflict that arose in a cross-functional team and how he facilitated a conversation to address differing opinions.",


    "Q. Can you provide an example of a situation where you had to be particularly empathetic and understanding of someone else's emotions or perspective? How did you approach this, and what was the outcome?",

    "Q. Tell us about a time when you had to manage a team member who was dealing with personal emotional challenges. How did you support them while ensuring the team's goals were met?",

    "Q. Discuss a situation where you needed to provide feedback to a colleague or team member about their performance or behavior. How did you approach this conversation, and how did you consider their emotions?",

    "Q. Share a scenario where you needed to persuade or influence a skeptical or resistant team member to support a new idea or direction. How did you leverage your emotional intelligence to build trust and gain their buy-in?"
]

let num = Math.floor(Number(Math.random()*10))
let num2 = Math.floor(Number(Math.random()*10))
quest.innerHTML = questions[num]
quest2.innerHTML = questions[num2]


let sc = a+b

function score(){
    const s = document.getElementById("score")
    s.innerText = sc
}

