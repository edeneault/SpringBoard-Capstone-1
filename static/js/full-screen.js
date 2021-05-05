console.log("full-screen");


function getFullscreenElement() {
    return document.fullscreenElement
        || document.webkitFullscreenElement
        || document.mozFullscreenElement
        || document.msFullscreenElement;
}

function toggleFullScreen() {
    if (getFullscreenElement()) {
        document.exitFullscreen();
    } else {
        document.documentElement.requestFullscreen().catch(console.log);
    }
}

document.addEventListener("fullscreenchange", () => {
    console.log("full screen changed!");
});
