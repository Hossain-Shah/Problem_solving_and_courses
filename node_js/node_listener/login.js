const express = require('express')
const router = express.Router()

// define the about route
router.get('/login', (req, res) => {
    res.send('Login page')
  })

module.exports = router
