const pool = require('../db')

const GET_ADVERTISEMENT_BY_ID = 'SELECT * FROM advertisement WHERE _id = $1;'
const GET_ADVERTISEMENT_BY_TITLE_COMPANY = 'SELECT * FROM advertisement WHERE company ILIKE ($1) AND title ILIKE ($2)'
// const GET_ADVERTISEMENT_BY_TITLE = 'SELECT * FROM advertisement WHERE title ILIKE($1)'
// const GET_ADVERTISEMENT_BY_COMPANY = 'SELECT * FROM advertisement WHERE company ILIKE($1)'



const getAdvertisementById = (req, res) => {
  const id = String(req.params['id'])
  console.log(id)
  pool.query(GET_ADVERTISEMENT_BY_ID, [id], (error, results) => {
    if (error) throw error
    res.status(200).json(results.rows)
  })
}

const getAdvertisementByTitleCompany = (req, res) => {
  const company = String(req.params['company'])
  var title = String(req.params['title'])
  title = '%' + title + '%'.replace(' ', '%')
  console.log(company, title)
  pool.query(GET_ADVERTISEMENT_BY_TITLE_COMPANY, [company, title], (error, results) => {
    if (error) throw error
    res.status(200).json(results.rows)
  })
}

// const getAdvertisementByTitle = (req, res) => {
//   var title = String(req.params['title'])
//   title = '%' + title + '%'.replace(' ', '%')
//   pool.query(GET_ADVERTISEMENT_BY_TITLE, [title], (error, results) => {
//     if (error) throw error
//     res.status(200).json(results.rows)
//   })
// }

// const getAdvertisementByCompany = (req, res) => {
//   var company = String(req.params['comp'])
//   company = '%' + company + '%'.replace(' ', '%')
//   pool.query(GET_ADVERTISEMENT_BY_COMPANY[company], (error, results) => {
//     if (error) throw error
//     res.status(200).json(results.rows)
//   })
// }

module.exports = {
  getAdvertisementById,
  getAdvertisementByTitleCompany
}
