<?php

if(isset($_GET["windspeed"])) {
   $state = $_GET["windspeed"]; 

   $servername = "";                // mysql server address
   $username = "";                  // mysql username
   $password = "";                  // mysql password
   $dbname = "anemometer";          // database name
   $table = "pellicciotti";         // table pellicciotti@anemometer database

   // Create connection
   $conn = new mysqli($servername, $username, $password, $dbname);
   // Check connection
   if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
   }

   //creare una tabella "monitoraggio" con due colonne "timeMYSQL" e "windspeed" o modificare i campi
   //della query sottostante
   $sql = "INSERT INTO $table (windspeed) VALUES ($state)";


   if ($conn->query($sql) == TRUE){
      
      echo "[*] New records created successfully \n";
    
   }
      
   else{
      echo "[!] Error: " . $sql . " => " . $conn->error . "\n";
   }

   $conn->close();
} 
else {
   echo "[!] Stat not set \n";
}
?>
