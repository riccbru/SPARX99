<html>

<head>
    <title> Windspeed </title>

</head>

<body>

<?php

    $servername = "";                // mysql server address
    $username = "";                  // mysql username
    $password = "";                  // mysql password
    $dbname = "anemometer";          // database name
    $table = "pellicciotti";         // table pellicciotti@anemometer database
  
    $conn = new mysqli($servername, $username, $password, $dbname);


    $query = "SELECT * FROM pellicciotti";
    $result = $conn->query($query);



    echo '<table border="8" align="center" cellspacing="2" cellpadding="2"> 
    <tr> 
        <td width="200">  <font face="Arial" align="center" color="red">Timestamp</font> </td> 
        <td width="200">  <font face="Arial" align="center" color="red">Windspeed</font> </td> 
    </tr>';

    if ($result) {
        while ($row = $result->fetch_assoc()) {
            $date = $row["timestamp"];
            $speed = $row["windspeed"];

        echo '<tr> 
                    <td>'.$date.'</td> 
                    <td>'.$speed.'</td> 
                </tr>';
    }
    $result->free();
    } 

?>

</body>

</html>
