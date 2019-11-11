const model = require('../database/models');
const { User } = model;


const express = require('express');
const router = express.Router();

/* GET users listing. */
router.get('/', (req, res, next) => {
  res.send('respond with a resource');
});

router.post('/', async (req, res, next) => {
  const { first_name, last_name, bio } = req.body
  try {
    const userCreateResponse = await User.create({
      first_name,
      last_name,
      bio
    })
    res.send({
      statusCode: 200,
      data: userCreateResponse
    });
  } catch (e) {
    res.send({
      statusCode: 500,
      errorMessage: e.message
    })
  }
});

module.exports = router;
