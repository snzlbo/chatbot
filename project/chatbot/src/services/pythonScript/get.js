const { spawn } = require('child_process');

const getQuestion = (req, res) => {
  var dataToSend;
  const python = spawn('python', ['./questionUnderstand/script.py']);

  python.stdout.on('data', (data) => {
    dataToSend = data.toString()
    myjson = JSON.parse(dataToSend)
    res.status(200).json(myjson)
    console.log(dataToSend)
  });
  python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);
  });
}

module.exports = { getQuestion }