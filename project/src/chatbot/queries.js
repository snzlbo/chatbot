const getCategories = 'SELECT * FROM category;'
const getCategoryById = 'SELECT * FROM category WHERE _id = $1;'

module.exports = {
  getCategories, 
  getCategoryById
}