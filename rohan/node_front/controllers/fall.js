var express = require('express');
var router = express.Router();

var fallModel = require('../models/fall');

router.route('/')
  .get(function(req,res) {
        var fallObject = new fallModel();
    // Calling our model function.
    fallObject.getAllfalls(function(err,fallResponse) {
      if(err) {
        return res.json({"responseCode" : 1, "responseDesc" : pollResponse});
      }
      res.json({"responseCode" : 0, "responseDesc" : "Success", "data" : pollResponse});
    });
  })
  .post(function(req,res) {
    // Code to add new polls.
  })
  .put(function(req,res) {
    // Code to update votes of poll.
  });

module.exports = router;
