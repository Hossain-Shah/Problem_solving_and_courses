var mysql = require('mysql2');

var con = mysql.createConnection({
  host: "localhost",
  user: "DB_DEVELOPER",
  password: "DONT_forget11",
  database: "mydb"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");

  var create_table = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))";
  con.query(create_table, function (err, result) {
    if (err) throw err;
    console.log("Table created");

  var insert_table_info = "INSERT INTO customers (name, address) VALUES ('Company Inc', 'Highway 37')";
  con.query(insert_table_info, function(err, rows, fields) {
  if (err) throw err;
  console.log("1 record inserted");

  var select_table_info = "SELECT * FROM customers"
  con.query(select_table_info, function (err, result, fields) {
  if (err) throw err;
  console.log(result);

  var where_clause_table_info = "SELECT * FROM customers WHERE address = 'Park Lane 38'"
  con.query(where_clause_table_info, function (err, result) {
  if (err) throw err;
  console.log(result);

  var order_by_clause_table_info = "SELECT * FROM customers ORDER BY name"
  con.query(order_by_clause_table_info, function (err, result) {
  if (err) throw err;
  console.log(result);

  var update_table = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'";
  con.query(update_table, function (err, result) {
  if (err) throw err;
  console.log(result.affectedRows + " record(s) updated");

  var limit_table_info = "SELECT * FROM customers LIMIT 5";
  con.query(limit_table_info, function (err, result) {
  if (err) throw err;
  console.log(result);

  var delete_table = "DELETE FROM customers WHERE address = 'Mountain 21'";
  con.query(delete_table, function (err, result) {
  if (err) throw err;
  console.log("Number of records deleted: " + result.affectedRows);

  });
  });
  });
  });
  });
  });
  });
  });
});