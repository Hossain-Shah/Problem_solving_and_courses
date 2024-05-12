const express = require('express')
const app = express()
const port = 3000

const cb0 = function (req, res, next) {
    console.log('Good')
    next()
  }
  
  const cb1 = function (req, res, next) {
    console.log('morning!')
    next()
  }
  
  app.get('/example/d', [cb0, cb1], (req, res, next) => {
    console.log('the response will be sent by the next function ...')
    next()
  }, (req, res) => {
    res.send('from me!')
  })

  app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
  })