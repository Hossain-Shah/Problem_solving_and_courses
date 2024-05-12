const mysql = require('mysql2');
const express = require('express');
const bodyparser = require('body-parser');
var app = express();

//Configuring express server
app.use(bodyparser.json());

//MySQL details
var mysqlConnection = mysql.createConnection({
    host: 'localhost',
    user: 'DB_DEVELOPER',
    password: 'DONT_forget11',
    database: 'mydb',
    multipleStatements: true
    });

mysqlConnection.connect((err)=> {
    if(!err)
    console.log('Connection Established Successfully');
    else
    console.log('Connection Failed!'+ JSON.stringify(err,undefined,2));
    });

//Establish the server connection
//PORT ENVIRONMENT VARIABLE
const port = process.env.PORT || 8080;
app.listen(port, () => console.log(`Listening on port ${port}..`));

//Creating GET Router to fetch all the learner details from the MySQL Database
app.get('/customers' , (req, res) => {
    mysqlConnection.query('SELECT * FROM customers', (err, rows, fields) => {
    if (!err)
    res.send(rows);
    else
    console.log(err);
    })
    } )

//Router to GET specific customers from the MySQL database
app.get('/customers/:id' , (req, res) => {
    mysqlConnection.query('SELECT * FROM customers WHERE name = ?',[req.params.id], (err, rows, fields) => {
    if (!err)
    res.send(rows);
    else
    console.log(err);
    })
    } );

//Router to INSERT/POST a learner's detail
app.post('/customers', (req, res) => {
    let customer = req.body;
    var sql = "SET @name = ?;SET @address = ?;CALL AddOrEdit(@name,@address);";
    mysqlConnection.query(sql, [customer.name, customer.address], (err, rows, fields) => {
    if (!err)
    rows.forEach(element => {
    if(element.constructor == Array)
    res.send('New customer ID : '+ element[0].name);
    });
    else
    console.log(err);
    })
    });

    //Router to UPDATE a learner's detail
app.put('/customers', (req, res) => {
    let customer = req.body;
    var sql = "SET @name = ?;SET @address = ?;CALL AddOrEdit(@name,@address);";
    mysqlConnection.query(sql, [customer.name, customer.address], (err, rows, fields) => {
    if (!err)
    res.send('customer Details Updated Successfully');
    else
    console.log(err);
    })
    });

//Router to DELETE a learner's detail
app.delete('/customers/:id', (req, res) => {
    mysqlConnection.query('DELETE FROM customers WHERE address = ?', [req.params.id], (err, rows, fields) => {
    if (!err)
    res.send('customer Record deleted successfully.');
    else
    console.log(err);
    })
    });