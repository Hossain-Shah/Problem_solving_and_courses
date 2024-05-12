const express = require('express')
const homeroute=require("./routes/home.js")
const loginroute=require("./routes/login.js")
const app=express()
  
// Handling routes request
app.use("/",homeroute)
app.use("/",loginroute)

app.listen((3000),()=>{
    console.log("Server is Running")
})