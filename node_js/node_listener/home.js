const express = require('express')
const router = express.Router()

// define the home page route
router.get('/home', (req, res) => {
    res.send('Home page')
  })

module.exports = router
