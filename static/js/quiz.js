var compteur = 0;
var tableau = document.getElementsByClassName("question-container");
var score = 0;
nombre_question = tableau.length;
tableau[0].style.display = "flex";

var MAX_QESTION = 5;

if (tableau.length< MAX_QESTION){

    MAX_QESTION = tableau.length;
}
RefreshCompteur();


function ShowAnwser(user_anwser) {
    let explications = document.getElementsByClassName("card-text");
    let btns_faux;
    let btns_vrai;
    let newtext;
    let text;
    let anwser;
    if (explications[compteur].style.display === "none") {
        explications[compteur].style.display = 'block';
        anwser = document.getElementsByClassName("card-subtitle")[compteur].innerHTML;
        text = explications[compteur].innerHTML;
        if (text.indexOf("<b") === -1) {
            //Si clique sur VRAI et réponse VRAI
            if (user_anwser && anwser === "True") {
                newtext = "<b style='color:green;'>Bravo! Bonne réponse.</b> La réponse est TRUE.<br>" + text;
                score +=1;
            }
            //Si clique sur VRAI et réponse FAUX
            else if (user_anwser && anwser === "False") {
                newtext = "<b style='color:red;'>Désolé! Mauvaise réponse.</b> La réponse est FALSE.<br>" + text;
            }
            //Si clique sur FAUX et réponse VRAI
            else if (!user_anwser && anwser === "True") {
                newtext = "<b style='color:red;'>Désolé! Mauvaise réponse.</b> La réponse est TRUE.<br>" + text;
            }
            //SI clique sur FAUX et réponse FAUX
            else {
                newtext = "<b style='color:green;'>Bravo! Bonne réponse.</b> La réponse est FALSE.<br>" + text;
                score +=1;
            }
            explications[compteur].innerHTML = newtext;

        } else {
            explications[compteur].innerHTML = text;
        }
        ShowBtnNext();
        HideBtnVrai();
        HideBtnFaux();
        HideTitle();

    } else {

    }

}

function HideTitle(){
    document.getElementsByClassName("card-title-1")[compteur].style.display = "none";
}

function HideBtnVrai(){
    document.getElementsByClassName("btn-vrai")[compteur].style.display = "none";
}
function HideBtnFaux(){
    document.getElementsByClassName("btn-faux")[compteur].style.display = "none";
}
function ShowBtnNext(){
    let btn_next = document.getElementsByClassName("btn-next");
    btn_next[compteur].style.display = "block";
}
function HideBtnNext(){
    let btn_next = document.getElementsByClassName("btn-next");
    btn_next[compteur].style.display = "none";

}
function RefreshCompteur(){
    document.getElementsByClassName("num_question")[compteur].innerHTML = (compteur+1).toString() + " / " + MAX_QESTION.toString();
}
function NextQuestion(){
    HideAnwser();
    compteur +=1;

    if(compteur<MAX_QESTION){
        tableau[compteur-1].style.display = "none";
        tableau[compteur].style.display = "flex";
        HideBtnNext();
        RefreshCompteur();
    }else{
        var score_percent = (score / MAX_QESTION) * 100;
        score_percent = Math.round(score_percent * 100) / 100
        if (score_percent>=50){
            var message = "Félicitations, vous avez " + score_percent.toString() +"% de réponse juste !";
        }else{
            var message = "Vous pouvez mieux faire, vous avez seulement " + score_percent.toString() +"% de réponse juste!";
        }
        if (document.getElementsByClassName("sub_category").length > 0) {


            getJSON("https://slyn4x.pythonanywhere.com/static/json/score_quiz.json").then(json => {
                sub_category = document.getElementsByClassName("sub_category")[0].innerHTML;

                if (score_percent >= 0 && score_percent < 20) {
                    var score_grade = json[sub_category]["1"];
                } else if (score_percent >= 20 && score_percent < 40) {
                    var score_grade = json[sub_category]["2"];
                } else if (score_percent >= 40 && score_percent < 60) {
                    var score_grade = json[sub_category]["3"];
                } else if (score_percent >= 60 && score_percent < 80) {
                    var score_grade = json[sub_category]["4"];
                } else if (score_percent >= 80 && score_percent < 100) {
                    var score_grade = json[sub_category]["5"];
                } else {
                    var score_grade = json[sub_category]["6"];
                }
                document.getElementsByClassName("row")[0].innerHTML = "<div  class='col-sm question-container'><div class='card-final'><form action='redirect_index/' method='post'><input type='hidden' name='csrfmiddlewaretoken' value='" + csrf_token + "'><h2>Grade : " + score_grade + "</h2><p>" + message + "</p><button class='btn' type='submit'>retour</button></form></div></div>"
            })
                .catch(error => {
                    console.error(error);
                    document.getElementsByClassName("row")[0].innerHTML = "<div  class='col-sm question-container'><div class='card-final'><form action='redirect_index/' method='post'><input type='hidden' name='csrfmiddlewaretoken' value='" + csrf_token + "'><p>" + message + "</p><button class='btn' type='submit'>retour</button></form></div></div>"
                });
        }
        else {
            document.getElementsByClassName("row")[0].innerHTML = "<div  class='col-sm question-container'><div class='card-final'><form action='redirect_index/' method='post'><input type='hidden' name='csrfmiddlewaretoken' value='" + csrf_token + "'><p>" + message + "</p><button class='btn' type='submit'>retour</button></form></div></div>"
        }
    }
}
function HideAnwser(){

    let explications = document.getElementsByClassName("card-text");
    explications[compteur].style.display = 'none';
}

function getJSON(url) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);
    xhr.responseType = "json";
    xhr.onload = () => {
      if (xhr.status >= 200 && xhr.status < 300) {
        resolve(xhr.response);
      } else {
        reject(xhr.statusText);
      }
    };
    xhr.onerror = () => reject(xhr.statusText);
    xhr.send();
  });
}