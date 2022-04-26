const pool = require('../db')

const GET_ADVERTISEMENT_BY_ID = 'SELECT * FROM advertisement WHERE _id = $1;'
const GET_ADVERTISEMENT_BY_TITLE = 'SELECT * FROM advertisement WHERE company = $1 AND title LIKE($2)'

const getAdvertisementById = (req, res) => {
  const id = String(req.params['id'])
  console.log(id)
  pool.query(GET_ADVERTISEMENT_BY_ID, [id], (error, results) => {
    if (error) throw error
    res.status(200).json(results.rows)
  })
}

const getAdvertisementByTitle = (req, res) => {
  const company = String(req.params['company'])
  var title = String(req.params['title'])
  title = '%' + title + '%'.replace(' ', '%')
  console.log(company, title)
  pool.query(GET_ADVERTISEMENT_BY_TITLE, [company, title], (error, results) => {
    if (error) throw error
    res.status(200).json(results.rows)
  })
}

module.exports = { getAdvertisementById, getAdvertisementByTitle }
