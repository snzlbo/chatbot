const getCategories = 'SELECT * FROM category;'
const getCategoryById = 'SELECT * FROM category WHERE _id = $1;'
const getAdvertisements = 'SELECT * FROM advertisement;'
const getAdvertisementById = 'SELECT * FROM advertisement WHERE _id = $1;'

module.exports = {
  getCategories, 
  getCategoryById,
  getAdvertisements,
  getAdvertisementById,
}
