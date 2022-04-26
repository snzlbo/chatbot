const pool = require('../db')

const GET_CATEGORIES = 'SELECT * FROM category;'

const getCategories = (req, res) => {
  pool.query(GET_CATEGORIES, (error, results) => {
    if (error) throw error
    res.status(200).json(results.rows)
  })
}

module.exports = { getCategories }
