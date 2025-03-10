player_name = prompt("enter your name dingbangle");
alert("hello " + player_name);
player_guess = prompt("yk how to play rok paper scissors");
computer_guess = randomintfrominterval(Rok, paper, scissors);
if (player_guess == computer_guess) {
  document.getElementById("user_feedback").innerHTML = "correct, you win";
} else {
  document.getElementById("user_feedback").innerHTML =
    "haha loser\n" + "the computer guessed " + computer_guess;
}

function randomintfrominterval(min, max) {
  // min and max included
  return Math.floor(Math.random() * (max - min + 1) + min);
}
