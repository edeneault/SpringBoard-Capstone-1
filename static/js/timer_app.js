/// TIMERS APP ///

// DOM SELECTORS//
const exerciseView = document.querySelector("#timers-exercise");
const completeView = document.querySelector("#timers-complete");
const homeView = document.querySelector("#timers-home");

const timerType = document.querySelector("#timer-type");

const sidebar = document.querySelector(".sidebar");
const overlay = document.querySelector(".overlay");
const tabataNav = document.querySelector("#tabata-timer");
const hiitNav = document.querySelector("#hiit-timer");
const roundNav = document.querySelector("#round-timer");

// const exercise = document.querySelector("#exercise");
// const rest = document.querySelector("#rest")
// const sets = document.querySelector("#sets");

// TIMER FORM TO DOM //
showTimerHome();

// INIT VARIABLES //
let currView = "exercise";
let totalSets = sets.value;
let timerCompleted = false;
let abort = false;


tabataNav.addEventListener("click", (e) => {
    if (timerCompleted === true) {
        completeView.removeChild(completeView.childNodes[0]);
        timerCompleted = false;
        currView = "exercise"; 
    }
    // exerciseView.removeChild(exerciseView.childNodes[0]);
    document.querySelector("#exercise").value = "20";
    document.querySelector("#rest").value = "10";
    document.querySelector("#sets").value = "8";
    // exercise.value = "20";
    // console.log("🚀 ~ file: app.js ~ line 28 ~ tabataNav.addEventListener ~ exercise.value", exercise.value)
    // rest.value = "10";
    // console.log("🚀 ~ file: app.js ~ line 30 ~ tabataNav.addEventListener ~ rest.value", rest.value)
    // sets.value = "8";
    // console.log("🚀 ~ file: app.js ~ line 32 ~ tabataNav.addEventListener ~ sets.value", sets.value)
    timerType.innerText = "TABATA Timer";
    sidebar.classList.remove("active");
    overlay.classList.remove("active");
});

hiitNav.addEventListener("click", (e) => {
    document.querySelector("#exercise").value = "30";
    document.querySelector("#rest").value = "15";
    document.querySelector("#sets").value = "12";
    timerType.innerText = "HIIT Timer";
    sidebar.classList.remove("active");
    overlay.classList.remove("active");
});

roundNav.addEventListener("click", (e) => {
    document.querySelector("#exercise").value = "60";
    document.querySelector("#rest").value = "0";
    document.querySelector("#sets").value = "15";
    timerType.innerText = "Round (EMOM) Timer";
    sidebar.classList.remove("active");
    overlay.classList.remove("active");
});


// Instanciate Sound Objects and Set Volume Property //
const snd = new Audio("static/assets/audio/Boxing_BELL_One_ring.mp3"); // buffers automatically when created
const snd1 = new Audio("static/assets/audio/Boxing_BELL_three_rings.mp3"); // buffers automatically when created
snd.volume = 0.2;
snd1.volume = 0.5;

function myTimer() {
    console.log("insode my Timer");

}

// Click Event Handler //
function handleClickStart(e) {
    e.preventDefault();
    exercise = document.querySelector("#exercise").value;
    rest = document.querySelector("#rest").value;
    sets = document.querySelector("#sets").value;
    // homeView.removeChild(homeView.childNodes[0]);
    console.log(homeView);
    changeVisibility(homeView);
    console.log(timerType);
    changeVisibility(timerType);
    showTimerExercise();
    startTimer();
    snd.play();   
}

// Timer LOGIC //
function startTimer() {
    const timerElement = document.querySelector("#timer");
    const progressBar = document.getElementById("progressBar");
    let timerCounter = progressBar.max;
   
    if (timerCompleted === true) {
        completeView.removeChild(completeView.childNodes[0]);
        timerCompleted = false;
        currView = "exercise"; 
    }

    var interval = setInterval(() => {
        if (timerCounter === 0) {   
            clearInterval(interval);
            try {
                exerciseView.removeChild(exerciseView.childNodes[0]);
            }
            catch (e) { };
            
            if (sets <= 0 && abort === true) {
                clearInterval(interval);
                try {
                    exerciseView.removeChild(exerciseView.childNodes[0]);
                }
                catch (e) { };
                
                snd1.play();  
                timerCompleted = true;
                showTimerHome();  
            }
            else if (sets <= 0) {
               
                snd1.play();  
                showTimerComplete(totalSets);
                changeVisibility(timerType);
                // submitBtn.disabled = false;
                // sets.value = 3;
                timerCompleted = true;
                changeVisibility(homeView);   
                // console.log("🚀 ~ file: app.js ~ line 66 ~ interval ~ showTimerHome(); ", showTimerHome);
            }
            
            else if (currView === "exercise") {
                snd.play();  
                showTimerRest();
                startTimer();
                currView = "rest"
                sets--;
            }
            else if (currView === "rest") {
                snd.play();  
                showTimerExercise();
                startTimer()
                currView = "exercise"
            }  
        }
        timerCounter = timerCounter - 1;
        
        timerElement.innerText = timerCounter + "s";
        progressBar.value = timerCounter;
    }, 1000);

}



