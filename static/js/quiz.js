function hintOn() {
    if (document.getElementById('hintUl').style.display == 'none') {
        document.getElementById('hintUl').style.display = 'inline-block';
        document.getElementById('hintUl').style.animation = 'fadein 1s';
    } else {
        document.getElementById('hintUl').style.display = 'none';
    }
};

function goback() {
    document.getElementById('hint1').style.display = 'none';
    document.getElementById('hint2').style.display = 'none';
    document.getElementById('hint3').style.display = 'none';
    document.getElementById('hint4').style.display = 'none';
    document.getElementById('hint5').style.display = 'none';
    document.getElementById('hintUl').style.display = 'none';
}

function goquiz(){
    document.getElementById('answer').style.display = 'none';
}

const drawStar = (target) => {
    document.querySelector(`.star span`).style.width = `${target.value * 10}%`;
  }