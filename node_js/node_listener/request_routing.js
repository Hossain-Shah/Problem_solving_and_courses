const express = require('express')
const app = express()
const port = 3000

app.route('/book')
  .get((req, res) => {
    res.send('Get a random book')
  })
  .post((req, res) => {
    res.send('Add a book')
  })
  .put((req, res) => {
    res.send('Update the book')
  })

  app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
  })