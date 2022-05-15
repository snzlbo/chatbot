const { Router } = require('express')
const useGetAds = require('./list')
const useGetAd = require('./get')

const router = Router()

router.get('/', useGetAds.getAdvertisements)
router.get('/id=:id', useGetAd.getAdvertisementById)
router.get('/company=:company&title=:title', useGetAd.getAdvertisementByTitleCompany)
router.get('/comp=:comp', useGetAd.getAdvertisementByCompany)
router.get('/types=:types&title=:title', useGetAd.getAdvertisementByTypeTitle)
router.get('/salary=:salary&title=:title', useGetAd.getAdvertisementBySalaryTitle)


module.exports = router
