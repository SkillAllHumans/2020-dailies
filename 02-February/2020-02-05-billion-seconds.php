<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Billion Seconds</title>
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
      background-color: rgba(30,87,153,0.4);
      border: 1px solid #1e5799;
      color: #eaeda2;
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

    <p id="date-input">Your birthday: <input type="date" name="bday" value="1990-01-01" /></p>
    <p><input type="submit" id="submit" name="submit" value="submit"/></p>
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
        calculate_billion_seconds($time);
      } else {
        echo "<p>Error, try again.</p>";
      }
    }

    function calculate_billion_seconds($time){
      //https://www.w3schools.com/php/func_date_timestamp_set.asp
      $dateUnix = strtotime($_GET['bday']);
      $date = date_create();
      date_timestamp_set($date, $dateUnix);
      echo "<p>Your were born on " . date_format($date, "l, F jS, Y") . ".</p>"; 

      $billionUnix = $dateUnix + 1000000000;
      $billionDate = date_create();
      date_timestamp_set($billionDate, $billionUnix);
      echo "<p>You hit a billion seconds on approximately " . date_format($billionDate, "l, F jS, Y") . ".</p>";

    } //end calculate_billion_seconds()
  ?>

</body>
</html>
