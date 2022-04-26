const pool = require('../db')

const GET_CATEGORY = 'SELECT * FROM category WHERE _id = $1;'

const getCategory = (req, res) => {
  const id = String(req.params['id'])
  pool.query(GET_CATEGORY, [id], (error, results) => {
    if (error) throw error
    res.status(200).json(results.rows)
  })
}

module.exports = { getCategory }
