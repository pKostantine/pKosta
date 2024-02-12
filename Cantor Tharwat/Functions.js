function ig() {
    window.open("https://www.instagram.com/cantor.tharwat/", "_blank");
}

function fb() {
    window.open("https://www.facebook.com/cantor.tharwat/", "_blank");
}

function sc() {
    window.open("https://soundcloud.com/cantor-tharwat-vmsa", "_blank");
}

function yt() {
    window.open("https://youtube.com/@cantortharwat?si=6tihN2I1KBphjRPL", "_blank");
}

function spotify() {
    window.open("https://open.spotify.com/artist/2gZIRTWfmP04m7PmevWZCq?si=kD-IM-s5SYGiB9bzfX3dKw", "_blank");
}

function apple() {
    window.open("https://music.apple.com/ca/artist/cantor-tharwat/1615194302", "_blank");
}

function homeEN() {
    window.location.href = "EN Home.html"
}

function liveEN() {
    window.location.href = "EN Live.html"
}

function studioEN() {
    window.location.href = "EN Studio.html"
}

function lyricsEN() {
    window.location.href = "EN Lyrics.html"
}

function lessonsEN() {
    window.location.href = "EN Lessons.html"
}

function homeAR() {
    window.location.href = "AR Cantor Tharwat.html"
}

function lyricsLatestEN() {
    window.location.href = "EN Home.html"
}

function listenLatestEN() {
    window.location.href = "EN Live.html"
}

function listenL1EN() {
    window.location.href = "EN Studio.html"
}

function lyricsL1EN() {
    window.location.href = "EN Lyrics.html"
}

function listenL2EN() {
    window.location.href = "EN Studio.html"
}

function lyricsL2EN() {
    window.location.href = "EN Lyrics.html"
}

function listenL3EN() {
    window.location.href = "EN Studio.html"
}

function lyricsL3EN() {
    window.location.href = "EN Lyrics.html"
}

function lLamentationsEN() {
    window.location.href = "EN L-Lamentations.html"
}

function lNativityTasEN() {
    window.location.href = "EN L-NativityTas.html"
}

function lIncenseEN() {
    window.location.href = "EN L-Incense.html"
}

function lPsalmodyEN() {
    window.location.href = "EN L-Psalmody.html"
}

function lLiturgyEN() {
    window.location.href = "EN L-Liturgy.html"
}

function lVenerationEN() {
    window.location.href = "EN L-Veneration.html"
}

function lJoyfulEN() {
    window.location.href = "EN L-Joyful.html"
}

function lVenerationEN() {
    window.location.href = "EN L-Veneration.html"
}

function lVenerationEN() {
    window.location.href = "EN L-Veneration.html"
}

function lVenerationEN() {
    window.location.href = "EN L-Veneration.html"
}

function lVenerationEN() {
    window.location.href = "EN L-Veneration.html"
}

function lVenerationEN() {
    window.location.href = "EN L-Veneration.html"
}

function lVenerationEN() {
    window.location.href = "EN L-Veneration.html"
}

function lVenerationEN() {
    window.location.href = "EN L-Veneration.html"
}

function lVenerationEN() {
    window.location.href = "EN L-Veneration.html"
}

const toggleVisibilityEN = () => {
    lyricsEnglish.forEach(element => {
        element.classList.toggle("hidden");
    });
};

const toggleVisibilityCO = () => {
    lyricsCoptic.forEach(element => {
        element.classList.toggle("hidden");
    });
};

const toggleVisibilityAR = () => {
    lyricsArabic.forEach(element => {
        element.classList.toggle("hidden");
    });
};

document.getElementById("englishBtn").addEventListener("click", () => toggleVisibilityEN());
document.getElementById("copticBtn").addEventListener("click", () => toggleVisibilityCO());
document.getElementById("arabicBtn").addEventListener("click", () => toggleVisibilityAR());

const showLyricsBtn = document.getElementById("showLyricsBtn");
const lyricsContainer = document.querySelector(".lyrics-container");
const lyricsGroup = document.querySelector(".table-lang");
const lyricsEnglish = document.querySelectorAll(".english-lyrics");
const lyricsCoptic = document.querySelectorAll(".coptic-lyrics");
const lyricsArabic = document.querySelectorAll(".arabic-lyrics");
const btnGroup = document.querySelector(".btn-group");
const closeLyricsBtn = document.getElementById("closeLyricsBtn");
// const listContainer = document.querySelector("")
const tempContainer = document.querySelector(".temp-container");
const playerControls = document.querySelector(".player-controls");
const unused = document.querySelector(".unused");

const englishLyrics1 = document.getElementById("englishLyrics1");
const copticLyrics1 = document.getElementById("copticLyrics1");
const arabicLyrics1 = document.getElementById("arabicLyrics1");
const englishLyrics2 = document.getElementById("englishLyrics2");
const copticLyrics2 = document.getElementById("copticLyrics2");
const arabicLyrics2 = document.getElementById("arabicLyrics2");
const englishLyrics3 = document.getElementById("englishLyrics3");
const copticLyrics3 = document.getElementById("copticLyrics3");
const arabicLyrics3 = document.getElementById("arabicLyrics3");
const englishLyrics4 = document.getElementById("englishLyrics4");
const copticLyrics4 = document.getElementById("copticLyrics4");
const arabicLyrics4 = document.getElementById("arabicLyrics4");
const englishLyrics5 = document.getElementById("englishLyrics5");
const copticLyrics5 = document.getElementById("copticLyrics5");
const arabicLyrics5 = document.getElementById("arabicLyrics5");
const englishLyrics6 = document.getElementById("englishLyrics6");
const copticLyrics6 = document.getElementById("copticLyrics6");
const arabicLyrics6 = document.getElementById("arabicLyrics6");
const englishLyrics7 = document.getElementById("englishLyrics7");
const copticLyrics7 = document.getElementById("copticLyrics7");
const arabicLyrics7 = document.getElementById("arabicLyrics7");
const englishLyrics8 = document.getElementById("englishLyrics8");
const copticLyrics8 = document.getElementById("copticLyrics8");
const arabicLyrics8 = document.getElementById("arabicLyrics8");
const englishLyrics9 = document.getElementById("englishLyrics9");
const copticLyrics9 = document.getElementById("copticLyrics9");
const arabicLyrics9 = document.getElementById("arabicLyrics9");
const englishLyrics10 = document.getElementById("englishLyrics10");
const copticLyrics10 = document.getElementById("copticLyrics10");
const arabicLyrics10 = document.getElementById("arabicLyrics10");
const englishLyrics11 = document.getElementById("englishLyrics11");
const copticLyrics11 = document.getElementById("copticLyrics11");
const arabicLyrics11 = document.getElementById("arabicLyrics11");
const englishLyrics12 = document.getElementById("englishLyrics12");
const copticLyrics12 = document.getElementById("copticLyrics12");
const arabicLyrics12 = document.getElementById("arabicLyrics12");
const englishLyrics13 = document.getElementById("englishLyrics13");
const copticLyrics13 = document.getElementById("copticLyrics13");
const arabicLyrics13 = document.getElementById("arabicLyrics13");
const englishLyrics14 = document.getElementById("englishLyrics14");
const copticLyrics14 = document.getElementById("copticLyrics14");
const arabicLyrics14 = document.getElementById("arabicLyrics14");
const englishLyrics15 = document.getElementById("englishLyrics15");
const copticLyrics15 = document.getElementById("copticLyrics15");
const arabicLyrics15 = document.getElementById("arabicLyrics15");
const englishLyrics16 = document.getElementById("englishLyrics16");
const copticLyrics16 = document.getElementById("copticLyrics16");
const arabicLyrics16 = document.getElementById("arabicLyrics16");
const englishLyrics17 = document.getElementById("englishLyrics17");
const copticLyrics17 = document.getElementById("copticLyrics17");
const arabicLyrics17 = document.getElementById("arabicLyrics17");
const englishLyrics18 = document.getElementById("englishLyrics18");
const copticLyrics18 = document.getElementById("copticLyrics18");
const arabicLyrics18 = document.getElementById("arabicLyrics18");
const englishLyrics19 = document.getElementById("englishLyrics19");
const copticLyrics19 = document.getElementById("copticLyrics19");
const arabicLyrics19 = document.getElementById("arabicLyrics19");
const englishLyrics20 = document.getElementById("englishLyrics20");
const copticLyrics20 = document.getElementById("copticLyrics20");
const arabicLyrics20 = document.getElementById("arabicLyrics20");
const englishLyrics21 = document.getElementById("englishLyrics21");
const copticLyrics21 = document.getElementById("copticLyrics21");
const arabicLyrics21 = document.getElementById("arabicLyrics21");
const englishLyrics22 = document.getElementById("englishLyrics21");
const copticLyrics22 = document.getElementById("copticLyrics21");
const arabicLyrics22 = document.getElementById("arabicLyrics21");
const englishLyrics23 = document.getElementById("englishLyrics22");
const copticLyrics23 = document.getElementById("copticLyrics23");
const arabicLyrics23 = document.getElementById("arabicLyrics23");
const englishLyrics24 = document.getElementById("englishLyrics24");
const copticLyrics24 = document.getElementById("copticLyrics24");
const arabicLyrics24 = document.getElementById("arabicLyrics24");

showLyricsBtn.addEventListener("click", () => {
    // lyricsPane.style.display = "block";
    // lyricsContainer.style.display = "block";
    lyricsContainer.style.position = "absolute";
    lyricsContainer.style.top = "0";
    lyricsContainer.style.left = "0";
    lyricsContainer.style.width = "85%";
    lyricsContainer.style.height = "85%";
    lyricsContainer.style.margin = "6rem 0 0 12.8rem";
    lyricsContainer.style.backgroundColor = "rgba(255, 255, 255, 0.95)";
    showLyricsBtn.style.display = "none";
    closeLyricsBtn.style.display = "flex";
    btnGroup.style.position = "absolute";
    btnGroup.style.transform = "translateY(-4rem)"+"translateX(5rem)";
    // lyricsGroup.style.position = "absolute";
    lyricsGroup.style.width = "75rem";
    // lyricsGroup.style.transform = "translateY(-5.95rem)";
    lyricsEnglish.forEach(element => {
        element.style.fontSize = "2.1rem";
    });
    lyricsCoptic.forEach(element => {
        element.style.fontSize = "2rem";
    });
    lyricsArabic.forEach(element => {
        element.style.fontSize = "2.3rem";
    });
    tempContainer.style.display = "block";
    // playerControls.style.position = "fixed";
    // playerControls.style.transform = "translateY(-32.5rem)"+"translateX(36rem)";
    playerControls.style.margin = "-34rem -25rem auto auto"
    playerControls.style.backgroundColor = "#050505";
    playerControls.style.borderRadius = "1rem";
    playerControls.style.boxShadow = "0 15px 30px 5px rgba(0, 0, 0, 0.3)";
    playerControls.style.padding = "1rem 0 1rem 2rem";
    unused.style.filter = "brightness(35%)";
});

closeLyricsBtn.addEventListener("click", () => {
    // lyricsPane.style.display = "none";
    // lyricsContainer.style.display = "block";
    lyricsContainer.style.position = "relative";
    lyricsContainer.style.marginTop = "0";
    lyricsContainer.style.left = "inherit";
    lyricsContainer.style.width = "400px";
    lyricsContainer.style.height = "510px";
    lyricsContainer.style.marginLeft = "12rem";
    lyricsContainer.style.backgroundColor = "#e4e4e4";
    showLyricsBtn.style.display = "flex"
    closeLyricsBtn.style.display = "none";
    btnGroup.style.position = "relative";
    btnGroup.style.transform = "none";
    // lyricsGroup.style.position = "relative";
    lyricsGroup.style.width = "100%";
    lyricsGroup.style.height = "auto";
    // lyricsGroup.style.transform = "none";
    lyricsEnglish.forEach(element => {
        element.style.fontSize = "1.1rem";
    });
    lyricsCoptic.forEach(element => {
        element.style.fontSize = "1.05rem";
    });
    lyricsArabic.forEach(element => {
        element.style.fontSize = "1.2rem";
    });
    tempContainer.style.display = "none"
    // playerControls.style.transform = "none";
    playerControls.style.margin = "inherit"
    playerControls.style.backgroundColor = "#e4e4e4";
    playerControls.style.borderRadius = "0";
    playerControls.style.boxShadow = "none";
    playerControls.style.padding = "0";
    unused.style.filter = "brightness(135%)";
});

// Mobile Adjustments

const menuBtn = document.querySelector("menu-btn");
const menu = document.querySelectorAll("menu");


menuBtn.addEventListener("click", () => {
    menu.style.display = "flex";
    menu.style.marginLeft = "0";
});
