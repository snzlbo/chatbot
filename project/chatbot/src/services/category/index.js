const { Router } = require('express')
const useGetCategories = require('./list')
const useGetCategory = require('./get')

const router = Router()

router.get('/', useGetCategories.getCategories)
router.get('/:id', useGetCategory.getCategory)

module.exports = router
