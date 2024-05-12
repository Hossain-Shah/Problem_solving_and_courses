var mysql = require('mysql2');

var con = mysql.createConnection({
  host: "localhost",
  user: "DB_DEVELOPER",
  password: "DONT_forget11", 
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  con.query("CREATE DATABASE mydb", function (err, result) {
    if (err) throw err;
    console.log("Database created");
  });
});