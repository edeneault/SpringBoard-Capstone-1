/// HIIT Timer Views and DOM Event Listeners ///


// View Function for the timer value input form //
function showTimerHome() {
    const homeTimer = document.createElement("div");

    homeTimer.innerHTML = `<div class="form-goup  pt-5"  method="post">
                                <div class="input-group row col-md-8 offset-md-2 mx-auto">
                                    <label class="input-group-text col-4 col-sm-2 col-form-label bg-timer-form text-black" for="exercise">EXERCISE</label>
                                    <input class="form-control col-4 col-sm-2 bg-timer-form text-black " type="number" name="exercise" id="exercise" value="10"/>
                                    <span class="input-group-text col-4 col-sm-2 bg-timer-form text-black"><small>SECONDS</small></span>
                                </div>
                                
                                <div class="input-group row col-md-8 offset-md-2 mx-auto">
                                    <label class="input-group-text col-4 col-sm-2 col-form-label bg-timer-form text-black" for="rest">REST</label>
                                    <input class="form-control col-4 col-sm-2 bg-timer-form text-black" type="number" name="rest" id="rest" value="5"/>
                                    <span class="input-group-text col-4 col-sm-2 bg-timer-form text-black"><small>SECONDS</small></span>
                                </div>
                                <div class="input-group row col-md-8 offset-md-2 mx-auto">
                                    <label class="input-group-text col-4 col-sm-2 col-form-label bg-timer-form text-black" for="sets">ROUNDS</label>
                                    <input class="form-control col-4 col-sm-2 bg-timer-form text-black" type="number" name="sets" id="sets" value="1"/>
                                    <span class="input-group-text col-4 col-sm-2 bg-timer-form text-black"><small>ROUNDS</small></span>
                                </div>    
                                <div class="row mt-2">
                                    <div class="col col-sm-12 align-self-center text-center mx-auto">
                                        <button class="btn btn-primary btn-customized-1 px-4 py-2 m-2" role="button" type="submit" id="startBtn"><span class="text-white fs-5">START!</span></button>
                                    </div>
                                </div>
                            </div>
                            <div class="image-wrapper pt-4">
                                    <img src="static/images/clipart1066235.png" alt="TIMER_IMAGE">
                            </div>`
                            
    homeView.append(homeTimer);
    const submitBtn = document.querySelector("#startBtn");
    submitBtn.addEventListener("click", handleClickStart);
}

// View Function for exercise time //
function showTimerExercise() {
    const exerciseTimer = document.createElement("div");
    exerciseTimer.classList.add("container-fluid", "main", "exercise-color");   

    exerciseTimer.innerHTML = ` <p id="fullscreen" class="btn btn-outline-light col-4 col-md-2 m-2 fullscreen"><i class="fas fa-expand-arrows-alt fa-2x"></i></p>
                                <h2 class="display-1 text-center text-light mb-5 pb-5">Exercise</h2>
                                <span class="display-1 timer text-light mb-5" id="timer">${ exercise } </span>
                                <h5 class=" text-center text-light my-5 py-5 " id="set">ROUNDS left: ${sets} </h5>
                                <progress max="${ exercise}" value="${exercise}" class="progress progress--rest" id="progressBar"></progress>
                                <p id="resetBtn" class="btn btn-outline-light col-2 col-md-1 m-3">RESET</p>
                                `
    exerciseView.append(exerciseTimer);  
     
    const fullscreenBtn = document.querySelector(".fullscreen"); 
    fullscreenBtn.addEventListener("click", () => {
        toggleFullScreen();
    });
    const resetBtn = document.querySelector("#resetBtn");
    resetBtn.addEventListener("click", () => {
        location.reload()
     
    });
}

// View Function for rest time //

function showTimerRest() {
    const exerciseTimer = document.createElement("div");
    exerciseTimer.classList.add("container-fluid",  "main", "rest-color");

    exerciseTimer.innerHTML = ` <p id="fullscreen1" class="btn btn-outline-light col-4 col-md-2 m-2 fullscreen"><i class="fas fa-expand-arrows-alt fa-2x"></i></p> 
                                <h2 class="display-1 text-center text-light mb-5 pb-5">Rest</h2>
                                <span class="display-1 timer text-light my-5" id="timer">${ rest } </span>
                                <h5 class="text-center text-light my-5 py-5" id="set"> ROUNDS left: ${sets} </h5>
                                <progress max="${ rest}" value="${rest}" class="progress progress--set" id="progressBar"></progress>
                                <p id="resetBtn" class="btn btn-outline-light col-2 col-md-1 m-3">RESET</p>`
    exerciseView.append(exerciseTimer);
    const fullscreenBtn = document.querySelector(".fullscreen");
    fullscreenBtn.addEventListener("click", () => {
        toggleFullScreen();
    });
    const resetBtn = document.querySelector("#resetBtn");
    resetBtn.addEventListener("click", () => {
        location.reload()
    });
}

// View Function for timer completed //
function showTimerComplete(totalSets) {
    const completeTimer = document.createElement("div");
    completeTimer.classList.add("card", "pt-4", "col-md-8", "offset-md-2");
    completeTimer.style.backgroundColor = "black";
    completeTimer.innerHTML = ` <h2 class="text-center p-2 tes2">Congratulations</h2>
                                <span class="tes2 text-white">You've completed ${ totalSets} sets.</span> `
    completeView.append(completeTimer);
}

// Function to change the visibility of various elements //
function changeVisibility(element) {
    element.classList.toggle("d-none");
    
  }


                                