const express = require('express')
const { spawn } = require('child_process');
const app = express()

const categoryRoutes = require('./category/index')
const adRoutes = require('./advertisement/index')
const questionRoutes = require('./pythonScript/index')
app.use(express.json())

app.use('/api/v1/category', categoryRoutes)
app.use('/api/v1/ad', adRoutes)
app.use('/api/v1/question', questionRoutes)

app.listen(4000, () => {
  console.log('Server is listening in port 4000')
})
