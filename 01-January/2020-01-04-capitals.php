<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Capitals and Times</title>
  <link href="https://fonts.googleapis.com/css?family=Charm" rel="stylesheet">
  <style>
    html {
      height: 100%; /*from https://stackoverflow.com/a/6654996*/
      width: 100%;
    }
    body {
      min-height: 100%;
      min-width: 100%;
    }
    html, body {
      /* modified from http://colorzilla.com/
      background: rgba(30,87,153,0.4); /* Old browsers */
      background: -moz-linear-gradient(left, rgba(30,87,153,0.4) 0%, rgba(47,127,20,0.4) 36%, rgba(85,160,70,0.4) 70%, rgba(0,130,229,0.4) 100%); /* FF3.6-15 */
      background: -webkit-linear-gradient(left, rgba(30,87,153,0.4) 0%,rgba(47,127,20,0.4) 36%,rgba(85,160,70,0.4) 70%,rgba(0,130,229,0.4) 100%); /* Chrome10-25,Safari5.1-6 */
      background: linear-gradient(to right, rgba(30,87,153,0.4) 0%,rgba(47,127,20,0.4) 36%,rgba(85,160,70,0.4) 70%,rgba(0,130,229,0.4) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
      filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='rgba(30,87,153,0.4)', endColorstr='rgba(0,130,229,0.4)',GradientType=1 ); /* IE6-9 */

      box-sizing: border-box;
      margin: 0;
      overflow: hidden;
      padding: 0;
    }

    .output{
      color: #eaeda2;
      font-family: 'Charm', cursive;
      font-size: 30px;
      padding: 5%;
    }
    .date{
      font-weight: bold;
    }

    form, input{
      padding: 15px;   
      margin: 0 auto;
      font-size: 30px;
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

  <form method="post">
      <input type="submit" name="button" value="Get a new place" /><br/>
  </form>

  <?php

  //This started as a fun little take on the Hello Dolly WordPress plugin.
   
  function random_time_zone() {
    $capitals_and_cities = [
      "Albania" => "Tirana",
      "Algeria" => "Algiers",
      "Andorra" => "Andorra La Vella",
      "Angola" => "Luanda",
      "Antigua and Barbuda" => "Saint John's",
      "Armenia" => "Yerevan",
      "Aruba" => "Oranjestad",
      "Australia" => "Canberra",
      "Austria" => "Vienna",
      "Bahamas" => "Nassau",
      "Bahrain" => "Manama",
      "Bangladesh" => "Dhaka",
      "Barbados" => "Bridgetown",
      "Belarus" => "Minsk",
      "Belgium" => "Brussels",
      "Belize" => "Belmopan",
      "Benin" => "Porto Novo",
      "Bermuda" => "Hamilton",
      "Bosnia-Herzegovina" => "Sarajevo",
      "Botswana" => "Gaborone",
      "British Virgin Islands" => "Road Town",
      "Bulgaria" => "Sofia",
      "Burkina Faso" => "Ouagadougou",
      "Burundi" => "Bujumbura",
      "Cameroon" => "Yaoundé",
      "Canada" => "Ottawa",
      "Cayman Islands" => "George Town",
      "Central African Republic" => "Bangui",
      "Chad" => "N'Djamena",
      "China" => "Beijing",
      "Comoros" => "Moroni",
      "Congo" => "Brazzaville",
      "Congo Dem. Rep." => "Kinshasa",
      "Costa Rica" => "San Jose",
      "Cote d'Ivoire (Ivory Coast)" => "Yamoussoukro",
      "Croatia" => "Zagreb",
      "Cuba" => "Havana",
      "Cyprus" => "Nicosia",
      "Cyprus" => "North Nicosia",
      "Czech Republic" => "Prague",
      "Denmark" => "Copenhagen",
      "Djibouti" => "Djibouti",
      "Dominica" => "Roseau",
      "Dominican Republic" => "Santo Domingo",
      "Egypt" => "Cairo",
      "El Salvador" => "San Salvador",
      "Equatorial Guinea" => "Malabo",
      "Eritrea" => "Asmara",
      "Estonia" => "Tallinn",
      "eSwatini" => "Mbabane",
      "Ethiopia" => "Addis Ababa",
      "Finland" => "Helsinki",
      "France" => "Paris",
      "Gabon" => "Libreville",
      "Gambia" => "Banjul",
      "Germany" => "Berlin",
      "Ghana" => "Accra",
      "Gibraltar" => "Gibraltar",
      "Greece" => "Athens",
      "Grenada" => "Saint George's",
      "Guatemala" => "Guatemala City",
      "Guinea" => "Conakry",
      "Guinea-Bissau" => "Bissau",
      "Haiti" => "Port-au-Prince",
      "Honduras" => "Tegucigalpa",
      "Hungary" => "Budapest",
      "Iceland" => "Reykjavik",
      "India" => "New Delhi",
      "Indonesia" => "Jakarta",
      "Iraq" => "Baghdad",
      "Ireland" => "Dublin",
      "Isle of Man" => "Douglas",
      "Israel" => "Jerusalem",
      "Italy" => "Rome",
      "Jamaica" => "Kingston",
      "Japan" => "Tokyo",
      "Jordan" => "Amman",
      "Kenya" => "Nairobi",
      "Kosovo" => "Pristina",
      "Kuwait" => "Kuwait City",
      "Latvia" => "Riga",
      "Lebanon" => "Beirut",
      "Lesotho" => "Maseru",
      "Liberia" => "Monrovia",
      "Libya" => "Tripoli",
      "Liechtenstein" => "Vaduz",
      "Luxembourg" => "Luxembourg",
      "Macedonia, Republic of" => "Skopje",
      "Madagascar" => "Antananarivo",
      "Malawi" => "Lilongwe",
      "Mali" => "Bamako",
      "Malta" => "Valletta",
      "Mauritania" => "Nouakchott",
      "Mexico" => "Mexico City",
      "Moldova" => "Chișinău",
      "Monaco" => "Monaco",
      "Montenegro" => "Podgorica",
      "Montserrat" => "Brades",
      "Morocco" => "Rabat",
      "Mozambique" => "Maputo",
      "Myanmar" => "Naypyidaw",
      "Namibia" => "Windhoek",
      "Nepal" => "Kathmandu",
      "Netherlands" => "Amsterdam",
      "New Zealand" => "Wellington",
      "Nicaragua" => "Managua",
      "Niger" => "Niamey",
      "Nigeria" => "Abuja",
      "North Korea" => "Pyongyang",
      "Norway" => "Oslo",
      "Oman" => "Muscat",
      "Pakistan" => "Islamabad",
      "Palau" => "Ngerulmud",
      "Panama" => "Panama",
      "Pitcairn Islands" => "Adamstown",
      "Poland" => "Warsaw",
      "Portugal" => "Lisbon",
      "Puerto Rico" => "San Juan",
      "Qatar" => "Doha",
      "Romania" => "Bucharest",
      "Russia" => "Moscow",
      "Rwanda" => "Kigali",
      "Saint Helena" => "Jamestown",
      "Saint Kitts and Nevis" => "Basseterre",
      "Saint Lucia" => "Castries",
      "Saint Vincent and Grenadines" => "Kingstown",
      "San Marino" => "San Marino",
      "Sao Tome and Principe" => "São Tomé",
      "Saudi Arabia" => "Riyadh",
      "Senegal" => "Dakar",
      "Serbia" => "Belgrade",
      "Sierra Leone" => "Freetown",
      "Slovakia" => "Bratislava",
      "Slovenia" => "Ljubljana",
      "Somalia" => "Mogadishu",
      "South Africa" => "Pretoria",
      "South Georgia/Sandwich Is." => "King Edward Point",
      "South Korea" => "Seoul",
      "South Sudan" => "Juba",
      "Spain" => "Madrid",
      "Sri Lanka" => "Sri Jayawardenepura Kotte",
      "Sudan" => "Khartoum",
      "Sweden" => "Stockholm",
      "Switzerland" => "Bern",
      "Syria" => "Damascus",
      "Taiwan" => "Taipei",
      "Tanzania" => "Dodoma",
      "Togo" => "Lomé",
      "Trinidad and Tobago" => "Port of Spain",
      "Tunisia" => "Tunis",
      "Turkmenistan" => "Ashgabat",
      "Turks and Caicos Islands" => "Cockburn Town",
      "Uganda" => "Kampala",
      "Ukraine" => "Kyiv",
      "United Arab Emirates" => "Abu Dhabi",
      "United Kingdom" => "London",
      "USA" => "Washington DC",
      "Vatican City State" => "Vatican City",
      "Yemen" => "Sana",
      "Zambia" => "Lusaka",
      "Zimbabwe" => "Harare"];

    // randomly choose a country and capital
    $country = array_rand($capitals_and_cities);
    $capital = $capitals_and_cities[$country];
    
    //get time zone
    $time_zone_codes = [
      "Albania" => "CET",
      "Algeria" => "CET",
      "Andorra" => "CET",
      "Angola" => "WAT",
      "Antigua and Barbuda" => "AST",
      "Armenia" => "AMT",
      "Aruba" => "AST",
      "Australia" => "AEDT",
      "Austria" => "CET",
      "Bahamas" => "EST",
      "Bahrain" => "AST",
      "Bangladesh" => "BST",
      "Barbados" => "AST",
      "Belarus" => "MSK",
      "Belgium" => "CET",
      "Belize" => "CST",
      "Benin" => "WAT",
      "Bermuda" => "AST",
      "Bosnia-Herzegovina" => "CET",
      "Botswana" => "CAT",
      "British Virgin Islands" => "AST",
      "Bulgaria" => "EET",
      "Burkina Faso" => "GMT",
      "Burundi" => "CAT",
      "Cameroon" => "WAT",
      "Canada" => "EST",
      "Cayman Islands" => "EST",
      "Central African Republic" => "WAT",
      "Chad" => "WAT",
      "China" => "CST",
      "Comoros" => "EAT",
      "Congo" => "WAT",
      "Congo Dem. Rep." => "WAT",
      "Costa Rica" => "CST",
      "Cote d'Ivoire (Ivory Coast)" => "GMT",
      "Croatia" => "CET",
      "Cuba" => "CST",
      "Cyprus" => "EET",
      "Cyprus" => "EET",
      "Czech Republic" => "CET",
      "Denmark" => "CET",
      "Djibouti" => "EAT",
      "Dominica" => "AST",
      "Dominican Republic" => "AST",
      "Egypt" => "EET",
      "El Salvador" => "CST",
      "Equatorial Guinea" => "WAT",
      "Eritrea" => "EAT",
      "Estonia" => "EET",
      "eSwatini" => "SAST",
      "Ethiopia" => "EAT",
      "Finland" => "EET",
      "France" => "CET",
      "Gabon" => "WAT",
      "Gambia" => "GMT",
      "Germany" => "CET",
      "Ghana" => "GMT",
      "Gibraltar" => "CET",
      "Greece" => "EET",
      "Grenada" => "AST",
      "Guatemala" => "CST",
      "Guinea" => "GMT",
      "Guinea-Bissau" => "GMT",
      "Haiti" => "EST",
      "Honduras" => "CST",
      "Hungary" => "CET",
      "Iceland" => "GMT",
      "India" => "IST",
      "Indonesia" => "WIB",
      "Iraq" => "AST",
      "Ireland" => "GMT",
      "Isle of Man" => "GMT",
      "Israel" => "IST",
      "Italy" => "CET",
      "Jamaica" => "EST",
      "Japan" => "JST",
      "Jordan" => "EET",
      "Kenya" => "EAT",
      "Kosovo" => "CET",
      "Kuwait" => "AST",
      "Latvia" => "EET",
      "Lebanon" => "EET",
      "Lesotho" => "SAST",
      "Liberia" => "GMT",
      "Libya" => "EET",
      "Liechtenstein" => "CET",
      "Lithuania" => "EET",
      "Luxembourg" => "CET",
      "Macedonia, Republic of" => "CET",
      "Madagascar" => "EAT",
      "Malawi" => "CAT",
      "Mali" => "GMT",
      "Malta" => "CET",
      "Mauritania" => "GMT",
      "Mexico" => "CST",
      "Moldova" => "EET",
      "Monaco" => "CET",
      "Montenegro" => "CET",
      "Montserrat" => "AST",
      "Morocco" => "CET",
      "Mozambique" => "CAT",
      "Myanmar" => "MMT",
      "Namibia" => "CAT",
      "Nepal" => "NPT",
      "Netherlands" => "CET",
      "New Zealand" => "NZDT",
      "Nicaragua" => "CST",
      "Niger" => "WAT",
      "Nigeria" => "WAT",
      "North Korea" => "KST",
      "Norway" => "CET",
      "Oman" => "GST",
      "Pakistan" => "PKT",
      "Palau" => "PWT",
      "Panama" => "EST",
      "Pitcairn Islands" => "PST",
      "Poland" => "CET",
      "Portugal" => "WET",
      "Puerto Rico" => "AST",
      "Qatar" => "AST",
      "Romania" => "EET",
      "Russia" => "MSK",
      "Rwanda" => "CAT",
      "Saint Helena" => "GMT",
      "Saint Kitts and Nevis" => "AST",
      "Saint Lucia" => "AST",
      "Saint Vincent and Grenadines" => "AST",
      "San Marino" => "CET",
      "Sao Tome and Principe" => "WAT",
      "Saudi Arabia" => "AST",
      "Senegal" => "GMT",
      "Serbia" => "CET",
      "Sierra Leone" => "GMT",
      "Slovakia" => "CET",
      "Slovenia" => "CET",
      "Somalia" => "EAT",
      "South Africa" => "SAST",
      "South Georgia/Sandwich Is." => "GST",
      "South Korea" => "KST",
      "South Sudan" => "EAT",
      "Spain" => "CET",
      "Sri Lanka" => "IST",
      "Sudan" => "CAT",
      "Sweden" => "CET",
      "Switzerland" => "CET",
      "Syria" => "EET",
      "Taiwan" => "CST",
      "Tanzania" => "EAT",
      "Togo" => "GMT",
      "Trinidad and Tobago" => "AST",
      "Tunisia" => "CET",
      "Turkmenistan" => "TMT",
      "Turks and Caicos Islands" => "EST",
      "Uganda" => "EAT",
      "Ukraine" => "EET",
      "United Arab Emirates" => "GST",
      "United Kingdom" => "GMT",
      "USA" => "EST",
      "Vatican City State" => "CET",
      "Yemen" => "AST",
      "Zambia" => "CAT",
      "Zimbabwe" => "CAT"];
    $timezone = $time_zone_codes[$country];
    //$time_text = timezone_name_from_abbr($timezone) || "great";
    $date = new DateTime("now", new DateTimeZone($timezone) );
    
    return "The capital of {$country} is {$capital}.<br/> The time is <span class='date'>{$date->format('g:i a')}</span> on <span class='date'>{$date->format('l, F jS, Y')}</span> in the {$timezone} zone.";
  }

  // This echoes the chosen line
  function get_capital() {
    $chosen = random_time_zone();
    echo "<p class='output'>$chosen</p>";
  }

    // call function 
    get_capital();

    //https://stackoverflow.com/a/40958782
    // if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['button'])){
    //   get_capital();
    // }

  ?>

</body>
</html>