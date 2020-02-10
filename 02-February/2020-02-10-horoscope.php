<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Horoscope</title>
  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    html, body {
      box-sizing: border-box;
      margin: 0;
      min-height: 100%;
      min-width: 100%;
      padding: 0;
    }
    input, form, p{
      padding: 15px;   
      margin: 5px;
      font-size: 20px;
      text-align: center;
    }
    input{
      background-color: rgba(255,220,220,0.5);
      border: 1px solid rgba(255,220,220,1);
      color: #111;
    }
    #submit{
      background-color: rgba(255,200,200,0.95);
    }
    .earth{
      color: green;
    }
    .water{
      color: blue;
    }
    .fire{
      color: red;
    }
    .air{
      color: gray;
    }
    .sign{
      font-weight: 600;
      color: orange;
    }
  </style>
</head>
<body>


  <form action="" method="get">

    <?php
      function setDefault($default){
        return $default;
      };
      setDefault("1990-01-01");
    ?>

    <p id="date-input">Your birthday: <input type="date" name="bday" id="bday" value="1990-01-01" />
      <input type="submit" id="submit" name="submit" value="Submit"/>
    </p>
  </form>

  <?php

    if(isset($_GET["submit"])){
      start_input();
    } else{      
      setDefault("1990-01-01");
    }

    function start_input(){
      //from https://stackoverflow.com/a/30243885
      $time = strtotime($_GET["bday"]);
      if ($time) {
        calculate_horoscope($time);
      } else {
        echo "<p>Error, try again.</p>";
      }
    }//end start_input()

    function calculate_horoscope($time){
      $dateUnix = strtotime($_GET['bday']);
      $date = date_create();
      date_timestamp_set($date, $dateUnix);
      echo "<p>Your were born on " . date_format($date, "l, F jS, Y") . ".</p>"; 

      $month = date("m", $dateUnix);
      $day = date("d", $dateUnix);
      $year = date("Y", $dateUnix);

      //set date input as the entered date
      echo "<script type='text/javascript'>
    //act on page load
    document.addEventListener('DOMContentLoaded', function(){
      let month = $month;
      let day = $day;
      let year = $year;

      if (month < 10) {
        month = '0'+month;
      } else if (day < 10) {
        day = '0'+day;
      } 
      
      let newDate = year + '-' + month + '-' + day;
      document.getElementById('bday').value = newDate;
    });//end document.addEventListener
  </script>";

      $dailies = ["Be nicer to giraffes",
        "Invest in the environment",
        "Ray guns are not a toy",
        "Breakfast is not more or less important than any other meal",
        "We all die, so take a moment to live",
        "Tomato is a fruit often used as a vegetable: be versatile",
        "Empty the lint trap as you would have others do for you",
        "When did rouge become blush? Take the chance and update your look",
        "Illness is not a fashion statement--enjoy what health you have",
        "Remember that happiness shouldn't be the goal",
        "The color gets is name from the fruit when the fruit is unique enough",
        "Vaccinate your kids, you damn science-hating self-obessed suggestible morons"];

      $daily = $dailies[array_rand($dailies)];

      display_horoscope($month, $day, $daily);
    }//end calculate_horoscope

    function display_horoscope($month, $day, $daily){
      $signs_and_text = [
        "Capricorn" => "Dec. 22 - Jan. 19 <br/>The Mountain Goat.
        <br/><span class='earth'>An Earth sign</span>, ruled by Saturn.",
        "Aquarius" => "Jan. 20 - Feb. 18 <br/>The Man who Carries Water.
        <br/><span class='air'>An Air sign</span>, ruled by Uranus.",
        "Pisces" => "Feb. 19 - March 20 <br/>The Fish.
        <br/><span class='water'>A Water sign</span>, ruled by Neptune.",
        "Aries" => "March 21 - April 19 <br/>The Ram.
        <br/><span class='fire'>A Fire sign</span>, ruled by Mars.",
        "Taurus" => "April 20 - May 20 <br/>The Bull.
        <br/><span class='earth'>An Earth sign</span>, ruled by Venus.",
        "Gemini" => "May 21 - June 20 <br/>The Twins.
        <br/><span class='air'>An Air sign</span>, ruled by Mercury.",
        "Cancer" => "June 21 - July 22 <br/>The Crab.
        <br/><span class='water'>An Water sign</span>, ruled by the Moon.",
        "Leo" => "July 23 - August 22 <br/>The Lion.
        <br/><span class='fire'>A Fire sign</span>, ruled by the Sun.",
        "Virgo" => "August 23 - Sept. 22 <br/>The Maiden.
        <br/><span class='earth'>An Earth sign</span>, ruled by Mercury.",
        "Libra" => "Sept. 23 - October 22 <br/>The Scales.
        <br/><span class='air'>An Air sign</span>, ruled by Venus.",
        "Scorpio" => "October 23 - Nov. 21 <br/>The Scorpion.
        <br/><span class='water'>A Water sign</span>, ruled by Pluto.",
        "Sagittarius" => "Nov. 22 - Dec. 21 <br/>The Centaur.
        <br/><span class='fire'>A Fire sign</span>, ruled by Jupiter."
      ];

      $sign = "";
      $text = "";

      if (($month == "01" && intval($day) < 20) || ($month == "12" && intval($day) > 21)){
        $sign = "Capricorn";
      } else if (($month == "02" && intval($day) < 19) || ($month == "01" && intval($day) > 20)){
        $sign = "Aquarius";
      } else if (($month == "03" && intval($day) < 21) || ($month == "02" && intval($day) > 18)){
        $sign = "Pisces";
      } else if (($month == "04" && intval($day) < 20) || ($month == "03" && intval($day) > 20)){
        $sign = "Aries";
      } else if (($month == "05" && intval($day) < 21) || ($month == "04" && intval($day) > 19)){
        $sign = "Taurus";
      } else if (($month == "06" && intval($day) < 21) || ($month == "05" && intval($day) > 20)){
        $sign = "Gemini";
      } else if (($month == "07" && intval($day) < 23) || ($month == "06" && intval($day) > 20)){
        $sign = "Cancer";
      } else if (($month == "08" && intval($day) < 23) || ($month == "07" && intval($day) > 22)){
        $sign = "Leo";
      } else if (($month == "09" && intval($day) < 23) || ($month == "08" && intval($day) > 22)){
        $sign = "Virgo";
      } else if (($month == "10" && intval($day) < 23) || ($month == "09" && intval($day) > 22)){
        $sign = "Libra";
      } else if (($month == "11" && intval($day) < 22) || ($month == "10" && intval($day) > 22)){
        $sign = "Scorpio";
      } else {
        // if (($month == "12" && intval($day) < 22) || ($month == "11" && intval($day) > 21))
        $sign = "Sagittarius";
      }
      $text = $signs_and_text[$sign];

      echo "<p>Information is from <a href='https://www.horoscopedates.com/zodiac-signs/'>this site</a>.</p>";
      echo "<p>Your sign is <span class='sign'>" . $sign . "</span>.</p>";
      echo "<p>Info about your sign: " . $text . "</p>";
      echo "<p>You insight: " . $daily . ".</p>";

    } //end display_horoscope()
  ?>

</body>
</html>
