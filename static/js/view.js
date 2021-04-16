/// HIIT Timer Views and DOM Event Listeners ///
function showTimerHome() {
    const homeTimer = document.createElement("div");
    // homeTimer.classList.add("row");
    homeTimer.innerHTML = `

                            <div class="form-goup"  method="post">
                                  
                                       
                                        <div class="input-group row col-md-8 offset-md-2 mx-auto">
                                            <label class="input-group-text col-4 col-sm-2 col-form-label bg-transparent text-black" for="exercise">EXERCISE</label>
                                            <input class="form-control col-4 col-sm-2 bg-transparent text-black " type="number" name="exercise" id="exercise" value="10"/>
                                            <span class="input-group-text col-4 col-sm-2 bg-transparent text-black"><small>SECONDS</small></span>
                                        </div>
                                        
                                        <div class="input-group row col-md-8 offset-md-2 mx-auto">
                                            <label class="input-group-text col-4 col-sm-2 col-form-label bg-transparent text-black" for="rest">REST</label>
                                            <input class="form-control col-4 col-sm-2bg-transparent text-black" type="number" name="rest" id="rest" value="5"/>
                                            <span class="input-group-text col-4 col-sm-2 bg-transparent text-black"><small>SECONDS</small></span>
                                        </div>
                                        <div class="input-group row col-md-8 offset-md-2 mx-auto">
                                            <label class="input-group-text col-4 col-sm-2 col-form-label bg-transparent text-black" for="sets">SETS</label>
                                            <input class="form-control col-4 col-sm-2 bg-transparent text-black" type="number" name="sets" id="sets" value="1"/>
                                            <span class="input-group-text col-4 col-sm-2 bg-transparent text-black"><small>SETS</small></span>
                                        </div>    
                                   
                                        <a class="btn btn-primary btn-customized" role="button" type="submit" id="startBtn"><span class="tes2">START!</span></a>
                                  
                               
                            </div>`
    homeView.append(homeTimer);
    const submitBtn = document.querySelector("#startBtn");
    submitBtn.addEventListener("click", handleClickStart);
}

function showTimerExercise() {
    const exerciseTimer = document.createElement("div");
    exerciseTimer.classList.add("container-fluid", "main", "exercise-color");

    exerciseTimer.innerHTML = ` <p class="btn btn-outline-light col-2 col-md-1 m-3 fullscreen"><i class="fas fa-expand-arrows-alt fa-2x"></i></p>
                                <h2 class="display-1 text-center text-light mb-5 pb-5">Exercise</h2>
                                <h1 class="display-1 timer text-light mb-5" id="timer">${ exercise } </h1>
                                <h5 class=" text-center text-light my-5 py-5 " id="set">Sets left: ${sets} </h5>
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
        timerCompleted = true;
  
        abort = true;
        sets = 0;
     
    });
}

function showTimerRest() {
    const exerciseTimer = document.createElement("div");
    exerciseTimer.classList.add("container-fluid",  "main", "rest-color");

    exerciseTimer.innerHTML = ` <p class="btn btn-outline-light col-2 col-md-1 m-2 fullscreen"><i class="fas fa-expand-arrows-alt fa-2x"></i></p> 
                                <h2 class="display-1 text-center text-light mb-5 pb-5">Rest</h2>
                                <span class="display-1 timer text-light my-5" id="timer">${ rest } </span>
                                <h5 class="text-center text-light my-5 py-5" id="set"> Sets left: ${sets} </h5>
                                <progress max="${ rest}" value="${rest}" class="progress progress--set" id="progressBar"></progress>
                                <p id="resetBtn" class="btn btn-outline-light col-2 col-md-1 m-3">RESET</p>`
    exerciseView.append(exerciseTimer);
    const fullscreenBtn = document.querySelector(".fullscreen");
    fullscreenBtn.addEventListener("click", () => {
        toggleFullScreen();
    });
    const resetBtn = document.querySelector("#resetBtn");
    resetBtn.addEventListener("click", () => {
        timerCompleted = true;
  
        abort = true;
        sets = 0;
    });
}

function showTimerComplete(totalSets) {
    const completeTimer = document.createElement("div");
    completeTimer.classList.add("card", "pt-4", "col-md-8", "offset-md-2");
    completeTimer.style.backgroundColor = "black";
    completeTimer.innerHTML = ` <h2 class="text-center p-2 tes2">Congratulations</h2>
                                <span class="tes2 text-white">You've completed ${ totalSets} sets.</span> `
    completeView.append(completeTimer);
}


function changeVisibility(element) {
    element.classList.toggle("d-none");
    
  }


                                