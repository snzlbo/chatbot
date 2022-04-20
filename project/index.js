const express = require('express')
const chatbotRoutes = require('./src/chatbot/routes')
const pool = require('./db')
const app = express()

app.use(express.json())

app.get('/', (req, res) => {
  res.send('Hello world')
})

app.use('/api/v1/chatbot', chatbotRoutes)

app.listen(4000, () => {
  console.log('Server is listening in port 4000')
})