const pool = require('../db')

const GET_ADVERTISEMENTS = 'SELECT * FROM advertisement;'

const getAdvertisements = (req, res) => {
  pool.query(GET_ADVERTISEMENTS, (error, results) => {
    if (error) throw error
    res.status(200).json(results.rows)
  })
}

module.exports = { getAdvertisements }
