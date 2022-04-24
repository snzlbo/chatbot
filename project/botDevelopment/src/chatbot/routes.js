const { Router } = require('express')
const controller = require('./controller')

const router = Router()

router.get('/categories', controller.getCategories)
router.get('/category/:id', controller.getCategoryById)
router.get('/ads', controller.getCategories)
router.get('/ads/:id', controller.getAdvertisementById)


module.exports = router 
