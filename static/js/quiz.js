function hintOn() {
    if (document.getElementById('hintUl').style.display == 'none') {
        document.getElementById('hintUl').style.display = 'inline-block';
        document.getElementById('hintUl').style.animation = 'fadein 1s';
    } else {
        document.getElementById('hintUl').style.display = 'none';
    }
};

function hint1() {
    modal.style.display = 'block';
}

function goback() {
    modal.style.display = 'none';
    document.getElementById('hintUl').style.display = 'none';
}

function solution() {
    if (document.getElementById('quizText').style.display == 'inline-block') {
        document.getElementById('quizAnswer').style.display = 'inline-block';
        document.getElementById('quizText').style.display = 'none';
        document.getElementById('foo').innerHTML = '문 제';
    }else {
        document.getElementById('quizAnswer').style.display = 'none';
        document.getElementById('quizText').style.display = 'inline-block';
        document.getElementById('foo').innerHTML = '정 답';
    }

};