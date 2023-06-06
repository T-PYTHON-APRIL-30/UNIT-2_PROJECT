// animation language
let progressBar = document.querySelector('.circular-progress');
let valueContainer = document.querySelector('.value-container');

let progressBar2 = document.querySelector('.circular-progress2');
let valueContainer2 = document.querySelector('.value-container2');
        
let progressValue = 0;

let progressEndValue = 100;
let progressEndValue2 = 70;

let speed = 50;
        
let progress = setInterval(() => {
    progressValue++;
    valueContainer.textContent = `${progressValue}%`;
    progressBar.style.background = `conic-gradient(
        var(--main-color) ${progressValue * 3.6}deg,
        var(--second-bg-color) ${progressValue * 3.6}deg
    )`;
    if (progressValue >= progressEndValue){
        clearInterval(progress);
    }
}, speed);

let progress2 = setInterval(() => {
    progressValue++;
    valueContainer2.textContent = `${progressValue}%`;
    progressBar2.style.background = `conic-gradient(
        var(--main-color) ${progressValue * 3.6}deg,
        var(--second-bg-color) ${progressValue * 3.6}deg
    )`;
    if (progressValue >= progressEndValue2){
        clearInterval(progress2);
    }
}, speed);