const pool = require('../../db')
const queries = require('./queries')


const getCategories = (req, res) => {
  pool.query(queries.getCategories, (error, results) => {
    if (error) throw error
    res.status(200).json(results.rows)
  })
}

const getCategoryById = (req, res) => {
  const id = String(req.params['id'])
  pool.query(queries.getCategoryById, [id], (error, results) => {
    if (error) throw error
    res.status(200).json(results.rows)
  })
}

const getAdvertisements = (req, res) => {
  pool.query(queries.getAdvertisements, (error, results) => {
    if (error) throw error
    res.status(200).json(results.rows)
  })
}

const getAdvertisementById = (req, res) => {
  const id = String(req.params['id'])
  pool.query(queries.getAdvertisementById, [id], (error, results) => {
    if (error) throw error
    res.status(200).json(results.rows)
  })
}

module.exports = {
  getAdvertisements,
  getCategories,
  getCategoryById,
  getAdvertisementById,
}
