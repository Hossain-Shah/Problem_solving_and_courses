const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('This test script will be launched through test local server address http://localhost:3000/')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})