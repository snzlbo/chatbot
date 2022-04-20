const pool = require('../../db')
const queries = require('./queries')

const getAdvertisements = (req, res) => {
  console.log('get ads')
}
const getCategories = (req, res) => {
  pool.query(queries.getCategories, (error, results) => {
    if (error) throw error
    res.status(200).json(results.rows)
  })
}

const getCategoryById = (req, res) => {
  const id = (req.params['id'])
  pool.query(queries.getCategoryById, [id], (error, results) => {
    if (error) throw error
    res.status(200).json(results.rows)
  })
}

module.exports = {
  getAdvertisements, 
  getCategories, 
  getCategoryById,
}