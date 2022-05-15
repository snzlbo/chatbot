const pool = require('../db')

const GET_ADVERTISEMENT_BY_ID = 'SELECT * FROM advertisement WHERE _id = $1;'
const GET_ADVERTISEMENT_BY_TITLE_COMPANY = 'SELECT * FROM advertisement WHERE company ILIKE ($1) AND title ILIKE ($2);'
const GET_ADVERTISEMENT_BY_COMPANY = 'SELECT * FROM advertisement WHERE company ILIKE($1)'
const GET_ADVERTISEMENT_BY_TYPE_TITLE = 'SELECT * FROM advertisement WHERE types ILIKE ($1) AND title ILIKE ($2);'
const GET_ADVERTISEMENT_BY_SALARY_TITLE = 'SELECT * FROM advertisement WHERE "minSalary"  >= ($1) AND title ILIKE ($2); '

const getAdvertisementById = (req, res) => {
  const id = String(req.params['id'])
  console.log(id)
  pool.query(GET_ADVERTISEMENT_BY_ID, [id], (error, results) => {
    if (error) throw error
    res.status(200).json(results.rows)
  })
}

const getAdvertisementByTitleCompany = (req, res) => {
  var company = String(req.params['company'])
  var title = String(req.params['title'])
  title = '%' + title + '%'.replace(' ', '%')
  company = '%' + company + '%'.replace(' ', '%')
  console.log(company, title)
  pool.query(GET_ADVERTISEMENT_BY_TITLE_COMPANY, [company, title], (error, results) => {
    if (error) throw error
    res.status(200).json(results.rows)
  })
}

const getAdvertisementByCompany = (req, res) => {
  var company = String(req.params['comp'])
  company = '%' + company + '%'.replace(' ', '%')
  console.log(company)
  pool.query(GET_ADVERTISEMENT_BY_COMPANY, [company], (error, results) => {
    if (error) throw error
    res.status(200).json(results.rows)
  })
}

const getAdvertisementByTypeTitle = (req, res) => {
  var types = String(req.params['types'])
  var title = String(req.params['title'])
  title = '%' + title + '%'.replace(' ', '%')
  types = '%' + types + '%'.replace(' ', '%')
  console.log(types, title)
  pool.query(GET_ADVERTISEMENT_BY_TYPE_TITLE, [types, title], (error, results) => {
    if (error) throw error
    res.status(200).json(results.rows)
  })
}
const getAdvertisementBySalaryTitle = (req, res) => {
  var salary = parseInt(req.params['salary'])
  var title = String(req.params['title'])
  title = '%' + title + '%'.replace(' ', '%')
  console.log(salary, title)
  pool.query(GET_ADVERTISEMENT_BY_SALARY_TITLE, [salary, title], (error, results) => {
    if (error) throw error
    res.status(200).json(results.rows)
  })
}

module.exports = {
  getAdvertisementById,
  getAdvertisementByTitleCompany,
  getAdvertisementByCompany,
  getAdvertisementByTypeTitle,
  getAdvertisementBySalaryTitle
}
